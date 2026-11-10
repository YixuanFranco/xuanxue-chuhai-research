#!/usr/bin/env python3
"""semrush_pull.py 的离线测试：起一个假的 Semrush MCP 服务器，不联网、不花单位。
用法：python3 工具/test_semrush_pull.py     （全过退出码 0）
覆盖：有 / 无环境变量两种认证、JSON 与 SSE 两种回包、全名表头 → 短码、查无结果记占位行、续跑跳过、--max-units 硬上限、tools 列表。
"""
import csv, json, os, shutil, subprocess, sys, tempfile, threading
from http.server import BaseHTTPRequestHandler, HTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
CALLS = []
AUTH = []


def make_handler(sse):
    class H(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_POST(self):
            AUTH.append(self.headers.get('Authorization'))
            req = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
            if req['method'] == 'tools/list':
                res = {'tools': [{'name': 'execute_report', 'description': 'run', 'inputSchema': {}}]}
            else:
                a = req['params']['arguments']; r, p = a['report'], a['params']
                CALLS.append((r, p.get('phrase') or p.get('domain')))
                assert isinstance(p.get('export_columns', []), list)
                if p.get('phrase') == 'nothing':
                    res = {'content': [{'type': 'text', 'text': 'ERROR 50 :: NOTHING FOUND'}], 'isError': True}
                elif r == 'phrase_this':   # 2026-11-05 实测的真实回包形状
                    sc = {'data': 'Keyword;Search Volume;CPC;Competition;Number of Results;Keyword Difficulty Index;Intent\n'
                                  '%s;1900;1.2;0.3;5000;37;1\n' % p['phrase'],
                          'metadata': {'format': 'csv', 'usage': {'api_units': 10}}}
                    assert p['export_columns'][0] == 'keyword', p['export_columns']
                    res = {'content': [{'type': 'text', 'text': json.dumps(sc)}], 'structuredContent': sc}
                elif r == 'resource_organic':
                    assert 'target' in p and 'domain' not in p
                    res = {'content': [{'type': 'text', 'text': 'Keyword;Position;Search Volume\nbazi;3;1600'}]}
                else:
                    res = {'content': [{'type': 'text', 'text': json.dumps(
                        [{'Domain': 'a.com', 'Url': 'https://a.com/x'}, {'Domain': 'b.com', 'Url': 'https://b.com'}])}]}
            msg = json.dumps({'jsonrpc': '2.0', 'id': 1, 'result': res})
            body = ('event: message\ndata: ' + msg + '\n\n') if sse else msg
            self.send_response(200); self.end_headers(); self.wfile.write(body.encode())
    return H


def serve(sse):
    srv = HTTPServer(('127.0.0.1', 0), make_handler(sse))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return f'http://127.0.0.1:{srv.server_port}/'


def run(work, url, *args, key='FAKE'):
    env = dict(os.environ, SEMRUSH_MCP_URL=url, SEMRUSH_TRANSPORT='mcp',
               NO_PROXY='127.0.0.1', no_proxy='127.0.0.1')
    env.pop('SEMRUSH_API_KEY', None)
    if key:
        env['SEMRUSH_API_KEY'] = key
    return subprocess.run([sys.executable, os.path.join(work, '工具', 'semrush_pull.py'), *args],
                          env=env, capture_output=True, text=True).stdout


def rows(work, name):
    return list(csv.DictReader(open(os.path.join(work, '工具', 'semrush', name), encoding='utf-8')))


def main():
    fails = []
    def check(cond, what):
        print(('✅ ' if cond else '❌ ') + what)
        if not cond:
            fails.append(what)

    work = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(work, '工具'))
        shutil.copy(os.path.join(HERE, 'semrush_pull.py'), os.path.join(work, '工具'))
        with open(os.path.join(work, '工具', 'keywords.csv'), 'w', encoding='utf-8') as f:
            f.write('keyword,family,database,verdict\nbazi chart,东方命理,us,空白\nnothing,东方命理,us,空白\nfeng shui,东方命理,us,强\n')
        sse, js = serve(True), serve(False)

        check('execute_report' in run(work, sse, 'tools'), 'tools 列出 execute_report')
        check(AUTH[-1] == 'Apikey FAKE', '有环境变量时脚本自己加 Authorization: Apikey …')
        check('execute_report' in run(work, sse, 'tools', key=None) and AUTH[-1] is None,
              '没有环境变量时不加认证头、照常发请求（代理注入模式）')

        run(work, sse, 'overview', '--max-units', '1000')
        ov = {r['Ph']: r for r in rows(work, 'overview.csv')}
        check(ov.get('bazi chart', {}).get('Nq') == '1900' and ov['bazi chart'].get('Kd') == '37',
              'SSE + 真实回包形状（data 里套 CSV）→ Nq=1900、Kd=37')
        check(ov.get('nothing', {}).get('Nq') == '0', '查无结果记占位行 Nq=0')
        check(len(ov) == 3, f'overview 3 个词各一行（实际 {len(ov)}）')

        n = len(CALLS)
        run(work, js, 'overview', '--max-units', '1000')
        check(len(CALLS) == n, '续跑：已查过的词不再发请求')

        run(work, js, 'serp', '--only', '空白', '--max-units', '1000')
        sp = rows(work, 'serp.csv')
        check([r['Dn'] for r in sp if r['query'] == 'bazi chart'] == ['a.com', 'b.com'], 'JSON 回包 + Domain → Dn')
        check(any(r['query'] == 'nothing' and r['Dn'] == '(无结果)' for r in sp), 'serp 查无结果占位')
        check(not any(r['query'] == 'feng shui' for r in sp), '--only 空白 只查空白词')

        # 旧表头迁移：先写一个少一列的旧 overview.csv，再追加，表头应合并、旧行不错位
        import semrush_pull as sp_mod  # noqa  (只为确认可导入)
        legacy = os.path.join(work, '工具', 'semrush', 'legacy.csv')
        with open(legacy, 'w', encoding='utf-8') as f:
            f.write('Ph,Nq,database\nold word,100,us\n')
        sys.path.insert(0, os.path.join(work, '工具'))
        import importlib; spm = importlib.import_module('semrush_pull')
        spm.append(legacy, [{'Ph': 'new word', 'Nq': '5', 'Kd': '9', 'database': 'sg'}], ['Ph', 'Nq', 'Kd', 'database'])
        got = list(csv.DictReader(open(legacy, encoding='utf-8')))
        check(got[0]['Ph'] == 'old word' and got[0]['database'] == 'us' and got[1]['Kd'] == '9' and got[1]['database'] == 'sg',
              '表头变化时旧文件先迁移，新旧行都不错位')

        n = len(CALLS)
        out = run(work, js, 'domains', '--max-units', '999')    # 每个域名最坏 100 行 × 10 = 1000 单位 > 999
        check(len(CALLS) == n and '到达上限' in out, '--max-units：最坏单价超上限就一个都不发')
        out = run(work, js, 'domains', '--max-units', '1009')   # 第 1 个按实际 1 行记 10，再加最坏 1000 > 1009
        check(len(CALLS) - n == 1 and '到达上限' in out, '--max-units：按「已用实际 + 下一次最坏」截停')
    finally:
        shutil.rmtree(work)
    print(f'\n{"全部通过" if not fails else f"{len(fails)} 项失败"}')
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
