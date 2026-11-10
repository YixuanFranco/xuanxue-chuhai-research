#!/usr/bin/env python3
"""Semrush 批量查询（玄学出海调研用）。只用 Python 标准库。

密钥从环境变量 SEMRUSH_API_KEY 读，不写进任何文件、不打印。

两种接入（环境变量 SEMRUSH_TRANSPORT 选，默认 mcp）：
  mcp  —— Semrush 给的 MCP 接口 https://mcp.semrush.com/v2/mcp（JSON-RPC，tools/call execute_report）。
          会话网络要放行 mcp.semrush.com。2026-11-05 Yixuan买的 Key 是这一种（<Key>）。
  rest —— 老的 https://api.semrush.com/ 直连。会话网络要放行 api.semrush.com。
查余额（balance）只有 rest 方式有，还要放行 www.semrush.com。

用法：
  python3 工具/semrush_pull.py plan                         # 只算预算，不发请求
  python3 工具/semrush_pull.py tools                        # 只列 MCP 工具与参数格式（不查报表、不花单位）
  python3 工具/semrush_pull.py balance                      # 查剩余单位
  python3 工具/semrush_pull.py overview  [--max-units N]    # 每个词：搜索量 / CPC / 竞争度 / 结果数
  python3 工具/semrush_pull.py serp      [--max-units N] [--only 空白,一般]   # 每个词的 Google 前 10
  python3 工具/semrush_pull.py domains   [--max-units N]    # 核心对手站的前 100 个排名词
  python3 工具/semrush_pull.py related   [--max-units N]    # 种子词的相关词（每个 20 个）
  python3 工具/semrush_pull.py ranks     [--max-units N]    # 站点总量：自然词数 / 自然流量（站点表 工具/domains_rank.csv）
  任一模式加 --keywords 文件.csv 可换词表（database 列决定查哪个国家库）；domains 模式加 --domains 文件.csv 可换站点表

所有结果写到 工具/semrush/*.csv；已查过的词自动跳过（可中断续跑）。
单位按文档估：每行 10（overview / serp / domains），related 每行 40。
**中文词要按字加空格**（如「八字 排 盘」「紫 微 斗 数」）：Semrush 库按字分词，「八字算命」查出来是 0，「八字 算命」才有量。
2026-11-08 第一批中文词一半是这样查成 0 的，用 related 反查才发现。
有来源称 overview 每行 50，所以 plan 同时给出最坏情况；--max-units 是硬上限，到了就停。
"""
import csv, json, os, sys, time, urllib.error, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'semrush')
KEYWORDS = os.path.join(HERE, 'keywords.csv')
API = 'https://api.semrush.com/'
MCP = os.environ.get('SEMRUSH_MCP_URL', 'https://mcp.semrush.com/v2/mcp')
TRANSPORT = os.environ.get('SEMRUSH_TRANSPORT', 'mcp').strip().lower()
DOMAINS_FILE = None   # --domains 文件.csv（domain,database）可换站点表与国家库

# 核心对手站（来自 R1-F1 各词族的核心玩家表）
DOMAINS = ['masterseanchan.com', 'skillon.com', 'onlineclarity.co.uk', 'fengshuied.com',
           'cafeastrology.com', 'astrostyle.com', 'astro-seek.com', 'zodiscope.io',
           'deckaura.com', 'tarotap.com', 'numerologist.com', 'astrosage.com']
# 相关词扩展的种子
SEEDS = ['bazi', 'feng shui', 'zi wei dou shu', 'i ching', 'chinese zodiac',
         'tarot reading', 'birth chart', 'human design', 'numerology', 'ai tarot']

COST = {'overview': (10, 50), 'serp': (10, 10), 'domains': (10, 10), 'related': (40, 40), 'ranks': (10, 10)}
LINES = {'overview': 1, 'serp': 10, 'domains': 100, 'related': 20, 'ranks': 1}
RANKS = os.path.join(HERE, 'domains_rank.csv')   # ranks 模式的站点表：domain,database,segment


def key():
    k = os.environ.get('SEMRUSH_API_KEY', '').strip()
    if not k:
        sys.exit('没有找到环境变量 SEMRUSH_API_KEY。请在云端环境设置的 Network secrets 里添加，然后开新会话。')
    return k


