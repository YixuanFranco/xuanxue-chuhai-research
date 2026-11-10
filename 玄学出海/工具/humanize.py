#!/usr/bin/env python3
"""把玄学出海报告里的「字母 + 数字」代号换成有语义的名字（Yixuan 2026-11-05 要求）。
  python3 工具/humanize.py --dry   # 只统计每个文件会换多少处，不写文件
  python3 工具/humanize.py         # 写回
  python3 工具/humanize.py --check # 汇总报告里还剩多少代号（0 才算干净）
规则：
  · 不动代码块、`行内代码`、链接地址（文件名本身含 R1-A 之类，不能改）。
  · 「R1-D A1」「R1-A #22」「R1-E §5」这类跨文件引用 → 「规则与风险调研「Apple 4.3(b)…」」：
    到被引用文件的表格 / 小标题里查那一行的真实标题。
  · 汇总报告（01、03、03a、R4-0、04、05、PLAN）里的市场代号、候选代号、方法论代号、备选项编号也换。
  · R1 原始调研文件只换跨文件引用；它们自己表格第一列的行编号（C1、A1…）旁边就是名字，保留。
"""
import glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SYNTH = ['01-充分做加法-备选项池.md', '03-行业画布-AB模型.md', '03a-追问-独立站与印度.md',
         'R4-0-Semrush第一批-空白复核与多国需求.md', '04-集中度-相关市场.md', '05-专业做减法.md', '06-OSCAR-候选深挖.md', 'PLAN.md']

SRC = {  # 代号 → (语义名, 文件 glob)
    'R1-F1-a': ('西占塔罗查词', 'R1-F1-a-*.md'), 'R1-F1-b': ('东方命理查词', 'R1-F1-b-*.md'),
    'R1-F1-c': ('新灵性与 AI 查词', 'R1-F1-c-*.md'), 'R1-F1-d': ('多语种查词', 'R1-F1-d-*.md'),
    'R1-F3': ('糊站验尸', 'R1-F3-*.md'), 'R1-F1': ('查词调研', None),
    'R1-A': ('规模与集中度调研', 'R1-A-*.md'), 'R1-B': ('方向全景调研', 'R1-B-*.md'),
    'R1-C': ('中国团队案例调研', 'R1-C-*.md'), 'R1-D': ('规则与风险调研', 'R1-D-*.md'),
    'R1-E': ('单位经济调研', 'R1-E-*.md'), 'R4-0': ('Semrush 第一批数据', 'R4-0-*.md'),
}
MARKET = {
    'M-a': '英语真人撮合市场', 'M-b': '西占订阅 App 市场', 'M-c': '西占与新灵性内容 / 免费工具市场',
    'M-d': 'AI 解读市场', 'M-e': '灵性实物市场', 'M-f': '非英语本土市场', 'M-g': '2B 工具与培训市场',
    'E1': '东南亚华人命理市场', 'E2': '欧美泛文化东方玄学市场',
}
CAND = {'K1': '①华人高客单咨询', 'K2': '②英文排盘工具站', 'K3': '③英文命理课程', 'K4': '④命理配实物'}
METH = {'M1': '商业预判（加法 / 减法）', 'M2': '投资人大哉 9 问', 'M3': 'AB 模型与行业画布',
        'M4': '集中度方法', 'M5': 'OSCAR 调研五部曲', 'M6': '麦肯锡框架'}
CASE = {'C1': 'FateTell', 'C2': 'Timing（顺时）', 'C3': '东海水晶', 'C4': '卡牌代工厂', 'C5': 'Joey Yap',
        'C6': '国内命理 App 挂海外区', 'C7': 'TikTok 直播 MCN', 'C8': '中国团队踩坑'}
