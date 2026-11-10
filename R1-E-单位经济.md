---
title: "玄学出海 · 单位经济调研：单位经济（每种商业模式的钱怎么算）"
date: 2026-11-02
status: v0 —— 案头摘要级；14 次 WebSearch（额度共用，主动收手），WebFetch 未用；大量数字来自第三方博客 / 计算器站，缺口见文末
permission_scope: 公开
---

# 单位经济调研 · 单位经济

> **一句话摘要**：七种模式里，**平台规则类参数查得最实**（Etsy 费率、TikTok 礼物约五五分、LLM 单价），**漏斗类参数查得最虚**（占星 App 的 CPI、web2app 转化、留存、LTV 没有一个查到占星 / 生活方式分类的可靠数），**分成类参数靠估**（psychic 平台给顾问的分成没有任何一家官方披露）。本文件只摆参数，不算结论。

**信度**：✅ 官方 / 多源一致 · 🟡 单一来源或第三方估算 · ⚠️ 自述（卖家、课程、博主、affiliate 软文、计算器 SEO 站）。
**方法说明**：本轮 14 次 WebSearch，全部为搜索摘要，未打开原文核对；部分数字复用了同目录 `R1-F1-c`、`R1-F3`、`R1-F1-b` 已查到的结果（标注「转引」）。

---

## 1. Web2App 订阅漏斗（占星 / 塔罗 App）