def mcp_auth_headers():
    """MCP 方式的认证头。
    云端会话的 Network secrets 可以让代理自动给 mcp.semrush.com 的请求加
    「Authorization: Apikey <key>」——这时会话里读不到 Key，脚本也不该自己加头（2026-11-05 Yixuan就是这样配的）。
    只有在环境变量里真有 SEMRUSH_API_KEY 时，才由脚本自己加。"""
    k = os.environ.get('SEMRUSH_API_KEY', '').strip()
    return {'Authorization': 'Apikey ' + k} if k else {}


def load_keywords(only=None):
    rows = list(csv.DictReader(open(KEYWORDS, encoding='utf-8')))
    for r in rows:
        r['database'] = (r.get('database') or 'us').strip()
    if only:
        rows = [r for r in rows if r['verdict'] in only]
    return rows


def call(params):
    return call_mcp(params) if TRANSPORT == 'mcp' else call_rest(params)


# Semrush 回包表头是全名（Keyword;Search Volume…），脚本内部用短码；两种都认
COLS = {'Keyword': 'Ph', 'Search Volume': 'Nq', 'CPC': 'Cp', 'Competition': 'Co',
        'Number of Results': 'Nr', 'Domain': 'Dn', 'Url': 'Ur', 'URL': 'Ur',
        'Position': 'Po', 'Traffic': 'Tr', 'Traffic (%)': 'Tr',
        'Keyword Difficulty Index': 'Kd', 'Keyword Difficulty': 'Kd', 'Intent': 'In',
        'Organic Keywords': 'Or', 'Organic Traffic': 'Ot', 'Organic Cost': 'Oc', 'Trend': 'Td'}

# MCP 接口的报表名 / 列名和 REST 不同（2026-11-05 用 get_report_schema 实测）
MCP_REPORT = {'domain_organic': 'resource_organic'}
MCP_COL = {'Ph': 'keyword', 'Nq': 'volume', 'Cp': 'cpc', 'Co': 'competitive_density', 'Nr': 'results',
           'Dn': 'domain', 'Ur': 'url', 'Po': 'position', 'Tr': 'traffic', 'Kd': 'keyword_difficulty',
           'In': 'intent', 'Or': 'organic_keywords', 'Ot': 'organic_traffic', 'Oc': 'organic_traffic_cost', 'Td': 'trend'}
LAST_UNITS = [None]   # 最近一次 MCP 调用回包里写的实际花费（metadata.usage.api_units）


def _norm(rows):
    return [{COLS.get(k.strip(), k.strip()): (v.strip() if isinstance(v, str) else v)
             for k, v in r.items()} for r in rows]


def _rows_from_text(text):
    """报表正文 → 行列表。兼容 Semrush 的分号 CSV 和 JSON 两种写法。"""
    text = (text or '').strip()
    if not text:
        return [], None
    if text.upper().startswith('ERROR'):
        return None, text
    if text[0] in '[{':
        try:
            data = json.loads(text)
        except ValueError:
            data = None
        if isinstance(data, dict) and isinstance(data.get('data'), str):   # 实测格式：{"data": "分号 CSV", "metadata": …}
            return _rows_from_text(data['data'])
        if isinstance(data, dict):
            for k in ('rows', 'data', 'result', 'items'):
                if isinstance(data.get(k), list):
                    data = data[k]; break
        if isinstance(data, list):
            return _norm([d for d in data if isinstance(d, dict)]), None
    lines = [l for l in text.splitlines() if l.strip()]
    head = lines[0].split(';')
    return _norm([dict(zip(head, l.split(';'))) for l in lines[1:]]), None


