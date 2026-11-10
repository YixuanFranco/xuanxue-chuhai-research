#!/usr/bin/env python3
"""R5 专业做减法：77 个备选项逐条过 A 维度 10 个误判 + B 维度团队匹配。
判断写在下面 DATA 里（一行一条），脚本负责校验和出表：
  python3 工具/subtract.py           # 打印 Markdown 表（05 文档用）
  python3 工具/subtract.py --check   # 校验：77 条齐全；划掉的必须有 ≥1 个死因代码 + 依据；并入的必须指向候选
死因代码（Yixuan提供的方法论原文）：
  A1 需求不刚  A2 天花板低  A3 方案不成立  A4 单元模型不成立  A5 持续性差
  A6 周期性差  A7 缺增长路径  A8 错过窗口  A9 缺壁垒  A10 规模不经济
  B1 缺初心  B2 缺关键能力  B3 缺文化基因  B4 缺起盘资金  B5 缺关键资源
  R  规则 / 合规（平台或法律直接卡死——方法论里没有单列，归在「持续性差」的环境变化之下，这里单独标出来便于看）
结论：K1–K4 = 候选；>Kx = 并入该候选（作为它的一个产品 / 渠道 / 交付方式，不单独成项）；X = 划掉。
"""
import re, sys

CANDIDATES = {
    'K1': 'E1 华人高客单命理咨询（八字 / 紫微 / 风水 / 择日；英文 + 中文；新马港 + 海外华人）',
    'K2': '英文八字 / 紫微排盘工具站 + AI 报告（获客前端，导流 K1）',
    'K3': '英文东方命理课程 / 认证（培养海外学习者与从业者）',
    'K4': '命理 × 实物：按八字配水晶 / 风水摆件（K1 / K2 的追加销售）',
}

