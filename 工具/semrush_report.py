#!/usr/bin/env python3
"""把 工具/semrush/*.csv 汇总成 Markdown 表（R4 用）。只读本地 CSV，不联网、不花单位。
用法：python3 工具/semrush_report.py > /tmp/x.md   （或 --section 空白 / 词族 / 多国）
判定规则（机械，写死在这里，改规则就改这里）：
  无需求 = 美区月搜索 < 50 或 Semrush 无数据；需求极小 = 50–199；
  强 = KD ≥ 60；可切 = KD ≤ 30 且月搜索 ≥ 500；其余 = 一般。KD 是 Semrush 的关键词难度估计（0–100）。
"""
import collections, csv, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, 'semrush')
POP = {'us': 335, 'uk': 68, 'ca': 40, 'au': 27, 'sg': 6, 'my': 34, 'hk': 7.5, 'ph': 115}   # 人口（百万，约数）


def num(x):
    try:
        return int(float(x))
    except (TypeError, ValueError):
        return 0


def load():
    kw = {r['keyword']: r for r in csv.DictReader(open(os.path.join(HERE, 'keywords.csv'), encoding='utf-8'))}
    ov = {(r['Ph'], r.get('database') or 'us'): r
          for r in csv.DictReader(open(os.path.join(D, 'overview.csv'), encoding='utf-8'))}
    sp = collections.defaultdict(list)
    p = os.path.join(D, 'serp.csv')
    if os.path.exists(p):
        for r in csv.DictReader(open(p, encoding='utf-8')):
            if r['Dn'] != '(无结果)':
                sp[r['query']].append(r['Dn'].replace('www.', ''))
    return kw, ov, sp


def verdict(nq, kd):
    if nq < 50:
        return '无需求'
    if nq < 200:
        return '需求极小'
    if kd >= 60:
        return '强'
    if kd <= 30 and nq >= 500:
        return '可切'
    return '一般'


def blanks(kw, ov, sp):
    print('| 词族 | 搜索词 | 美区月搜索 | KD | 新判定 | 前 5 名 |\n| --- | --- | ---: | ---: | --- | --- |')
    rows = []
    for k, r in kw.items():
        if r['verdict'] != '空白':
            continue
        o = ov.get((k, 'us'), {})
        nq, kd = num(o.get('Nq')), num(o.get('Kd'))
        rows.append((r['family'], -nq, k, nq, kd, verdict(nq, kd), ' · '.join(sp[k][:5]) or '（无结果）'))
    for f, _, k, nq, kd, v, top in sorted(rows):
        print(f'| {f} | {k} | {nq:,} | {kd} | **{v}** | {top} |')
    c = collections.Counter(x[5] for x in rows)
    print(f'\n合计 {len(rows)} 个原「空白」词：' + '，'.join(f'{k} {v}' for k, v in c.most_common()))


def families(kw, ov):
    print('| 词族 | 词数 | 美区月搜索合计 | 0 量词数 | 最大的 3 个词 |\n| --- | ---: | ---: | ---: | --- |')
    fam = collections.defaultdict(list)
    for k, r in kw.items():
        fam[r['family']].append((num(ov.get((k, 'us'), {}).get('Nq')), k))
    for f, L in sorted(fam.items(), key=lambda x: -sum(n for n, _ in x[1])):
        L.sort(reverse=True)
        print(f'| {f} | {len(L)} | {sum(n for n, _ in L):,} | {sum(1 for n, _ in L if n == 0)} | '
              + '；'.join(f'{k} {n:,}' for n, k in L[:3]) + ' |')


def intl(ov):
    p = os.path.join(HERE, 'keywords_intl.csv')
    if not os.path.exists(p):
        return
    words, dbs = [], []
    for r in csv.DictReader(open(p, encoding='utf-8')):
        if r['keyword'] not in words:
            words.append(r['keyword'])
        if r['database'] not in dbs:
            dbs.append(r['database'])
    print('| 搜索词 | ' + ' | '.join(dbs) + ' | 合计 | 新+马 每百万人 | 美 每百万人 |')
    print('| --- |' + ' ---: |' * (len(dbs) + 3))
    for w in words:
        v = [num(ov.get((w, d), {}).get('Nq')) for d in dbs]
        m = dict(zip(dbs, v))
        semy = (m.get('sg', 0) + m.get('my', 0)) / (POP['sg'] + POP['my'])
        us = m.get('us', 0) / POP['us']
        print(f'| {w} | ' + ' | '.join(f'{x:,}' for x in v) + f' | {sum(v):,} | {semy:,.0f} | {us:,.0f} |')
    print('\n人口为约数（百万）：' + '、'.join(f'{k} {v}' for k, v in POP.items() if k in dbs) + '。')


