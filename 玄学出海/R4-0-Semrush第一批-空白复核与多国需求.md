---
title: "玄学出海 · Semrush 第一批数据：Semrush 第一批——「空白」复核与东方命理多国需求"
date: 2026-11-05
status: v0 —— R4 的数据前置；表格由 `工具/semrush_report.py` 从 `工具/semrush/*.csv` 生成，可重跑
method: Semrush MCP（phrase_this 搜索量 + KD；phrase_organic 谷歌前 10）；判定规则写在 semrush_report.py 头部
permission_scope: 公开
---

# Semrush 第一批数据 · Semrush 第一批：「空白」复核 + 东方命理多国需求

> **花了多少**：本批约 5,000 单位（脚本按最坏单价记账，实际更少；查无结果的词每个记 50）。试用额度 50,000。
> **信度**：Semrush 的搜索量是**模型估计**，不是谷歌官方数，但同一口径下**互相比较**是可靠的（🟡→ 相对比较可当 ✅ 用）。KD（关键词难度 0–100）也是 Semrush 估计。
> **这一批回答 R3 留下的一个关键问号**：东方命理英文市场「是还没人做，还是需求本来就小」？

## 一、三句话结论

1. **R1 查词里的「空白」，大多数是「没人搜」，不是「没人做」。** 37 个原「空白」词里，14 个无需求（美区月搜索 <50 或无数据）、5 个需求极小（50–199）；东方命理的 14 个「空白」里，**紫微排盘、用神、大运、奇门、九星、五行计算器全部是 0–30 次 / 月**。真正「有量又好切」的只有 4 个（KD ≤ 30 且 ≥500 次）。
2. **东方命理在美国是西占的 1/16。** 美区月搜索合计：西占塔罗约 300 万、新灵性约 104 万、东方命理约 19 万——而东方这 19 万里一半是泛词 feng shui（9 万）。八字本体（bazi + bazi calculator + bazi reading）在美区只有约 7,200 次 / 月。
3. **但东方命理的需求集中在东南亚华人。** bazi calculator：新加坡 3,600、马来西亚 3,600、菲律宾 1,900，美国 5,400——按人口折算，**新马每百万人 180 次，美国 16 次，差 11 倍**；紫微斗数新加坡（1,000）比美国（390）还多。对照组 tarot reading 新马每百万人 80、美国 99，差不多——说明这不是新马「本来就爱搜玄学」，是**八字 / 紫微特有的华人需求**。

> 对 R3 的修正：R3 判断点 ④ 写东方命理英文「极早期，或需求本身小——分不清」。现在可以分清了：**在欧美英语市场是需求本身小；在东南亚华人英语市场，需求是真的、而且密度高。** 「英语」不是一个相关市场的好边界——「人群」才是（R4 切相关市场时用）。

## 二、三个词族的美区需求

| 词族 | 词数 | 美区月搜索合计 | 0 量词数 | 最大的 3 个词 |
| --- | ---: | ---: | ---: | --- |
| 西占塔罗通灵 | 41 | 2,997,970 | 1 | horoscope 1,500,000；daily horoscope 673,000；111 angel number meaning 165,000 |
| 新灵性与AI | 55 | 1,038,770 | 15 | numerology 550,000；moon phase today 368,000；human design chart 27,100 |
| 东方命理 | 53 | 189,380 | 10 | feng shui 90,500；i ching 22,200；chinese zodiac 2026 22,200 |


## 三、东方命理核心词 · 8 个英语市场（月搜索）

| 搜索词 | us | uk | ca | au | sg | my | hk | ph | 合计 | 新+马 每百万人 | 美 每百万人 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| bazi | 1,600 | 480 | 390 | 480 | 1,900 | 1,300 | 590 | 480 | 7,220 | 80 | 5 |
| bazi calculator | 5,400 | 720 | 880 | 1,000 | 3,600 | 3,600 | 210 | 1,900 | 17,310 | 180 | 16 |
| bazi reading | 210 | 40 | 40 | 70 | 590 | 170 | 20 | 140 | 1,280 | 19 | 1 |
| four pillars of destiny | 480 | 50 | 110 | 70 | 30 | 30 | 30 | 170 | 970 | 2 | 1 |
| chinese astrology | 9,900 | 1,300 | 1,300 | 1,000 | 390 | 260 | 20 | 390 | 14,560 | 16 | 30 |
| chinese zodiac 2026 | 22,200 | 2,900 | 3,600 | 2,900 | 2,400 | 1,600 | 0 | 2,900 | 38,500 | 100 | 66 |
| zi wei dou shu | 390 | 50 | 110 | 110 | 1,000 | 590 | 110 | 20 | 2,380 | 40 | 1 |
| feng shui | 90,500 | 18,100 | 12,100 | 9,900 | 3,600 | 4,400 | 1,900 | 22,200 | 162,700 | 200 | 270 |
| feng shui consultant | 1,300 | 140 | 140 | 140 | 260 | 260 | 20 | 210 | 2,470 | 13 | 4 |
| i ching | 22,200 | 5,400 | 3,600 | 2,400 | 1,000 | 720 | 480 | 880 | 36,680 | 43 | 66 |
| kua number calculator | 590 | 140 | 170 | 140 | 170 | 210 | 20 | 260 | 1,700 | 10 | 2 |
| chinese birth chart | 9,900 | 1,600 | 1,000 | 1,300 | 30 | 0 | 30 | 720 | 14,580 | 1 | 30 |
| chinese horoscope today | 2,400 | 1,000 | 720 | 320 | 20 | 720 | 30 | 480 | 5,690 | 18 | 7 |
| tarot reading | 33,100 | 9,900 | 3,600 | 5,400 | 1,900 | 1,300 | 590 | 8,100 | 63,890 | 80 | 99 |