# 编号 | 结论 | 死因代码 | 依据（文件 / 数字）
DATA = '''
1|X|A8 R B2|西占 Web2App 是结束战斗型（R4 M-b）；加州 ARL / ROSCA 直压试用扣费（R1-D）；投流能力是空白（PLAN 资源）
2|X|A2 B2|八字类核心词美区约 7,200 次 / 月（R4-0），撑不起投流漏斗；投流能力空白。交付思路并入 K2
3|X|A8 R B2|Apple 4.3(b) 不收新算命 App（R1-D ✅）；Co-Star 被收购、头部持平（R1-A）
4|X|A8 R|同 #3；The Pattern 已占「心理化关系解释」位（R1-F1-c）
5|X|A8 R|Tinder 2026-04 自做合盘（R1-B ✅）；4.3(b) 约会与算命同句点名（R1-D）
6|X|A3 B2|iOS 已有 6+ 人类图 App（R1-F1-c）；团队无人类图专业
7|X|A9 B2|numerology 美区 55 万但 KD 89、老站占位（R4-0）；非团队专业
8|X|A4 A9|单个 AI 塔罗 App 多数 <$1 万 / 月（R1-F1-c）；Labyrinthos 等长期占位
9|>K2|A6 A8|生肖年运季节性强、2027 页已有 7+ 站（R1-F1-b）；chinese zodiac 2026 美区 2.2 万 KD 29（R4-0）→ 作 K2 的季节内容
10|>K1|A2|宝宝星盘 Etsy 7 年 1.8k 单（R1-B），单独做太小 → 作 K1 的「八字起名」服务项
11|>K1|A2|择日无出海规模玩家（R1-B）；masterseanchan 按月铺吉日页（R1-F1-b）→ 作 K1 服务项
12|X|B2 A9|韩语 / 韩国文化不是团队能力；Naver、银行 App 免费送运势（R1-F1-d）
13|X|B2 B5|日语与 LINE 货架合作资源都没有；且 App/SNS 占卜持平（R1-A ✅）
14|X|A8 B2|Astrotalk 已在吃印度侨民（海外 ₹621 crore ✅）；团队不做吠陀
15|X|A3 A9 R|AI 塔罗前 10 全是 AI 站（R1-F1-a）；挂牌月利 $2.4–3.3k（⚠️）；4.3(b)
16|>K2|A3|单独做会被免费大模型替代（R1-C）；作 K2 的 AI 报告交付方式
17|X|A1|「AI feng shui floor plan」美区 0 量（R4-0）；bagua map 有量但是内容词 → 进 K2 / K3 内容
18|X|A3 R|5+ 同质 AI 看手相 App（R1-F1-c）；Apple 1.1.6「仅供娱乐」挡不住（R1-D ✅）
19|X|A3 B2|AI 解梦多为 ChatGPT 套壳（R1-F1-c）；非团队专业
20|X|A1 A3|无需求证据（R1-B ❓）；通用大模型就能陪聊
21|>K1|A8|美英独立做是 Nebula / Astrotalk 的地盘（R4 M-a）；「AI 先解读、不满意转真人」作 K1 的交付结构
22|X|A1 R|PH 玩家 3 个关注（R1-B）；越南组织迷信活动可罚（R1-D）
23|X|A8 B4 B5|美国线上撮合搜索侧 CR3≈95%（R4 M-a）；需要顾问网络和获客资金
24|X|A2 A10|E1 核心搜索约 1.9 万次 / 月（R4），撑不起双边平台抽佣；平台依赖人、规模不经济
25|>K1|A1|只有 ⚠️ 证据；「中文服务海外华人」作 K1 的语言版本
26|X|B2 R A8|泰 / 越 / 印尼语不是团队能力；Stripe 泰国主体据称禁 psychic（R1-D）；InstaAstro 已拿 A 轮
27|X|A8 B4|Purple Garden 类视频平台已集中（R4 M-a）；需要大额资金
28|K1||masterseanchan 报告 $488–588、面谈 $1,288、自称排队 50–60 工作日（R1-F1-b 🟡 / ⚠️）；E1 偏分散（R4）；团队是命理实践者 + 有私域高客单 SOP
29|>K1|A10|新加坡办公室风水审计 S$800–1,688+（R1-B）；要上门、服务半径受限 → 作 K1 的线上风水 / 远程勘测项
30|X|R B2|以导流站外为主的 LIVE 不进推荐流（R1-D ✅）；海外直播未测（PLAN）
31|X|A4|25.6 万订阅估广告 $2K / 月（R1-B）；单独做不成立，可作 K3 的获客渠道
32|>K3|A4|单独内容 IP 难变现；作 K3 的获客内容（Joey Yap 就是内容 → 课程）
33|X|B2 A2|西占专栏非团队专业；头部个人年入十万美元级（R1-B）
34|X|A2|Patreon $3.69 / 月级（R1-B）；付费人数未查到
35|X|A1 B2|塔罗 MCN 一个案例都没有（R1-C）；海外直播未测
36|X|R A9|TikTok 要求 AI 内容打标、非原创不计收益（R1-D ✅）
37|X|A5 A8|美国 TikTok 水晶饱和、2024–25 下行（R1-C）
38|K4||Etsy 八字五行手串 $50–190、几家在做无规模（R1-B）；Astrotalk 电商 ₹166 crore 占营收 9%（R1-A ✅）证明「咨询 + 开运商品」路径；可去东海一手
39|X|B2 A2|西方塔罗牌设计与众筹不是团队能力；实物 5 年增量仅 $1.98 亿（⚠️）
40|X|A8 A9|广东 / 香港多家厂已饱和抢英文 SEO（R1-C）
41|>K4|A9|风水摆件单独做无壁垒（太岁词被珠宝品牌占）；作 K4 的品类
42|X|A5|Goddess Provisions 2024-04 停办（R1-B）
43|X|R B3|印尼新刑法打击卖法术（R1-D）；真假难辨、信任成本高（R1-B）
44|X|A9|Etsy 标「witch」商品 40 万+（R1-B）
45|X|A4 B2|$5–15 单被扣 19–34%（R1-E）；西方塔罗非团队专业
46|X|B2 A9|星盘海报是西占 + 设计生意
47|X|A2 A9|需求未查到；无壁垒
48|>K2|A2|Etsy 八字店评价 8–23 条（R1-B），单独做太小；作 K2 的付费报告
49|K2||bazi calculator 美 5,400 / 新 3,600 / 马 3,600 / 菲 1,900 次 / 月（R4-0）；skillon 等老站用神放付费墙（R1-F1-b）；单独靠广告撑不起，价值在导流 K1
50|X|A2 A9 B2|西占计算器有缝（saturn return 9,900 KD 20）但靠广告、非团队专业（R4 §五）
51|X|B2 A9|西 / 葡 / 印尼语不是团队能力；巴西 Personare 一家独大（R1-F1-d）
52|X|A9 A2|起名生成器 AI 站泛滥、意图偏写作（R1-F1-b）
53|K3||Joey Yap 第三方估营收 $5–20M（R1-B 🟡）；masterseanchan 课 $1,688 / 96 课时（R1-F1-b）；Yixuan有玄学卖课约 200 万元（自述）
54|X|B5 A1|西方顾问圈子不是团队资源；专教接单的课未查到
55|X|A1|「feng shui tour」零结果（R1-B）
56|>K3|R|App 内一对多直播须走 IAP（R1-D）；作 K3 的学员社群
57|X|A1 A9|买家未见；开源排盘包免费（R1-F1-b）；可作 K2 的副产品
58|X|A9|开源 Kerykeion 免费（R1-F1-c）
59|X|A9 A2|泛预约工具开垂直页即可替代（R1-B）
60|X|B2|投流能力是空白（PLAN）
61|X|A1|买家未见（R1-B）；可作Yixuan另一条「方法论转 Skill」服务线，不属本项目（见 沉淀/160）
62|X|A1|只有 ⚠️ 证据；平台给顾问分成两说差 3 倍
63|X|A8 R|Tinder 自做合盘（✅）；Align / Struck / NUiT 均未做大（R1-F3）
64|X|B1 A10|团队无此初心；依赖个人、规模不经济
65|X|A1|调用量与收入未查到；可作 K2 的副产品
66|X|B1 A9|Starseed 不是团队的体系
67|X|A9 R|manifestation 词被媒体垄断（R1-F1-c）；4.3(b)
68|>K4|A8 B4|印度路径的平台部分 = 结束战斗型；「咨询顺势卖开运商品」这一招并入 K4
69|X|A1|需求量未查到；是入境游、不是出海
70|X|A1 R|reality shifting method 美区 10 次 / 月（R4-0）；心理健康风险
71|X|A4 B2|aura colors meaning 1,000 KD 29 可切，但只能靠广告；非团队专业
72|X|R A5|Meta 禁暗示个人属性的广告句式（R1-D）；upsell 退款风险
73|X|B2 R|泰语内容能力与泰国收款都卡（Stripe 泰国主体据称禁 psychic）
74|X|B3 R|咖啡杯占卜不是团队文化；阿语市场宗教合规风险最大（R1-F1-d）
75|X|B2|日语不是团队能力
76|X|B2 B5|日 / 法 / 西语顾问供给都没有
77|X|B2 A9|西占星图非团队专业；AI 星图在洗牌期
'''