def mcp_request(method, params=None):
    """发一条 JSON-RPC；返回 (result, 错误文本)。兼容 JSON 和 text/event-stream 两种回包。"""
    body = json.dumps({'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params or {}}).encode()
    req = urllib.request.Request(MCP, data=body, method='POST', headers={
        **mcp_auth_headers(),
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/event-stream',
        'MCP-Protocol-Version': '2025-11-25'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                raw = r.read().decode('utf-8', 'replace')
            break
        except urllib.error.HTTPError as e:
            detail = e.read().decode('utf-8', 'replace')[:300]
            hint = ''
            if e.code in (401, 403) and not mcp_auth_headers():
                hint = ('（会话里没有 SEMRUSH_API_KEY，靠代理注入认证头：检查 Network secrets 里'
                        ' Header name = Authorization、Prefix = Apikey、Allowed websites 含 mcp.semrush.com，并已开新会话）')
            return None, f'HTTP {e.code}：{detail}{hint}'   # 4xx 多是密钥 / 额度问题，不重试
        except Exception as e:
            if attempt == 2:
                return None, f'网络错误：{type(e).__name__}'
            time.sleep(2 * (attempt + 1))
    msg = None
    if raw.lstrip().startswith('{'):
        msg = json.loads(raw)
    else:                                             # SSE：取最后一条 data: 里的 JSON
        for line in raw.splitlines():
            if line.startswith('data:'):
                try:
                    msg = json.loads(line[5:].strip())
                except ValueError:
                    pass
    if not isinstance(msg, dict):
        return None, '回包看不懂：' + raw[:200]
    if 'error' in msg:
        return None, 'ERROR ' + json.dumps(msg['error'], ensure_ascii=False)[:300]
    return msg.get('result'), None


def call_mcp(params):
    p = dict(params)
    report = p.pop('type')
    report = MCP_REPORT.get(report, report)
    if report in ('resource_organic', 'domain_rank') and 'domain' in p:
        p['target'] = p.pop('domain')
    if 'export_columns' in p:
        p['export_columns'] = [MCP_COL.get(c, c) for c in p['export_columns'].split(',')]
    if 'display_limit' in p:
        p['display_limit'] = int(p['display_limit'])
    result, err = mcp_request('tools/call', {'name': 'execute_report',
                                             'arguments': {'report': report, 'params': p}})
    if err:
        return None, err
    parts = [c.get('text', '') for c in (result or {}).get('content', []) if c.get('type') == 'text']
    text = '\n'.join(parts)
    if (result or {}).get('isError'):
        return None, (text if text.upper().startswith('ERROR') else 'ERROR ' + text)[:300]
    if not parts and isinstance((result or {}).get('structuredContent'), (dict, list)):
        text = json.dumps(result['structuredContent'])
    LAST_UNITS[0] = None
    meta = (result or {}).get('structuredContent')
    if isinstance(meta, dict):
        LAST_UNITS[0] = ((meta.get('metadata') or {}).get('usage') or {}).get('api_units')
    return _rows_from_text(text)


def list_tools():
    result, err = mcp_request('tools/list')
    if err:
        sys.exit('❌ ' + err)
    for t in (result or {}).get('tools', []):
        print('●', t.get('name'), '—', (t.get('description') or '')[:200].replace('\n', ' '))
        print('  参数：', json.dumps(t.get('inputSchema', {}), ensure_ascii=False)[:1500])


def call_rest(params):
    params = dict(params, key=key())
    url = API + '?' + urllib.parse.urlencode(params)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                text = r.read().decode('utf-8', 'replace')
            break
        except Exception as e:
            if attempt == 2:
                return None, f'网络错误：{type(e).__name__}'
            time.sleep(2 * (attempt + 1))
    if text.startswith('ERROR'):
        return None, text.strip()
    lines = [l for l in text.strip().splitlines() if l]
    if not lines:
        return [], None
    head = lines[0].split(';')
    return _norm([dict(zip(head, l.split(';'))) for l in lines[1:]]), None


def done_set(path, col):
    """已查过的 (对象, 数据库)；同一个词在不同国家库里算不同的查询。"""
    if not os.path.exists(path):
        return set()
    return {(r[col], r.get('database') or 'us') for r in csv.DictReader(open(path, encoding='utf-8'))}


def append(path, rows, fields):
    """往结果 CSV 追加行。**表头和 fields 不一致时先把旧文件迁到新表头**——
    2026-11-08 踩过：给 domains / related 加了 database 列、overview 加了 Td 列后直接追加，
    新行比旧表头多一列，整列错位，汇总脚本什么都读不到。"""
    if os.path.exists(path):
        with open(path, newline='', encoding='utf-8') as f:
            old_rows = list(csv.reader(f))
        head = old_rows[0] if old_rows else []
        if head and head != list(fields):
            merged = list(fields) + [h for h in head if h not in fields]
            fixed = []
            for r in old_rows[1:]:
                d = dict(zip(head, r))
                if 'database' in merged and not d.get('database'):
                    d['database'] = 'us'          # 旧行默认美国库
                fixed.append(d)
            with open(path, 'w', newline='', encoding='utf-8') as f:
                w = csv.DictWriter(f, fieldnames=merged)
                w.writeheader(); w.writerows(fixed)
            fields = merged
    new = not os.path.exists(path)
    with open(path, 'a', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        if new:
            w.writeheader()
        w.writerows(rows)


def plan(only=None):
    kws = load_keywords(only)
    print(f'关键词 {len(kws)} 个；对手站 {len(DOMAINS)} 个；种子 {len(SEEDS)} 个\n')
    total_lo = total_hi = 0
    for mode, n in (('overview', len(kws)), ('serp', len(kws)), ('domains', len(DOMAINS)), ('related', len(SEEDS))):
        lo, hi = COST[mode]
        a, b = n * LINES[mode] * lo, n * LINES[mode] * hi
        total_lo, total_hi = total_lo + a, total_hi + b
        print(f'{mode:9s} {n:4d} 次 × {LINES[mode]:3d} 行 × {lo}{"–"+str(hi) if hi != lo else ""} 单位 = {a:,}{" – "+format(b, ",") if b != a else ""}')
    print(f'\n合计约 {total_lo:,}（最坏 {total_hi:,}）；试用额度 50,000')


def run(mode, max_units, only=None):
    os.makedirs(OUT, exist_ok=True)
    used, per_line = 0, COST[mode][1]   # 预算按最坏单价算，宁可少查不超支
    if mode in ('overview', 'serp'):
        items = [(r['keyword'], r['database']) for r in load_keywords(only)]
    elif mode == 'domains':
        items = [(r['domain'].strip(), (r.get('database') or 'us').strip()) for r in csv.DictReader(open(DOMAINS_FILE, encoding='utf-8'))] \
            if DOMAINS_FILE else [(d, 'us') for d in DOMAINS]
    elif mode == 'ranks':
        items = [(r['domain'].strip(), r['database'].strip()) for r in csv.DictReader(open(RANKS, encoding='utf-8'))]
    else:
        items = [(r['keyword'].strip(), (r.get('database') or 'us').strip()) for r in csv.DictReader(open(KEYWORDS, encoding='utf-8'))] \
            if '--keywords' in sys.argv else [(s, 'us') for s in SEEDS]
    path = os.path.join(OUT, f'{mode}.csv')
    col = {'overview': 'Ph', 'serp': 'query', 'domains': 'domain', 'related': 'seed', 'ranks': 'domain'}[mode]
    done = done_set(path, col)
    for item, db in items:
        if (item, db) in done:
            continue
        cost = LINES[mode] * per_line
        if used + cost > max_units:
            print(f'⏹ 到达上限 {max_units:,} 单位，停止。已用约 {used:,}。')
            break
        if mode == 'overview':
            rows, err = call({'type': 'phrase_this', 'phrase': item, 'database': db,
                              'export_columns': 'Ph,Nq,Cp,Co,Nr,Kd,In,Td'})
            fields = ['Ph', 'Nq', 'Cp', 'Co', 'Nr', 'Kd', 'In', 'Td', 'database']
            for r in rows or []:
                r['database'] = db
            if rows == []:
                rows = [{'Ph': item, 'Nq': '0', 'database': db}]   # 无数据也记一行，避免重复查
        elif mode == 'serp':
            rows, err = call({'type': 'phrase_organic', 'phrase': item, 'database': db,
                              'display_limit': LINES[mode], 'export_columns': 'Po,Dn,Ur'})
            fields = ['query', 'rank', 'Po', 'Dn', 'Ur', 'database']
            rows = [dict(r, query=item, rank=i + 1, database=db) for i, r in enumerate(rows or [])] or \
                   ([{'query': item, 'rank': 0, 'Dn': '(无结果)', 'database': db}] if err is None else None)
        elif mode == 'domains':
            rows, err = call({'type': 'domain_organic', 'domain': item, 'database': db,
                              'display_limit': LINES[mode], 'export_columns': 'Ph,Po,Nq,Cp,Tr,Ur'})
            fields = ['domain', 'database', 'Ph', 'Po', 'Nq', 'Cp', 'Tr', 'Ur']
            rows = [dict(r, domain=item, database=db) for r in rows or []] or \
                   ([{'domain': item, 'database': db, 'Ph': '(无数据)'}] if err is None else None)
        elif mode == 'ranks':
            rows, err = call({'type': 'domain_rank', 'domain': item, 'database': db,
                              'export_columns': 'Dn,Or,Ot,Oc'})
            fields = ['domain', 'database', 'Or', 'Ot', 'Oc']
            rows = [dict(r, domain=item, database=db) for r in rows or []] or \
                   ([{'domain': item, 'database': db, 'Ot': '0'}] if err is None else None)
        else:
            rows, err = call({'type': 'phrase_related', 'phrase': item, 'database': db,
                              'display_limit': LINES[mode], 'export_columns': 'Ph,Nq,Cp,Co,Nr,Kd'})
            fields = ['seed', 'database', 'Ph', 'Nq', 'Cp', 'Co', 'Nr', 'Kd']
            rows = [dict(r, seed=item, database=db) for r in rows or []] or \
                   ([{'seed': item, 'database': db, 'Ph': '(无数据)'}] if err is None else None)
        if err:
            print(f'❌ {item}: {err}')
            if 'NOTHING FOUND' not in err.upper():
                if any(w in err.upper() for w in ('LIMIT', 'UNITS', 'WRONG KEY', 'HTTP 401', 'HTTP 403', 'HTTP 402')):
                    print('⏹ 额度或密钥问题，停止。'); break
                continue
            # 查无结果也记一行，续跑时跳过、不重复花单位
            rows = [{'overview': {'Ph': item, 'Nq': '0', 'database': db},
                     'serp': {'query': item, 'rank': 0, 'Dn': '(无结果)', 'database': db},
                     'domains': {'domain': item, 'Ph': '(无数据)'},
                     'related': {'seed': item, 'Ph': '(无数据)'},
                     'ranks': {'domain': item, 'database': db, 'Ot': '0'}}[mode]]
        append(path, rows, fields)
        actual = LAST_UNITS[0] if TRANSPORT == 'mcp' else None
        used += actual if isinstance(actual, (int, float)) else max(len(rows), 1) * per_line
        print(f'✅ {item}（{len(rows)} 行，累计{"" if isinstance(actual, (int, float)) else "约"} {used:,} 单位）')
        time.sleep(0.2)
    print(f'结果：{path}')


def balance():
    if TRANSPORT == 'mcp':
        sys.exit('MCP 方式没有查余额接口：去 Semrush 网页后台看剩余单位，或设 SEMRUSH_TRANSPORT=rest 并放行 www.semrush.com。')
    url = 'https://www.semrush.com/users/countapiunits.html?key=' + urllib.parse.quote(key())
    with urllib.request.urlopen(url, timeout=30) as r:
        print('剩余单位：', r.read().decode().strip())


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args or args[0] not in ('plan', 'tools', 'balance', 'overview', 'serp', 'domains', 'related', 'ranks'):
        print(__doc__); sys.exit(2)
    max_units = int(args[args.index('--max-units') + 1]) if '--max-units' in args else 15000
    if '--domains' in args:
        DOMAINS_FILE = os.path.abspath(args[args.index('--domains') + 1])
    if '--keywords' in args:   # 换一张词表，如 工具/keywords_intl.csv（同一批词放到别的国家库里查）
        KEYWORDS = os.path.abspath(args[args.index('--keywords') + 1])
    only = set(args[args.index('--only') + 1].split(',')) if '--only' in args else None
    if args[0] == 'plan':
        plan(only)
    elif args[0] == 'tools':
        list_tools()
    elif args[0] == 'balance':
        balance()
    else:
        run(args[0], max_units, only)