人口为约数（百万）：us 335、uk 68、ca 40、au 27、sg 6、my 34、hk 7.5、ph 115。


**怎么读**：
- 「新+马 每百万人」vs「美 每百万人」是**需求密度**。八字类词差 10 倍以上，风水 / 易经 / 生肖这类「泛文化词」反而美国更高——泛文化词的人群是「对东方文化好奇的西方人」，八字类词的人群是「华人」。这两类人要分开算市场。
- **chinese birth chart（美区 9,900）不是八字需求**：前排是 thebump、whattoexpect（母婴站），搜的是「清宫图生男生女」。别被这个数骗了。

## 四、原「空白」词复核（37 个）

| 词族 | 搜索词 | 美区月搜索 | KD | 新判定 | 前 5 名 |
| --- | --- | ---: | ---: | --- | --- |
| 东方命理 | chinese birth chart | 9,900 | 70 | **强** | thebump.com · whattoexpect.com · bendigojosshouse.com · travelchinaguide.com · pinterest.com |
| 东方命理 | chinese horoscope today | 2,400 | 47 | **一般** | asiaone.com · horoscope.com · astrology.com · timesofindia.indiatimes.com · astrologizeme.com |
| 东方命理 | bagua map feng shui | 590 | 25 | **可切** | fengshuimanhattan.com · reddit.com · youtube.com · mindfuldesignconsulting.com · ifsguild.org |
| 东方命理 | kua number calculator | 590 | 20 | **可切** | wofs.com · squaredawayfengshui.com · wehomzfurn.com · prokerala.com · youtube.com |
| 东方命理 | chinese gender predictor calendar | 390 | 50 | **一般** | rforrabbit.com · baby-chick.com · thebump.com · fairhavenhealth.com · whattoexpect.com |
| 东方命理 | chinese numerology calculator | 110 | 41 | **需求极小** | tsemrinpoche.com · loshugridcalculators.com · occultscience.in · astrologyfutureeye.com · pinterest.com |
| 东方命理 | purple star astrology | 110 | 12 | **需求极小** | purplestarchart.com · en.wikipedia.org · zwds-calculator.com · fatemaster.ai · tumblr.com |
| 东方命理 | bazi compatibility calculator | 70 | 8 | **需求极小** | xuanseal.com · shen-shu.com · yourchineseastrology.com · fatemaster.ai · baziinsight.com |
| 东方命理 | qi men dun jia chart | 30 | 0 | **无需求** | （无结果） |
| 东方命理 | zi wei dou shu chart calculator | 30 | 0 | **无需求** | （无结果） |
| 东方命理 | bazi useful god | 20 | 0 | **无需求** | （无结果） |
| 东方命理 | five elements calculator | 20 | 0 | **无需求** | （无结果） |
| 东方命理 | bazi luck pillars | 0 | 0 | **无需求** | （无结果） |
| 东方命理 | kyusei kigaku | 0 | 0 | **无需求** | （无结果） |
| 新灵性与AI | astrocartography calculator | 1,300 | 32 | **一般** | horoscopes.astro-seek.com · astrocartography.asknovaastrology.com · astro.com · reddit.com · astrocarto.net |
| 新灵性与AI | aura colors meaning | 1,000 | 29 | **可切** | auratheory.com · healthline.com · instagram.com · reddit.com · ascendgetlifted.com |
| 新灵性与AI | gene keys calculator | 390 | 19 | **一般** | genekeys.com · genekeys.com · home.genekeys.com · geneticmatrix.com · driftinward.com |
| 新灵性与AI | astrocartography map free | 260 | 38 | **一般** | astrocartography.asknovaastrology.com · astrocarto.org · astro.com · reddit.com · astrocarto.net |
| 新灵性与AI | what starseed am i calculator | 20 | 0 | **无需求** | （无结果） |
| 新灵性与AI | reality shifting method | 10 | 0 | **无需求** | （无结果） |
| 新灵性与AI | AI feng shui floor plan | 0 | 0 | **无需求** | （无结果） |
| 新灵性与AI | AI human design reading | 0 | 0 | **无需求** | （无结果） |
| 新灵性与AI | AI numerology reading | 0 | 0 | **无需求** | （无结果） |
| 新灵性与AI | horoscope API daily JSON | 0 | 0 | **无需求** | （无结果） |
| 新灵性与AI | personalized astrology report birth chart reading | 0 | 0 | **无需求** | （无结果） |
| 新灵性与AI | starseed signs quiz | 0 | 0 | **无需求** | （无结果） |
| 西占塔罗通灵 | yes or no tarot | 74,000 | 61 | **强** | reddit.com · anytimeastro.com · quora.com · youtube.com · forum.becomealivinggod.com |
| 西占塔罗通灵 | synastry chart | 12,100 | 57 | **一般** | horoscopes.astro-seek.com · astro-charts.com · reddit.com · synastrychart.org · astrotheme.com |
| 西占塔罗通灵 | saturn return calculator | 9,900 | 20 | **可切** | apps.apple.com · astrochart.co · driftinward.com · reddit.com · vedicrishi.in |
| 西占塔罗通灵 | venus sign calculator | 3,600 | 35 | **一般** | birthchart.net · cafeastrology.com · astrostyle.com · zodiscope.io · prokerala.com |
| 西占塔罗通灵 | north node calculator | 2,900 | 33 | **一般** | cafeastrology.com · nextastrology.com · saturnandhoney.com · birthchartstore.com · astrostyle.com |
| 西占塔罗通灵 | transit chart calculator | 1,900 | 38 | **一般** | horoscopes.astro-seek.com · asknovaastrology.com · astro-charts.com · appliedjyotish.com · prokerala.com |
| 西占塔罗通灵 | daily tarot card | 1,600 | 43 | **一般** | dailytarotdraw.com · labyrinthos.co · tarot.com · nostra-tarot.com · free-tarot-reading.net |
| 西占塔罗通灵 | love tarot reading | 1,600 | 40 | **一般** | free-tarot-reading.net · labyrinthos.co · youtube.com · evatarot.net · deckaura.com |
| 西占塔罗通灵 | tarot spreads for beginners | 390 | 32 | **一般** | reddit.com · suburbanwitchery.com · emeraldlotusdivination.com · forum.thetarot.guru · ethony.com |
| 西占塔罗通灵 | does he love me tarot | 90 | 29 | **需求极小** | tarostarot.com · tellmytarot.com · tarot-7.com · divinimagic.com · tarotap.com |
| 西占塔罗通灵 | synastry compatibility calculator | 50 | 48 | **需求极小** | horoscopes.astro-seek.com · asknovaastrology.com · astrolibrary.org · reddit.com · theinnerwheel.com |