# 自然搜索点击率曲线（第 1–10 位）。行业常用的近似值，是假设，不是 Semrush 数据——改这里就改全部 CRn。
CTR = [0.28, 0.15, 0.11, 0.08, 0.07, 0.05, 0.04, 0.03, 0.03, 0.025]
UGC = {'youtube.com', 'reddit.com', 'pinterest.com', 'quora.com', 'facebook.com', 'en.wikipedia.org', 'tiktok.com',
       'instagram.com', 'apps.apple.com', 'play.google.com', 'medium.com', 'scribd.com', 'tumblr.com', 'm.youtube.com'}


def basket_shares(ov, words_dbs):
    """一篮子词（相关市场的搜索侧代理）里，每个站分到的估计点击。"""
    serp = collections.defaultdict(list)
    for r in csv.DictReader(open(os.path.join(D, 'serp.csv'), encoding='utf-8')):
        if r['Dn'] != '(无结果)':
            serp[(r['query'], r.get('database') or 'us')].append((num(r['rank']), r['Dn'].replace('www.', '')))
    clicks, total, covered = collections.Counter(), 0, 0
    for w, db in words_dbs:
        nq = num(ov.get((w, db), {}).get('Nq'))
        rows = sorted(serp.get((w, db), []))
        if not rows:
            continue
        covered += 1
        for rank, dn in rows[:10]:
            if 1 <= rank <= 10:
                c = nq * CTR[rank - 1]
                clicks[dn] += c
                total += c
    return clicks, total, covered


def crn(ov):
    baskets = collections.OrderedDict()
    for f, path in (('篮子', 'keywords_basket.csv'), ('新马', 'keywords_semy.csv')):
        p = os.path.join(HERE, path)
        if not os.path.exists(p):
            continue
        for r in csv.DictReader(open(p, encoding='utf-8')):
            name = f"{r['family']} · {r['database']}"
            baskets.setdefault(name, []).append((r['keyword'], r['database']))
    print('| 相关市场（搜索侧代理） | 词数 | 估计月点击 | CR1 | CR3 | CR5 | CR10 | CR5（去掉 YouTube / Reddit 等平台） | 前 5 名 |')
    print('| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |')
    for name, wd in baskets.items():
        clicks, total, covered = basket_shares(ov, wd)
        if not total:
            continue
        top = clicks.most_common()
        cr = lambda n, L: sum(c for _, c in L[:n]) / total * 100
        site = [(d, c) for d, c in top if d not in UGC]
        print(f'| {name} | {covered} | {total:,.0f} | {cr(1, top):.0f}% | {cr(3, top):.0f}% | {cr(5, top):.0f}% | '
              f'{cr(10, top):.0f}% | {cr(5, site):.0f}% | ' + ' · '.join(f'{d} {c / total * 100:.0f}%' for d, c in top[:5]) + ' |')
    print('\n点击率曲线（假设）：第 1–10 位 = ' + ' / '.join(f'{x:.0%}' for x in CTR) + '。分母 = 篮子里所有词前 10 位的估计点击之和。')


if __name__ == '__main__':
    kw, ov, sp = load()
    sec = sys.argv[sys.argv.index('--section') + 1] if '--section' in sys.argv else 'all'
    if sec in ('all', '空白'):
        print('### 原「空白」词复核\n'); blanks(kw, ov, sp); print()
    if sec in ('all', '词族'):
        print('### 三个词族的美区需求\n'); families(kw, ov); print()
    if sec in ('all', '多国'):
        print('### 东方命理核心词 · 8 个英语市场\n'); intl(ov); print()
    if sec in ('all', 'crn'):
        print('### 搜索侧集中度（按词篮子估计点击份额）\n'); crn(ov); print()