OPT_FIX = {5: '合盘恋爱 App', 22: '聊天机器人占卜', 33: '付费占星专栏', 40: '卡牌代工对接', 47: '可打印学习卡',
           51: '多语种占星 SEO 站', 62: '命理师供给培训输出', 63: '命理 × 约会', 66: '新奇灵性概念 PDF',
           70: 'Reality shifting 工具', 3: '品牌订阅占星 App', 28: '英文命理大师高客单咨询', 58: '占星合盘 API',
           13: '日本占い货架', 14: '吠陀占星报告（印度侨民）', 17: 'AI 风水户型图', 21: 'AI + 真人混合',
           24: '中国命理师 × 海外用户撮合', 29: '企业风水 / 择日顾问', 9: '生肖年运报告', 38: '按八字配水晶手串',
           6: '人类图 App', 7: '数字命理报告', 73: '泰国吉祥号码计算器', 77: '星图地图 + AI 解读'}

PROTECT = re.compile(r'```.*?```|`[^`\n]*`|\]\([^)\n]*\)|https?://\S+', re.S)


def clean(t):
    t = re.sub(r'<[^>]+>', ' ', t).replace('**', '').strip()
    t = re.split(r'[：:（(。；;|]', t)[0].strip()
    return t[:24]


def index_file(pattern):
    """表格首列 ID → 第二列标题；小标题编号 → 标题。"""
    idx = {}
    files = glob.glob(os.path.join(ROOT, pattern)) if pattern else []
    for path in files:
        for line in open(path, encoding='utf-8'):
            c = [x.strip() for x in line.strip().strip('|').split('|')]
            if line.lstrip().startswith('|') and len(c) >= 2:
                k = c[0].replace('**', '')
                if re.fullmatch(r'[A-Z]\d{1,2}|\d{1,3}', k) and c[1] and not re.fullmatch(r'-+', c[1]):
                    idx.setdefault(k, clean(c[1]))
            m = re.match(r'#{2,4}\s+(?:§)?(\d+)[.、\s]\s*(.+)', line)
            if m:
                idx.setdefault('§' + m.group(1), clean(m.group(2)))
    return idx


IDX = {code: index_file(g) for code, (_, g) in SRC.items()}
OPT = {}
OPT_AUTO = {}


def load_opts():
    for line in open(os.path.join(ROOT, '01-充分做加法-备选项池.md'), encoding='utf-8'):
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(c) >= 7 and re.fullmatch(r'\d+', c[0]) and 1 <= int(c[0]) <= 77:
            OPT.setdefault(int(c[0]), re.split(r'[（(：:]', c[1].replace('**', ''))[0].strip()[:20])
    OPT_AUTO.update(OPT)
    OPT.update(OPT_FIX)


SRC_RE = re.compile(r'(?<![\w/`-])(R1-F1-[abcd]|R1-F1|R1-F3|R1-[A-E]|R4-0)(?![\w-])'
                    r'(?:\s?((?:#\d+(?:[–\-]\d+)?)(?:\s?/\s?#\d+)*|§\d+|[A-Z]\d{1,2}\b))?')


def src_sub(m):
    code, ref = m.group(1), m.group(2)
    name = SRC[code][0]
    if not ref:
        return name
    if ref.startswith('§'):
        lab = IDX[code].get(ref)
        return f'{name}「{lab}」一节' if lab else f'{name}第 {ref[1:]} 节'
    if ref.startswith('#'):
        nums = re.findall(r'\d+(?:[–\-]\d+)?', ref)
        labs = [IDX[code].get(n) for n in nums]
        if len(nums) == 1 and labs[0]:
            return f'{name}「{labs[0]}」'
        if all(labs):
            return f'{name}「' + '」「'.join(labs) + '」'
        return f'{name}第 {"、".join(nums)} 条'
    if code == 'R1-C' and ref in CASE:
        return f'{name}「{CASE[ref]}」'
    lab = IDX[code].get(ref)
    return f'{name}「{lab}」' if lab else f'{name} {ref}'


def opt_sub(m):
    a, b = m.group(1), m.group(2)
    if b:
        return f'第 {a}–{b} 条备选项'
    n = int(a)
    name = OPT.get(n)
    after = m.string[m.end():m.end() + 8].lstrip()
    auto = OPT_AUTO.get(n, name or '')
    if not name or after.startswith('「') or after.startswith(name[:4]) or (auto and after.startswith(auto[:4])):
        return m.group(0)
    return f'#{n}「{name}」'