合计 37 个原「空白」词：无需求 14，一般 12，需求极小 5，可切 4，强 2


**复核后真正「有量 + 可切」的 4 个**（KD ≤ 30 且 ≥500 次 / 月，美区）：

| 词 | 月搜索 | KD | 为什么可切（看前 10） |
| --- | ---: | ---: | --- |
| saturn return calculator | 9,900 | 20 | 前排是 App Store 页、Reddit、小站，**没有一个好用的网页工具压住** |
| aura colors meaning | 1,000 | 29 | 前排是 healthline、vogue 的文章 + Instagram，**是内容词不是工具词** |
| kua number calculator | 590 | 20 | 前排是风水小站，工具粗糙 |
| bagua map feng shui | 590 | 25 | 前排是风水顾问个人站 + Reddit + YouTube |

**原「空白」被推翻成「强」的 2 个**：yes or no tarot（74,000，KD 61，前排是 Reddit / Quora 论坛——流量大但被论坛占着，难切）、chinese birth chart（见上，母婴需求）。

## 五、这一批对 R4 / R5 的意义（只是输入）

- **R4 相关市场**：「东方命理 · 英语」要拆成两个：**东南亚华人（新马菲港）× 八字 / 紫微**——需求密度高、对手是 masterseanchan（新加坡）这一类；**欧美西方人 × 风水 / 易经 / 生肖**——量大但是泛文化好奇，付费意愿未知。
- **R5 减法**：#49「英文八字 / 紫微在线排盘工具站」（英文八字 / 紫微排盘工具站）在美区的「空白」不成立——是没量；在新马成立的可能性要用新马库的 SERP 再看一次（下一批）。#17 AI 风水、#57 东方命理 API 相关词美区全是 0。
- **Yixuan的资源对照**（推断）：东南亚华人英语市场 = 中文 / 英文双语、文化同源、可能能用上中文内容母本——比欧美更接近Yixuan已有的能力。但新马市场**小**（新马合计约 4,000 万人），天花板要在 R4 算。

## 六、下一批 Semrush（R4 正文用，预计约 2 万单位）

1. 新马库（sg / my）的八字类词前 10 → 看那边谁在排名、强不强。
2. 12 个核心对手站的排名词（domains）→ 算 SEO 流量份额，作为「搜索渠道里的 CRn」。
3. 10 个种子词的相关词（related）→ 补我们漏掉的词。

## 来源

`工具/semrush/overview.csv`（149 + 112 行）、`工具/semrush/serp.csv`（37 个词前 10）；Semrush MCP，2026-11-05 拉取，database = us / uk / ca / au / sg / my / hk / ph。人口为约数。