NAMES = {}

# 死因代码 → 中文全名（出表时用全名，代码只在数据里当简写）
LABEL = {
    'A1': '需求不刚（不够疼、不愿花钱、频次低或潜在客户少）',
    'A2': '天花板低（市场太小，撑不起一定规模）',
    'A3': '方案不成立（产品力弱，没有足够差异化）',
    'A4': '单元模型不成立（单笔生意就不赚钱）',
    'A5': '持续性差（需求、渠道、行业变化太快，赚不了长钱）',
    'A6': '周期性差（季节或周期波动大）',
    'A7': '缺增长路径（找不到持续增长的驱动力）',
    'A8': '错过窗口（已同质化、已集中、头部已拿到融资）',
    'A9': '缺壁垒（别人很容易复制）',
    'A10': '规模不经济（太依赖人，做大反而更难）',
    'B1': '缺初心（团队没有支撑这件事的长期动力）',
    'B2': '缺关键能力（团队没有这门生意必需的能力，如语言、专业、投流）',
    'B3': '缺文化基因（团队文化和这门生意不匹配）',
    'B4': '缺起盘资金（需要的钱远超能拿出的）',
    'B5': '缺关键资源（缺必需的合作方、供给或渠道）',
    'R': '规则卡死（平台政策或法律直接禁止 / 严限）',
}
SHORT = {k: v.split('（')[0] for k, v in LABEL.items()}


def names(codes, full=False):
    return '；'.join((LABEL if full else SHORT)[c] for c in codes)


def load_names():
    path = __file__.replace('工具/subtract.py', '01-充分做加法-备选项池.md')
    for line in open(path, encoding='utf-8'):
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(c) >= 7 and re.fullmatch(r'\d+', c[0]) and 1 <= int(c[0]) <= 77:
            NAMES.setdefault(int(c[0]), c[1].replace('**', ''))


def rows():
    out = []
    for line in DATA.strip().splitlines():
        n, v, codes, why = line.split('|')
        out.append((int(n), v.strip(), codes.split(), why.strip()))
    return out