def transform(text, synth):
    out, pos = [], 0
    for m in PROTECT.finditer(text):
        out.append(conv(text[pos:m.start()], synth)); out.append(m.group(0)); pos = m.end()
    out.append(conv(text[pos:], synth))
    return ''.join(out)


def conv(t, synth):
    t = SRC_RE.sub(src_sub, t)
    # 「规则与风险调研 二.3 / D4」这种一个引用里串了多个行号：把落单的行号也换成标题
    t = re.sub(r'(规则与风险调研[^（）()\n]{0,14}?)(?<![\w-])([A-E]\d)(?![\w-])',
               lambda m: m.group(1) + '「' + IDX['R1-D'].get(m.group(2), m.group(2)) + '」', t)
    if not synth:
        return t
    # 市场：标题 / 加粗里「代号 + 自己的描述」→ 去掉代号；其余 → 换名字
    # 标题、加粗开头、列表项开头的「代号 + 描述」：只删代号，保留 # / ** / - 本身
    t = re.sub(r'\*\*(M-[a-g]|E[12])\*\*\s+(?=\S)', '', t)                     # 「**M-a** 描述」→「描述」
    t = re.sub(r'\*\*(M-[a-g]|E[12])\s+(?=\S)', '**', t)                         # 「**E1 描述**」→「**描述**」
    t = re.sub(r'^(\s*[-*]\s+)(M-[a-g]|E[12])\s+(?=\S)', r'\1', t, flags=re.M)    # 列表项开头
    t = re.sub(r'^#{2,4}\s.*$', lambda m: re.sub(r'(?<![\w-])(M-[a-g]|E[12])\s+', '', m.group(0)), t, flags=re.M)  # 标题里全部
    t = re.sub(r'(?<![\w-])(M-[a-g])(?![\w-])', lambda m: MARKET[m.group(1)], t)
    t = re.sub(r'(?<![\w-])(E[12])(?![\w-])', lambda m: MARKET[m.group(1)], t)
    t = re.sub(r'(?<![\w>-])>?(K[1-4])(?![\w-])', lambda m: CAND[m.group(1)], t)
    t = re.sub(r'(?<![\w-])(M[1-6])(?![\w-])', lambda m: METH[m.group(1)], t)
    t = re.sub(r'(?<![\w-])(C[1-8])(?![\w-])', lambda m: CASE[m.group(1)], t)
    t = re.sub(r'(?<![\w&#])#(\d{1,2})(?:[–\-](\d{1,2}))?(?![\d\w])', opt_sub, t)
    return t


LEFT = re.compile(r'(?<![\w/`-])(?:R1-(?:F1-[abcd]|F1|F3|[A-E])|R4-0)(?![\w-])|(?<![\w-])(?:M-[a-g]|E[12]|K[1-4]|M[1-6]|C[1-8])(?![\w-])')


def strip_protected(t):
    return PROTECT.sub(' ', t)


def main():
    load_opts()
    dry, chk = '--dry' in sys.argv, '--check' in sys.argv
    files = sorted(glob.glob(os.path.join(ROOT, '*.md')))
    total = 0
    for path in files:
        base = os.path.basename(path)
        synth = base in SYNTH or base.startswith('R6-')   # R6 起新写的文件都按汇总报告的标准查
        old = open(path, encoding='utf-8').read()
        if chk:
            if synth:
                n = len(LEFT.findall(strip_protected(old)))
                total += n
                print(f'{"✅" if n == 0 else "❌"} {base}: 剩 {n} 处代号')
            continue
        new = transform(old, synth)
        diff = sum(1 for a, b in zip(old.splitlines(), new.splitlines()) if a != b)
        print(f'{base}: 改动 {diff} 行')
        if not dry and new != old:
            open(path, 'w', encoding='utf-8').write(new)
    if chk:
        print(f'合计剩 {total} 处')
        sys.exit(1 if total else 0)


if __name__ == '__main__':
    main()
