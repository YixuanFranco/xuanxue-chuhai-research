#!/usr/bin/env python3
# 用法：python3 工具/check_evidence.py —— 校验 01 备选项池每行证据列非空、格式合规（R2 起每轮改完都跑）
"""R2 自检：数备选项表每一行的证据列是否非空、格式与长度是否合规。"""
import re, sys, pathlib
P = pathlib.Path(__file__).resolve().parent.parent / '01-充分做加法-备选项池.md'
text = P.read_text(encoding='utf-8')
# 只看第二节（备选项池）里的表
sec = text[text.index('## 二、备选项池'):text.index('## 三、')]
rows = {}
for ln in sec.split('\n'):
    m = re.match(r'^\|\s*(\d+)\s*\|', ln)   # Obsidian 会给表格补空格对齐，编号两边空格数不固定
    if m:
        cells = [c.strip() for c in ln.strip().strip('|').split('|')]
        rows[int(m.group(1))] = cells
# 来源 2026-11-05 起写语义名（如「方向全景调研」「东方命理查词」），不再是 R1-B 这类代号
SRCNAME = r'(?:规模与集中度调研|方向全景调研|中国团队案例调研|规则与风险调研|单位经济调研|西占塔罗查词|东方命理查词|新灵性与 AI 查词|多语种查词|查词调研|糊站验尸|Semrush 第一批数据)'
ENTRY = re.compile(r'^(▼)?(✅|🟡|⚠️|❓) .+（(查过：)?' + SRCNAME + r'[^（）]*(、' + SRCNAME + r'[^（）]*)*）$')
vis = lambda s: len(s.replace('️', ''))
empty, badfmt, toolong, ncol = [], [], [], []
for n, cells in sorted(rows.items()):
    if len(cells) != 7: ncol.append(n); continue
    ev = cells[-1]
    if not ev: empty.append(n); continue
    for e in ev.split('<br>'):
        if not ENTRY.match(e): badfmt.append((n, e))
        body = re.sub(r'（[^（）]*）\s*$', '', e)   # 末尾的来源括号不计（2026-11-05 来源改成语义名后变长）
        if vis(body) > 40: toolong.append((n, vis(body), e))
exp = set(range(1, 78))
print(f'表格行数: {len(rows)}（期望 77 = 64 + 13）；编号缺失: {sorted(exp - set(rows)) or "无"}；多余: {sorted(set(rows) - exp) or "无"}')
print(f'列数不是 7 的行: {ncol or "无"}')
print(f'证据列为空: {empty or "无"}  → 非空 {len(rows) - len(empty) - len(ncol)}/{len(rows)}')
print(f'条目格式不合规: {badfmt or "无"}')
print(f'单条 >40 字（含信度符号，不含末尾来源）: {toolong or "无"}')
cnt = [len(c[-1].split('<br>')) for c in rows.values()]
print(f'每格条数分布: 1条={cnt.count(1)} 2条={cnt.count(2)} 3条={cnt.count(3)} >3条={sum(x>3 for x in cnt)}')
sys.exit(1 if (empty or badfmt or toolong or ncol or exp - set(rows)) else 0)