def check():
    load_names()
    R = rows()
    errs = []
    nums = [r[0] for r in R]
    if sorted(nums) != list(range(1, 78)):
        errs.append(f'编号不全或重复：缺 {sorted(set(range(1, 78)) - set(nums))}')
    valid = {f'A{i}' for i in range(1, 11)} | {f'B{i}' for i in range(1, 6)} | {'R'}
    for n, v, codes, why in R:
        if v not in ('X', *CANDIDATES, *[f'>{k}' for k in CANDIDATES]):
            errs.append(f'#{n} 结论写法不对：{v}')
        if v == 'X' and not codes:
            errs.append(f'#{n} 划掉了但没写死因代码')
        bad = [c for c in codes if c not in valid]
        if bad:
            errs.append(f'#{n} 未知代码 {bad}')
        if len(why) < 8:
            errs.append(f'#{n} 依据太短')
    for k in CANDIDATES:
        if not any(v == k for _, v, _, _ in R):
            errs.append(f'候选 {k} 没有主条目')
    for n in NAMES:
        pass
    print('❌ ' + '\n❌ '.join(errs) if errs else
          f'✅ 77 条齐全；候选 {sum(v in CANDIDATES for _, v, _, _ in R)} 个、并入 {sum(v.startswith(">") for _, v, _, _ in R)} 条、'
          f'划掉 {sum(v == "X" for _, v, _, _ in R)} 条，每条划掉的都有死因代码与依据')
    return not errs


def table():
    load_names()
    R = rows()
    from collections import Counter
    print('### 候选（主条目 + 并入的条目）\n')
    for k, desc in CANDIDATES.items():
        main = [r for r in R if r[1] == k]
        merged = [r for r in R if r[1] == '>' + k]
        print(f'**{k} · {desc}**\n')
        for n, v, codes, why in main:
            print(f'- 主条目 #{n} {NAMES.get(n, "")}：{why}')
        for n, v, codes, why in merged:
            print(f'- 并入 #{n} {NAMES.get(n, "")}（单独做的问题：{names(codes)}）：{why}')
        print()
    print('### 划掉的条目与死因\n')
    print('| # | 备选项 | 死因 | 依据 |\n| --- | --- | --- | --- |')
    for n, v, codes, why in R:
        if v == 'X':
            print(f'| {n} | {NAMES.get(n, "")} | {names(codes)} | {why} |')
    c = Counter(code for _, v, codes, _ in R if v == 'X' for code in codes)
    print('\n**死因分布（61 条划掉的条目里，每种死因出现几次；一条可以有多个死因）**：\n')
    print('| 死因 | 什么意思 | 出现次数 |\n| --- | --- | ---: |')
    for k, n in c.most_common():
        print(f'| {SHORT[k]} | {LABEL[k].split("（", 1)[1].rstrip("）") if "（" in LABEL[k] else ""} | {n} |')


# 给合伙人看的「可解决吗」判断（Yixuan 2026-11-08 要求）：按最卡人的那个死因定
SOLVABLE_RULES = [
    ({'R', 'A8'}, '不可解', '规则或窗口不在我们手里（平台 / 法律直接卡，或头部已拿到门票）'),
    ({'A1', 'A2'}, '不可解', '需求侧问题：没人要、或市场小到撑不起'),
    ({'A9', 'A4', 'A10', 'A5', 'A6', 'A3', 'A7'}, '难解', '结构性问题：无壁垒 / 单笔不赚钱 / 太依赖人 / 变化快'),
    ({'B1', 'B2', 'B3', 'B4', 'B5'}, '可解', '只是团队现在不具备：招人、合作或补能力能解决——但要先证明值得'),
]


def solvable(codes):
    cs = set(codes)
    for keys, verdict, why in SOLVABLE_RULES:
        if cs & keys:
            return verdict, why
    return '未判', ''


def partner_table():
    """给合伙人的失败清单：怎么失败的（依据）、为什么（死因）、可解决吗。"""
    load_names()
    R = rows()
    print('| # | 备选项 | 怎么失败的（证据） | 失败原因 | 可解决吗 |\n| --- | --- | --- | --- | --- |')
    from collections import Counter
    c = Counter()
    for n, v, codes, why in R:
        if v != 'X':
            continue
        verdict, _ = solvable(codes)
        c[verdict] += 1
        print(f'| {n} | {NAMES.get(n, "")} | {why} | {names(codes)} | **{verdict}** |')
    print('\n**可解决吗的分布**：' + '，'.join(f'{k} {v} 条' for k, v in c.most_common()))
    print('\n判断规则（按最卡人的那个死因定）：')
    for keys, verdict, why in SOLVABLE_RULES:
        print(f'- **{verdict}**：{why}')


if __name__ == '__main__':
    if '--check' in sys.argv:
        sys.exit(0 if check() else 1)
    if '--partner' in sys.argv:
        import io, contextlib, os
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import humanize
        humanize.load_opts()
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            partner_table()
        print(humanize.transform(buf.getvalue(), True), end='')
        sys.exit(0)
    # 出表前统一过 humanize：代号（K1、R1-B…）换成有语义的名字
    import io, contextlib, os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import humanize
    humanize.load_opts()
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        table()
    print(humanize.transform(buf.getvalue(), True), end='')
