#!/usr/bin/env python3
"""从 R1-F1 查词文件里抽出关键词，生成 工具/keywords.csv（Semrush 批量查询用）。
列：keyword, family, database, verdict（强/一般/空白/未判定）
用法：python3 工具/extract_keywords.py
"""
import csv, os, re, glob
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FAMILY = {'a': '西占塔罗通灵', 'b': '东方命理', 'c': '新灵性与AI'}
rows, seen = [], set()
for path in sorted(glob.glob(os.path.join(ROOT, 'R1-F1-[abc]-*.md'))):
    fam = FAMILY[os.path.basename(path)[6]]
    for line in open(path, encoding='utf-8'):
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 5 or not re.fullmatch(r'\d+', cells[0]):
            continue
        kw = re.sub(r'[（(].*?[）)]', '', cells[1]).replace('*', '').strip()
        kw = kw.split('/')[0].strip()
        if not kw or re.search(r'[一-鿿\[\]]', kw):   # 跳过中文说明和 [星座] 这类模板
            continue
        if re.search(r'\.(com|co|io|net|org|uk)\b', kw) or kw in ('Fiverr', 'Gumroad', 'Etsy'):
            continue   # 核心玩家表里的域名不是关键词
        # 先只看判定列（a/b/c 三个文件都是第 5 列），判定列里没有判定词才扫 3 列。
        # 理由列里常有「不是空白」这类字样，旧逻辑直接扫 3 列，会把「一般」误抽成「空白」（2026-11-02 普查出 3 行）。
        # 优先级不变（空白>一般>强），所以「一般偏空白」「强/空白（独立站）」照旧算空白。
        order = ('空白', '一般', '强', '未')
        verdict = next((v for v in order if v in cells[4]), None) or \
            next((v for v in order if any(v in c for c in cells[3:6])), '未判定')
        key = kw.lower()
        if key in seen:
            continue
        seen.add(key)
        rows.append({'keyword': kw, 'family': fam, 'database': 'us',
                     'verdict': {'未': '未判定'}.get(verdict, verdict)})
out = os.path.join(HERE, 'keywords.csv')
with open(out, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['keyword', 'family', 'database', 'verdict'])
    w.writeheader(); w.writerows(rows)
from collections import Counter
print(f'{len(rows)} 个词 → {out}')
print(Counter(r['family'] for r in rows), Counter(r['verdict'] for r in rows))