| 指标 | 数字 | 出处（年份） | 信度 |
| --- | --- | --- | --- |
| 下载 → 付费（35 天内），全品类中位数 | 1.9%；头部 8.5% | 第三方转述 RevenueCat SOSA 2025（[RevenueCat 报告页](https://revenuecat.com/state-of-subscription-apps-2025)，原页只有预览，数字来自摘要，未在一手页核到） | 🟡 |
| 试用 → 付费，按试用长度 | ≥17 天试用中位 42.5%；≤4 天试用中位 25.5% | RevenueCat 2026 benchmarks（[链接](https://www.revenuecat.com/blog/growth/subscription-app-trends-benchmarks-2026.md)，2026） | 🟡 |
| 试用 → 付费，按付费墙类型（D35） | 硬付费墙 10.7%（2025 年为 12.1%）；freemium 2.1% | 同上（2026） | 🟡 |
| 试用 → 付费，最高品类 | Travel 48.7%、Media & Entertainment 43.8%；**Lifestyle 未见** | [i-programmer 转述 SOSA 2025](https://www.i-programmer.info/news/83-mobilephone/17938-making-money-from-subscription-apps.html)（2025） | 🟡 |
| Web2App 漏斗转化 vs iOS 应用内 | Web2App 1.10% vs iOS 应用内 1.60%（口径未说明） | 第三方转述 Adapty（[stormy.ai](https://stormy.ai/blog/mobile-app-revenue-benchmarks-paywall-optimization)，2026） | ⚠️ |
| 硬付费墙 vs 软付费墙 | 硬墙 LTV 高 21%；软墙原始转化高 50% | 同上（转述 Adapty） | ⚠️ |
| iOS 退款率 | 8.3%（全品类，未分类） | 同上（转述 Adapty） | ⚠️ |
| Web2App 试用价 / 续费价 | 17 个 Web2App 漏斗：试用价中位 $41.99；续费价 ÷ 首期价 = 4.5 倍（非占星专属） | [Consumer App Index](https://cai-breakdowns.pages.dev/web2app-paywalls-2026)（2026） | ⚠️ |
| Nebula 的试读 → 扣费结构 | $0.50 / $1 试读或 3 天试用 → $42–49.99 订阅扣费（用户投诉描述） | 转引 `R1-F3` 案例 13（Trustpilot / sikayetvar，2025–2026） | ⚠️ |
| Nebula 体量 | ARR 约 $50M；按分钟咨询约 $1/分钟 | 转引 `R1-F3`（[The Next Web](https://thenextweb.com/news/ukrainian-startup-astrology-app-nebula-thriving-despite-war)）、`R1-F1-c` | 🟡 |
| 订阅价格样本 | CHANI $11.99/月；Hint $29.99/月；Sanctuary $19.99/月（含 15 分钟真人文字解读）；AI 梦境 App $9.99/月 | 转引 `R1-F3`、`R1-F1-c`（2019–2026） | 🟡 |
| 东方命理 AI 报告价 | XuanSeal $19.99 起 / $39.99 单份 / $99/年；SajuAI $7.99；Fiverr / Gumroad 八字 $28–50 | 转引 `R1-F1-b`（2026） | 🟡 |
| 单个 AI 塔罗 App 天花板 | Flippa 挂牌月利 $2.4k–3.3k；appgoblin 多数 <$1 万/月 | 转引 `R1-F1-c` | ⚠️ / 🟡 |
| **CPI（占星 / 美国）** | **未查到**。只有泛品类：「$1–5 算有效」、2016 年口径 $0.25–100 | [wask.co](https://wask.co/facebook-advertising-costs/cpi-cost-per-install)、[consumeracquisition 2016](https://consumeracquisition.com/2016/05) | ⚠️（不可作占星参数） |
| 留存、LTV（占星分类） | **未查到** | Adapty 有 Lifestyle 基准文章，摘要没给数 | — |

**收入公式骨架**：
`月收入 = 投放预算 ÷ CPA（单个 quiz 完成或安装成本）× 付费墙转化（Web2App 约 1.1% ⚠️ / 硬墙 D35 试用转付费 10.7% 🟡）× [试用价 + 续费价（约 4.5× 首期 ⚠️）× 续费月数] × (1 − 退款率 8.3% ⚠️ − 拒付)`；CPA、留存曲线、占星分类 LTV 均未查到。

---

## 2. psychic 分钟计费平台

| 指标 | 数字 | 出处（年份） | 信度 |
| --- | --- | --- | --- |
| Keen 价格 | 约 $1.99/分钟起，头部顾问 $20–30+/分钟 | [bestonlinepsychicreading 对比页](https://bestonlinepsychicreading.pages.dev/compare/keen-vs-kasamba)（2026） | ⚠️（affiliate 站） |
| Kasamba 价格 | $1.99–16.50/分钟（另一来源 $2–30+） | [Outlook India](https://www.outlookindia.com/outlook-spotlight/free-psychic-reading-sites-news-304286)（2023）、[jpost 推广文](https://m.jpost.com/promocontent/100-percent-free-psychic-readings-online-by-phone-chat-or-live-video-644841) | ⚠️ |
| Psychic Source 价格 | $4.99–15.99/分钟常规；自称「低至 $0.60/分钟」（新客） | 搜索摘要 review 站；转引 `R1-F1-a` | ⚠️ |
| California Psychics 价格 | $5–23/分钟；推广文称「$1/分钟起」（新客价） | [newswire 软文](https://www.newswire.com/news/california-psychics-review-2025-most-trusted-online-psychic-readings-22650468)（2025） | ⚠️ |
| 平台给顾问的分成 | **无一家官方披露**。行业文章称「读者佣金 >61%」（未点名平台）；一家通灵生意转让挂牌称平台毛利 73–78%（即顾问拿约 22–27%） | [issuu Psychic Lifestyles 2024](https://issuu.com/psychiclifestyles/docs/plifestylesfall2024a/s/56319536)、[websiteclosers 挂牌](https://www.websiteclosers.com/businesses/10-year-internet-business-in-the-field-of-online-entertainment-psychic-readings-17-000-active-users-95-repeat-customer-rate-230-psychics-in-network/97537) | ⚠️（两说相差很大） |
| 同一挂牌的其他自述 | 17,000 活跃用户、复购率 95%、网络中 230 名通灵师、经营 10 年 | 同上 websiteclosers | ⚠️（卖方自述） |
| Astrotalk 抽成 | 未官方披露；第三方估 20–25% / 30–40% / 30–50% | [miracuves](https://miracuves.com/blog/business-model-of-astrotalk/)（2026）等 | ⚠️ |
| Astrotalk 每分钟价 | ₹10–200/分钟；新人 ₹5–15、成熟 ₹30–100+ | 同上 | ⚠️ |
| Astrotalk 体量 | FY25 收入 ₹1,214 crore（+85%）；FY26 利润 ₹222 crore（10 倍）、收入 +55%；15,000+ 活跃占星师（公司自述） | 转引 `R1-F1-c`（[Outlook Business](https://www.outlookbusiness.com/start-up/news/astrotalk-reports-85-revenue-growth-in-fy25-as-tier-i-cities-boost-platform-activity)）；[Inc42 FY26](https://inc42.com/buzz/astrotalks-fy26-profit-jumps-10x-to-₹222-cr-revenue-zooms-55-yoy/) | ✅（收入，注册处文件）/ ⚠️（人数） |
| 获客侧：affiliate 每新客 | Keen 约 $100/新订户（30 天 cookie）；Kasamba $100–125/新订户（另有 10% 分成一说） | [UpPromote](https://uppromote.com/blog/psychic-and-astrology-affiliate-programs)、[referly](https://www.referly.so/affiliate-programs/kasamba)（2025–2026） | 🟡（数字互相矛盾） |

**收入公式骨架**：
`平台毛利 = 付费用户数 × 每人月均通话分钟 × 每分钟价（$1.99–20+ ⚠️）× 平台抽成（20–78%，未定 ⚠️）− 新客首单补贴（$1/分钟、免费 3 分钟等）− 获客成本（affiliate CPA 约 $100–125 🟡）`；顾问侧 `顾问收入 = 分钟数 × 每分钟价 × (1 − 抽成)`。每人月均分钟数、复购周期未查到。

---

## 3. TikTok 直播打赏

| 指标 | 数字 | 出处（年份） | 信度 |
| --- | --- | --- | --- |
| 钻石兑现 | 约 $0.005/钻石（200 钻石 = $1）；也有站写 $0.025 或 $0.05（视为错） | [tik.tools](https://tik.tools/tiktok-diamonds-calculator)、[ttcalculator](https://ttcalculator.net/learn/tiktok-gifts/)（2026） | 🟡（多站一致，非官方） |
| 平台 / 主播分成 | 主播约得礼物金币价值的 50%（100 金币约 $1.06 → 主播约 $0.53）；TikTok 官方只说钻石「按受欢迎程度发放」 | 同上 | 🟡 |
| 提现门槛 | 10,000 钻石（$50）或约 $100，因地区而异 | 同上 | ⚠️ |
| 主播月收入（泛品类） | 1K–10K 粉：$50–600/月；10K–100K：$240–2,400/月；100K+：$5k–20k+/月 vs 「5 万粉以上多数 <$500/月」——两说矛盾 | [fluxnote](https://fluxnote.io/guides/tiktok-live-gifts-earnings-usa)、[joinotto](https://joinotto.com/blog/tiktok-gifts-value/)（2026） | ⚠️ |
| 塔罗主播专属数据 | **未查到**（仅一个西语塔罗号在 tik.tools 显示 0 钻石，无参考价值） | [tik.tools 账号页](https://tik.tools/creator/tarotenvivoconlilith) | — |
| 若有公会 / MCN | 公会再分成比例 **未查到** | — | — |

**收入公式骨架**：
`主播打赏收入 = 场次 × 场均在线 × 送礼率 × 人均送礼金币 × $0.0106/金币 × 50%（🟡）− 公会分成（未查到）`；加导流：`+ 导流到付费解读的人数 × 解读客单`（转化率未查到）。

---

## 4. Etsy 解读 / 星盘海报

| 指标 | 数字 | 出处（年份） | 信度 |
| --- | --- | --- | --- |
| 上架费 | $0.20 / 件，4 个月续一次，或售出时续 | [Craftybase](https://app.craftybase.com/blog/the-complete-guide-to-etsy-fees)、[eRank](https://help.erank.com/blog/beginners-guide-to-etsy-fees/)（2025–2026） | ✅（多源一致；未读 Etsy 官方页） |
| 交易费 | 6.5%（商品 + 运费 + 礼品包装；是否含销售税各说不一） | 同上 | ✅ |
| 支付处理费（美国） | 3% + $0.25（英国 4% + £0.20，另有监管费） | 同上 | ✅ |
| Offsite Ads | 归因订单收 15%（年销 <$1 万的店强制）；年销 ≥$1 万可选、费率 12% | 同上 | 🟡 |
| 不投站外广告的总费率 | 约 10–15%（低价商品更高）；被站外广告归因的单可到 25%+ | [checkoutpage](https://checkoutpage.com/blog/etsy-fees)（2026） | 🟡 |
| 塔罗解读客单 | same-day / same-hour 单问题 $2–7；视频解读 $13–50+ | 转引 `R1-F1-c` #47（etsy listing、findniche） | 🟡 |
| 星盘 / 个性化报告客单 | 几美元到 $99 | 转引 `R1-F1-c` #46 | 🟡 |
| 星盘海报（实物 / 数字）客单 | **未查到** | — | — |

**按费率规则算的示例**（纯算术，不是结论）：$5 的塔罗解读：$0.20 + 6.5%（$0.33）+ 3% + $0.25（$0.40）≈ $0.93，即约 19%；若被站外广告归因再 + $0.75，合计约 34%。$10 的单：约 $1.40（14%），被归因合计约 $2.90（29%）。

**收入公式骨架**：
`净收入 = 订单数 × 客单（$2–99 🟡）× (1 − 6.5% − 3%) − 订单数 × ($0.25 + $0.20) − 被站外广告归因订单 × 客单 × 15% − 交付成本（真人时间或 AI 成本）`；Etsy 站内流量转化率、复购率未查到。

---

## 5. 实物：水晶手串、塔罗牌

| 指标                   | 数字                                                                           | 出处（年份）                                                                                                                                                                        | 信度  |
| -------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| 塔罗牌胶印（中国印厂）          | 每副 $1.99–8.55（200–3,000 副，含运至美国本土 + 关税；量大价低）；MOQ 200；1,000 副比 200 副便宜 40–50% | [QinPrinting 塔罗印刷页](https://www.qinprinting.com/tarot-card-printing/)（2025–2026，印厂自报价）                                                                                        | 🟡  |
| 塔罗牌胶印，1,000–2,000 副  | 约 $2–5/副，全款预付                                                                | [globalspiritualstudies](https://globalspiritualstudies.com/cost-to-make-a-tarot-deck/)                                                                                       | 🟡  |
| 精装 / 加工附加            | 天地盖 / 磁吸盒、烫金、内衬每副 + $1–2 或更多                                                 | 同上                                                                                                                                                                            | 🟡  |
| 按需印刷（POD）            | 1 副 $24.90；50 副 $10.95/副；另一说 $5–7/副                                          | [printkk](https://www.printkk.com/gb/blog/articles/print-on-demand-tarot-cards)、[qpmarketnetwork](https://qpmarketnetwork.com/making-custom-tarot-cards-with-print-on-demand) | 🟡  |
| 起订量                  | 美国小厂 25 副起；海外印厂 200–500 副；PrintNinja 500 副                                   | 同上；[PrintNinja](https://printninja.com/printing-products/custom-tarot-card-printing/)                                                                                         | 🟡  |
| 塔罗牌零售价               | **未查到**（本轮没搜）                                                                | —                                                                                                                                                                             | —   |
| 水晶手串批发（中国）           | 义乌购：8mm 散珠一串约 47 颗 ¥8.43（2 串起，**是散珠，不是成品手串**）                                | [yiwugo](https://en.yiwugo.com/product/detail/984703411.html)                                                                                                                 | 🟡  |
| 水晶手串批发（印度）           | 8mm 成品手串 ₹50（七脉轮）–₹180（紫水晶）/条                                                | [IndiaMART](https://m.indiamart.com/mscrystal/crystal-bracelets.html)                                                                                                         | 🟡  |
| 水晶手串批发（Faire，美国批发平台） | 8mm 手串建议零售价 $6–18；Faire 页面上的批发价与零售价大致是 2–3 倍关系（标签不清，未核实）                     | [Faire 例 1](https://www.faire.com/product/p_sgmj8qgnmm) 等                                                                                                                     | ⚠️  |
| 水晶手串零售               | Walmart 8mm 黑曜石 / 次石墨手串 $13.60；eBay 6 条一批约 $14.87                            | [Walmart](https://www.walmart.com/ip/6531271114)、[eBay](https://ebay.com/itm/276157079179)                                                                                    | 🟡  |
| 阿里巴巴成品手串 MOQ 与单价     | **未查到**（搜索没返回 alibaba）                                                       | —                                                                                                                                                                             | —   |

**收入公式骨架**：
`毛利 = 件数 × (零售价 − 出厂价 − 头程 / 关税 − 平台费（Etsy 约 10–15% / TikTok Shop 未查到）− 尾程运费 − 退货)`；塔罗另加 `− 设计 / 插画一次性成本`（benebellwen 有自出版成本文，本轮没打开）。手串 `出厂价` 的可靠数需Yixuan去东海一手询价。

---

## 6. SEO 工具站（广告 + affiliate）

| 指标                   | 数字                                                                         | 出处（年份）                                                                                                            | 信度       |
| -------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | -------- |
| 占星类展示广告 RPM          | **未查到**（Mediavine / Raptive 也没有结果）。泛品类：生活类博客约 $3 RPM；高价值品类 $8（娱乐）–$65+（金融） | [organicarbitrage](https://organicarbitrage.pages.dev/articles/display-ad-rpm-by-niche)（2026）                     | ⚠️（低质量站） |
| Astrology.com 收入结构   | 年收入「低八位数」美元；程序化展示广告 60% + 直售广告 20% + 邮件 15% + 付费内容 5%                      | [Digiday](https://digiday.com/media/astrology-com-grew-revenue-without-caring-social-distribution/)（年份未在摘要中显示，较早） | 🟡       |
| 占星站受众                | astrosofa：80% 女性，75% 移动端                                                   | [astrosofa 广告页](https://www.astrosofa.com/Contact/Ads)                                                            | ⚠️（媒体自述） |
| psychic 平台 affiliate | Keen 约 $100/新订户；Kasamba $100–125/新订户                                       | 见第 2 节                                                                                                            | 🟡       |
| 季节性                  | Q4 广告单价最高                                                                  | organicarbitrage                                                                                                  | ⚠️       |

**收入公式骨架**：
`月收入 = 月 PV × RPM（占星类未查到）÷ 1000 + 点击到 psychic 平台的人数 × 注册转化（未查到）× $100–125 CPA（🟡）+ 自有报告销售`。

---

## 7. AI 交付的推理成本

| 指标 | 数字 | 出处（年份） | 信度 |
| --- | --- | --- | --- |
| Claude Haiku 4.5 | 输入 $1 / 输出 $5 每百万 token | [DEV 对比表](https://dev.to/ab_ab_d41b57cab9a754e32a4/llm-api-pricing-comparison-table-2026-token-costs-across-providers-3if3)（2026；第三方，未读官方页） | 🟡 |
| Claude Sonnet 4.6 | $3 / $15 | 同上 | 🟡 |
| GPT-5 mini | $0.20 / $1.20 | [costbench](https://costbench.com/stats/llm-api-pricing-benchmarks-2026/)（2026） | 🟡 |
| GPT-5 nano | $0.05 / $0.40 | [fungies](https://fungies.io/llm-api-pricing-comparison-2026/)（2026） | 🟡 |
| DeepSeek V3.2 | $0.14 / $0.28 | [cloudzero](https://www.cloudzero.com/blog/llm-api-pricing/)（2026） | 🟡 |
| Batch / 缓存 | Batch 一般打五折；缓存输入远低于标准输入 | 同上多源 | 🟡 |

**数量级示例**（假设，非实测）：一份英文 AI 解读报告 ≈ 输入 5k token（排盘数据 + 系统提示 + 知识片段）+ 输出 4k token（约 3,000 词）。
- Sonnet 级：5k × $3/M + 4k × $15/M ≈ **$0.075/份**
- Haiku 级：≈ **$0.025/份**
- GPT-5 mini 级：≈ **$0.006/份**
- 一段 20 轮的 AI 塔罗聊天（累计输入约 100k、输出约 10k，不用缓存）：Sonnet 级约 $0.45，Haiku 级约 $0.15。

→ 对照报告售价 $7.99–49.99（第 1 节），**推理成本在 1% 量级以下**；单位经济的大头在获客，不在交付。（这是参数对比，不是结论。）

**收入公式骨架**：
`单份毛利 = 售价 − 应用商店 / 支付抽成 − token 成本（$0.006–0.075 / 份，估算）− 排盘 API（如 astrology-api.io $21/月起，转引 R1-F1-c）`。

---

## 缺口（下一轮 / R6 需补）

1. **占星 / 塔罗 App 的 CPI、web2app quiz 完成率、付费墙转化、D30 / D90 留存、LTV**：全部未查到分类数据。可补路径：RevenueCat SOSA 完整 PDF（Lifestyle 分类表）、Adapty Lifestyle 基准原文、Appfigures / Sensor Tower 付费报告；或 Semrush 之外买一次 AppMagic。
2. **psychic 平台给顾问的真实分成**：没有官方数字，两个第三方说法相差约 3 倍（顾问拿 >61% vs 约 22–27%）。需一手：去 Keen / Kasamba / Purple Garden 的顾问申请页或顾问论坛（Reddit r/psychicreaders 类）问，R6 列给Yixuan。
3. **塔罗主播专属收入**：零数据。需一手：访谈 2–3 个英文塔罗主播，或在 TikTok 实测观察几场直播礼物量。
4. **星盘海报客单、塔罗牌零售价、阿里巴巴成品水晶手串单价**：本轮没搜到 / 没搜。东海一手询价可补手串出厂价。
5. **TikTok Shop 玄学 / 水晶类目佣金率**：本轮没搜。
6. **占星类展示广告 RPM**：只有泛品类区间。可补：Mediavine / Raptive 发布商自曝收入帖。
7. **退款 / 拒付率（占星专属）**：只有 Adapty 全品类 iOS 8.3%（⚠️）；Nebula 投诉潮提示占星 Web2App 的拒付可能显著更高，未量化。
8. **LLM 单价**：均来自第三方汇总，落地前到各家官方定价页核一次。
