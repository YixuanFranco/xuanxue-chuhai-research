---
title: "玄学出海 · 规则与风险调研：规则与风险（平台 / 法律 / 支付 / 海外起号门槛）"
date: 2026-11-02
status: v0 —— 案头摘要级；27 次 WebSearch + 2 次 WebFetch（仅 developer.apple.com 能打开）；不下「能不能做」结论
permission_scope: 公开
---

# 规则与风险调研 · 规则与风险

> **方法**：WebSearch 27 次（额度上限 28）。WebFetch 只有 `developer.apple.com` 能打开（Apple 条款为**原文直引**）；`transparency.meta.com`、`ads.tiktok.com`、`support.google.com`、`www.etsy.com` 均被会话网络拦截，这几家的规则**只来自搜索摘要或第三方转述**，没对过原文。
> **信度**：✅ 官方原文或多个独立来源一致 · 🟡 单一来源 / 第三方转述 / 日期不明 · ⚠️ 卖服务的商家自述（有利益） · ❓ 没查到。
> **不重复**：Miss Cleo、Maria Duval、PFN、WTFuture/Struck 被 4.3 拒审、Nebula 扣费投诉、Co-Star 的 Android 缺位等**案例**已在 [`R1-F3-糊站验尸.md`](R1-F3-糊站验尸.md)，本文只写**规则本身**。
> 备选项编号指 [`01-充分做加法-备选项池.md`](01-充分做加法-备选项池.md) 的 #1–#64。

---

## 一句话摘要

查到的硬规则里，**没有哪个主流平台明文「禁止占卜」**；
真正卡人的是四类**通用规则恰好压在玄学的常见打法上**：
	① Apple 4.3(b) 把 fortune telling 点名为「已饱和类目」；
	② 「低价试用 → 自动续费」在加州 ARL（2025-07 起）和 FTC 的 ROSCA 执法下要求明示同意、留证、一键取消；
	③ 支付侧被商家普遍当作高风险（Stripe 对日本 / 墨西哥 / 泰国主体据转述直接禁止 psychic services）；
	④ 卖「结果」（爱情、复仇、转运、疗愈）在 Etsy、TikTok Shop、英国 ASA、印尼新刑法里都是红线。
		另外，**海外起号对Yixuan是一整套新门槛**（网络环境、开户代理、收款国别、直播资格），资料多为服务商软文，可信度低，需要一手实测。

---

## 一、风险表

### A. App 商店

| # | 风险 | 影响备选项 | 规则要点 | 出处（日期） | 信度 |
| --- | --- | --- | --- | --- | --- |
| A1 | **Apple 4.3(b)：fortune telling 是点名的饱和类目** | 1、3–8、12、15–20、22（若做 App）、63、64 | 原文：「Certain kinds of apps, such as dating, flashlight, … and **fortune telling**, are well established on the App Store and we will not accept new submissions unless they offer a **meaningfully different or improved experience**. We may **remove these apps** … if they are not updated, improved, or do not attract customers.」注意约会也在同一句里——#5 合盘、#63 命理×约会两头都踩 | https://developer.apple.com/app-store/review/guidelines/ （2026-11-01 抓取，页面未显示更新日期） | ✅ |
| A2 | **Apple 1.1.6：「仅供娱乐」挡不住** | 18（AI 面相手相）、15、17、36 | 原文：「False information and features, including … trick/joke functionality … Stating that the app is "**for entertainment purposes**" won't overcome this guideline.」条款本身针对假功能（如假定位器）；是否会套到「拍照读面相」上，**是推断，未见实例** | 同上 | ✅（条文）/ 推断（适用性） |
| A3 | **Apple 3.1.3(d)：只有「一对一实时真人服务」可绕开 IAP** | 21、23–28（真人在线咨询）vs 15–20（AI 解读） | 原文：「real-time **person-to-person** services between two individuals … you may use purchase methods other than in-app purchase … **One-to-few and one-to-many** real-time services **must use in-app purchase**.」推论：AI 解读、群体直播课不在豁免内，走 IAP 抽成（抽成比例本轮未查） | 同上 | ✅（条文）/ 推论 |
| A4 | **Apple 3.1.2 订阅规则** | 1–3、8、15、19、20、56 | 自动续费订阅「must provide **ongoing value**」、周期 ≥ 7 天；订阅前「clearly describe what the user will get for the price」；试用前须写明时长、到期后失去什么、「any downstream charges」 | 同上 | ✅ |
| A5 | **Apple 5.1.1(iii) 数据最小化** | 所有收出生数据 / 照片的 App（1–7、16–18、63） | 原文：「only request access to data relevant to the core functionality … only collect and use data that is required」。出生时间、地点、照片要能说清为什么必需 | 同上 | ✅ |
| A6 | Google Play：**没找到点名占卜的条款**，只有通用 Spam / Repetitive Content | 同 A1 的 Android 版 | 「只复制 Play 上已有功能」的 App 违反 Repetitive Content；开发者反映封号理由含糊。占卜专属执法细节未公开 | https://play.google.com/intl/de_ALL/about/ip-deception-spam/spam/ ；开发者论坛转述 | 🟡 |

### B. 广告投放

| # | 风险 | 影响备选项 | 规则要点 | 出处（日期） | 信度 |
| --- | --- | --- | --- | --- | --- |
| B1 | **Meta：没找到 psychic / astrology 专属条款**；压在玄学上的是「个人属性」政策 | 1、2、5、9、10、15–21、23（一切靠 Meta 投流的 Web2App 漏斗） | 广告不得「assert or imply personal attributes」，不得暗示知道用户或其家人的个人属性 / 财务状况。玄学广告常见句式（「你最近感情是不是出了问题？」）直接撞线——**这是对句式的推断，未见占卜被拒实例** | https://transparency.meta.com/policies/ad-standards/objectionable-content/personal-attributes （原页被拦，取自搜索摘要） | 🟡 |
| B2 | Meta 2022 起**不能再按 tarot / astrology 兴趣定向** | 同 B1 | 2022-02 谣传「Meta/TikTok 封禁占星塔罗内容」被平台否认；真实变化是 Meta 删除了一批详细定向兴趣，含 tarot、astrology | https://www.papermag.com/tiktok-instagram-tarot-astrology-ban ；https://hypebae.com/2022/2/tarot-astrology-ban-tiktok-instagram-facebook-meta-rumors-paid-advertising-info （2022-02） | 🟡 |
| B3 | Google Ads：psychic 服务据称归入 **Unreliable Claims**，承诺结果会被拒 | 23、28、45、49、50（买词导流） | 唯一来源是营销博客；Google 官方页被拦，**没对原文** | https://www.graphed.com/blog/google-ads-for-psychics （日期不明） | ⚠️ |
| B4 | TikTok 广告：**没找到明文**禁止或限制占卜广告 | 1、2、30、37 | 官方 Ad Policy Handbook 被拦，未核。只确认 2022 「TikTok 封占星」是谣言 | https://ads.tiktok.com/help/article/ad-policy-handbook-north-america （未打开） | ❓ |
| B5 | LinkedIn（参照）：禁 fortune telling / 解梦 / 个人星座广告，**除非重点是娱乐** | 58、61（2B 投放时） | 第三方条款库转述 | https://conductatlas.com/platform/linkedin/linkedin-advertising-policies/provision/CA-P-063672/occult-pursuits-advertising-restricted/ | 🟡 |
| B6 | **英国 ASA / CAP**：宣称解读「真实、准确」大概率违规；不得误导或利用弱势人群 | 所有面向英国投放的方向 | ASA 有专门的「Psychics, spiritualists, fortune tellers…」与「Spiritual and psychic services」指导页 | https://www.asa.org.uk/advice-online/psychics-spiritualists-fortune-tellers-astrologers-and-clairvoyants.html ；https://www.asa.org.uk/advice-online/spiritual-and-psychic-services.html （日期未见） | 🟡（官方页，但只看到摘要） |

### C. 直播与内容平台

| #   | 风险                                                                             | 影响备选项                       | 规则要点                                                                                                                                                                            | 出处（日期）                                                                                                                                                                      | 信度               |
| --- | ------------------------------------------------------------------------------ | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| C1  | **TikTok LIVE：以「导流到站外」为主要目的的直播不进推荐流，并可能被限制变现**                                 | **30**（直播打赏 + 导流付费解读）、35、56 | 官方社区准则：LIVE 不进 For You 的情形包括「the **main purpose of the LIVE is redirecting people to go off-platform**」；不进 FYF 的内容「may be restricted from monetization features」。#30 的核心动作正好是导流 | https://www.tiktok.com/community-guidelines/en/accounts-features （检索于 2026-11-01）                                                                                           | ✅（条文）/ 套到塔罗直播是推论 |
| C2  | TikTok LIVE 资格：**开播与送礼 18+**；粉丝门槛约 1,000；部分地区不开放礼物                             | 30、35                       | 18+ 来自官方准则；1,000 粉、地区差异来自第三方（土耳其、俄罗斯被举例为限制礼物地区）                                                                                                                                 | 官方准则同上；https://ttcalculator.net/learn/tiktok-live-requirements/ 等（2026）                                                                                                     | ✅（18+）/ 🟡（其余）   |
| C3  | TikTok LIVE：**没找到**点名塔罗 / 占卜的条款；有付费解读被骗的请愿                                     | 30                          | 2024-05 TikTok 发布 LIVE 变现指南，报道只提「graphic、inauthentic、low quality」；Change.org 请愿称付费塔罗后被拉黑                                                                                        | https://newsroom.tiktok.com/en-africa/tiktoklive （2024-05-24）；https://www.change.org/p/demand-tiktok-to-take-action-against-fraudulent-accounts-exploiting-vulnerable-users | ❓（专属条款）/ ⚠️（请愿）  |
| C4  | **TikTok 要求给逼真的 AI 生成内容打标**；用户可调低 AI 内容比例；Creator Rewards 是否收全 AI 视频**说法相互矛盾** | **36**（AI 玄学短视频矩阵）、35、20    | 官方：已给 13 亿+ 条 AI 视频打标，测试「Manage Topics」里的 AI 内容滑杆；第三方：Creator Rewards 要 18+、1 万粉、30 天 10 万播放、原创 >1 分钟，「unoriginal」不计                                                            | https://newsroom.tiktok.com/more-ways-to-spot-shape-and-understand-ai-content （2025-11-19）；第三方 2026 指南                                                                      | ✅（打标）/ 🟡（变现资格）  |
| C5  | **YouTube 变现按 AdSense 国家卡**：频道须位于开放地区，AdSense 不支持的国家走不完 YPP                    | 31、32、34                    | YPP 门槛：1,000 订阅 + 12 个月 4,000 小时，或 90 天 1,000 万 Shorts 播放。**中国大陆是否可收款：本轮搜索未证实**；历史上 AdSense 不向大陆付款、支持香港台湾——这是背景知识，待核                                                            | https://support.google.com/youtube/answer/72851 （原页被拦，摘要）                                                                                                                   | 🟡 / 大陆部分 ❓      |

### D. 电商与市场平台

| # | 风险 | 影响备选项 | 规则要点 | 出处（日期） | 信度 |
| --- | --- | --- | --- | --- | --- |
| D1 | **更正前提**：2012 年禁 metaphysical 的是 **eBay**，不是 Etsy | 45 | eBay 2012-08 起禁「spells; curses; … Psychic, Tarot, Reiki, and other metaphysical readings & services」，理由是无形商品难核实、难仲裁。大批卖家转去 Etsy | https://www.npr.org/2012/09/06/160697505/ebay-bans-supernatural-goods-and-services ；https://money.cnn.com/2012/08/16/technology/ebay-bans-spells/ （2012-08/09） | ✅ |
| D2 | **Etsy（2015 起，现行）**：禁 metaphysical services；**占卜解读可卖，但必须附有形交付物**，且不得承诺结果 | **45**、46、47、48、38（若宣称转运）、41 | 2015-06 新规：「any metaphysical service that promises or suggests it will effect a physical change … or other outcome (e.g., love, revenge) is not allowed, even if it delivers a tangible item」；现行 House Rules：tarot / psychic 解读「must include a tangible good」（牌阵照片、音视频、文字）；Reiki、远程疗愈被举为禁例。Vice 报道称近期仍有卖法术的店被清（日期未定） | https://www.etsy.com/legal/policy/services/242665313101 （原页被拦）；https://time.com/3929919/etsy-ban-spells （2015-06）；https://www.vice.com/en/article/etsy-witches-say-spell-casting-is-no-longer-welcome-on-the-platform/ | ✅（2015 规则）/ 🟡（现行措辞未对原文） |
| D3 | Amazon：**没查到**对占卜服务 / 法术类商品的规则 | 41、44、39 | 搜索只返回 eBay、Etsy | — | ❓ |
| D4 | **TikTok Shop：功效 / 疗愈宣称是主要雷区**；**没找到**水晶、灵性服务的点名规则 | **37**、38、41、42、43、44 | 第三方合规站：禁「unsubstantiated health, safety, and performance claims」；美区禁带身材焦虑、减重、心理健康伤害宣称的「wellness」商品；禁售 ≠ 限售（限售可凭资质卖）。据称 2026-05 美区有更新，未核 | https://www.godatafeed.com/disapproval/tiktok-prohibited-claims ；https://www.echotik.live/blog/prohibited-products-list-on-tiktok-shop-2026/ | 🟡 |

### E. 支付与拒付

| # | 风险 | 影响备选项 | 规则要点 | 出处（日期） | 信度 |
| --- | --- | --- | --- | --- | --- |
| E1 | **Stripe：按收款主体国别禁 psychic services** | 所有用 Stripe 收款的方向；尤其主体若设在泰国（Yixuan已有泰国店）、日本（#13）、墨西哥（#51 拉美） | 第三方条款库转载 Stripe 限制清单：**日本、墨西哥、泰国**栏下列「Psychic services and fortune tellers」；称文档 2026-05-20 更新。另有科技媒体称 Stripe 曾把 psychic services 从通用限制清单移除（日期不明）——两者不矛盾：全局放开、个别国家仍禁，**但没对 stripe.com 原文** | https://conductatlas.com/platform/stripe/stripe-restricted-businesses-list/thailand-psychic-services-prohibited/ （及 japan / mexico 同站页）；https://stripe.com/us/restricted-businesses/ （未打开）；https://www.thetechoutlook.com/…stripes-decision-of-unrestricting-psychic-services/ | 🟡 |
| E2 | PayPal：AUP **没查到**点名 psychic / astrology 的条款 | 同上 | 只确认 AUP 有「禁止」和「需预先批准」两档，且不穷尽 | https://www.paypal.com/uk/webapps/mpp/ua/acceptableuse-full | ❓ |
| E3 | **收单行把 psychic / tarot 普遍归为高风险商户**：无形、主观、易争议；传统银行常拒 | 23–28、30、45、48、1–3（Web 端收款） | 说法全部来自卖高风险收单服务的公司 | https://paymentcloudinc.com/industries/psychics/ ；https://corepay.net/industries/tarot-and-psychic-merchant-accounts/ ；https://paykings.com/tarot-and-psychic-merchant-account/ | ⚠️ |
| E4 | **卡组织拒付监控阈值约 0.9%–1%（口径不一）** | 同 E3 | Visa 2015 起从 2% / 200 笔降到 1% / 100 笔（一说 0.9%）；Mastercard 一说 1%，一说 1.5%–2.99% 为低档、≥3% 为高档；两家分母口径不同。超标→加费、限制、关户 | https://www.americanbanker.com/payments/news/risky-merchants-get-riskier-under-bolstered-visa-acquirer-program ；https://chargebacks911.com/excessive-chargeback-programs.md 等 | 🟡（数字互相冲突，需对卡组织原文） |
| E5 | **行业常见退款 / 拒付数字（非玄学专属）** | 1–3、8、15、19、20 | 移动订阅 App 退款率约 **2%–5%**（Adapty 引自自有数据 + RevenueCat 报告）；**硬付费墙退款率明显高于免费增值**；SaaS 拒付率 0.8%–1.5%（第三方，弱）；被拒退款的用户会直接找银行拒付，Apple 侧拒付高会危及开发者账号。案例：Dipsea 退款率 3%→1.9%（厂商案例） | https://adapty.io/blog/refund-rate-metrics-and-benchmarking/ ；https://www.revenuecat.com/docs/dashboard-and-metrics/charts/refund-rate-chart ；https://chargebackcost.pages.dev/saas-chargeback-rate | 🟡 / ⚠️；**玄学类目专属数字 ❓** |

### F. 法律（按地区）

| # | 风险 | 影响备选项 | 规则要点 | 出处（日期） | 信度 |
| --- | --- | --- | --- | --- | --- |
| F1 | **美国联邦：FTC「Click-to-Cancel」规则已被撤销，但 ROSCA 执法照旧** | 1–3、8、15、19、20、33、42、56（一切自动续费） | 第八巡回法院 2025-07 以程序理由撤销（未审实体）；FTC 2026-02/03 以 ANPRM 重启 Negative Option 规则制定，尚无替代规则生效；FTC 继续用 ROSCA 打订阅陷阱（2025 年诉 Uber 订阅）。民事罚款据称最高约 $53,088 / 次违规（可能已按通胀调整，待核） | https://www.gibsondunn.com/ftc-restarts-negative-option-rulemaking-after-eighth-circuit-vacatur-enforcement-under-rosca-continues/ （2026-02-27）；https://www.alston.com/en/insights/publications/2025/07/ftc-click-to-cancel-rule-vacated （2025-07）；https://www.bclplaw.com/…im-not-dead-yet… （2026-03） | ✅ |
| F2 | **加州 ARL（AB 2863，2025-07-01 生效）** | 同 F1 | ① 须取得「express affirmative consent」，同意凭证保存 ≥3 年或合约终止后 1 年（取长）；② 每年发提醒（服务、扣费频率、金额）；③ 价格 / 服务重大变更须显著告知；④ 「click to quit」线上一键取消；⑤ 免费转付费也纳入；不得就任何交易重要事实作误导。适用于 2025-07-01 后订立、修改或续期的合约 | https://btlaw.com/en/insights/alerts/2025/california-expands-automatic-renewal-law-new-requirements-now-in-effect ；https://fenwick.com/insights/publications/california-tightens-requirements-for-automatically-renewing-subscriptions ；https://legiscan.com/CA/text/AB2863/id/3012746 | ✅ |
| F3 | 其他州自动续费法「在增多」 | 同 F1 | 只得到一句概括，**没拿到州名单** | Gibson Dunn 同上 | ❓ |
| F4 | **美国州 / 地方的占卜法：宾州整州按轻罪处理有偿占卜，马里兰是县镇级执照 / 禁令** | 23–29（真人咨询）、30、45；线下工作坊（55） | 宾州：1861 年起职业占卜为 misdemeanor（18 Pa.C.S. §7104）；2024-08 有人起诉称违宪；2025 年 HB 1562 提出废止，**进展未知**；2026-07 又有店主挑战（The Wild Hunt）。马里兰：Montgomery County 禁令被州上诉法院推翻（Nefedro 案，日期未取到）；Carroll County 2011 废止；Salisbury（2021 修订）要执照，Ridgely 禁止收费占卜，St. Mary's 要警长执照。**这些法对跨州线上服务是否适用：没查到** | https://en.wikipedia.org/wiki/Legality_of_fortune-telling ；https://wildhunt.org/2026/07/serpents-key-owner-challenges-pennsylvanias-fortune-telling-ban.html （2026-07）；https://www.abc27.com/news/top-stories/bill-proposes-repealing-bans-on-fortune-telling-in-pennsylvania/ ；https://salisbury.md/wp-content/uploads/2021/09/Ord-2676.pdf ；https://mgaleg.maryland.gov/2011rs/bills/sb/sb0469f.pdf | 🟡（宾州多源，现状未核）；其余州 ❓ |
| F5 | **英国：「for entertainment only」不是法定要求，也不一定能免责** | 所有面向英国的方向；与 A2 呼应 | 1951 年《Fraudulent Mediums Act》已废止（多个来源说「repealed」）。**废止时间与现行替代法未在本轮证实**：据背景知识，2008 年由 CPRs 取代、CPRs 又于 2025-04 被 DMCC Act 2024 第 4 部分取代——待对 legislation.gov.uk。Tarot Association 称法律未要求加娱乐免责；Simon Singh 认为小字免责未必站得住 | https://www.legislation.gov.uk/ukpga/Geo6/14-15/33/enacted ；https://www.tarotassociation.net/legal/legal-uk.pdf ；https://simonsingh.net/thats-entertainment-or-an-experiment-or-neither | 🟡（免责部分）/ ❓（现行法名与日期） |
| F6 | **欧盟 GDPR：出生日期 / 时间 / 地点是个人数据；本身不是第 9 条特殊类别，但「推断」可能触发** | 1–7、16、18（面部照片）、**5、63**（合盘 / 约会）、57、58（API 存数据） | Art.4 个人数据无争议；Art.9 是封闭清单，出生数据不在内。风险在推断：挪威 DPA 认定「是 Grindr 用户」即揭示性取向→特殊类别，2021 年对 Grindr 罚款（约 $7.1M）。合盘 / 约会产品若推断性取向、宗教信仰，**有可能**被同样处理——这是类比，不是既有判例。面部照片若用于唯一识别属生物特征数据——同为推断 | https://infobytes.orrick.com/2021-12-17/norwegian-data-protection-authority-fines-us-dating-app-71-million-alleged-gdpr-violations/ ；https://www.dataprotection.ie/organisations/know-your-obligations/lawful-processing/special-category-data ；https://roxyapi.com/blogs/astrology-api-data-residency-gdpr-checklist （⚠️ API 商） | ✅（Grindr、Art.9 清单）/ 推断（对玄学的适用） |
| F7 | **印度：没有专门管数字占星的法律**；1954《药品与魔法疗法（不良广告）法》是否覆盖占星有争议 | 14、61、62 | Storyboard18（2025-10）：无专门立法，DPDP 法下的数据问题被提及；Astrotalk FY2024 广告投放 Rs 162.7 crore（Tracxn）。2011 年孟买高院案中联邦政府宣誓书称该法不覆盖占星、手相、Vaastu。ASCI 2024–25 向 AYUSH 部转报 233 条广告，均为健康类，非占星 | https://www.storyboard18.com/how-it-works/biz-of-belief-how-indias-astrology-apps-are-turning-faith-into-fortune-amid-rising-regulatory-concerns-83027.htm （2025-10）；https://medicaldialogues.in/news/industry/pharma/asci-flags-233-health-ads-for-dmr-act-violation-reports-to-ayush-ministry-149226 | 🟡 |
| F8 | **越南：占卜本身不禁，但「组织迷信活动」与借民间信仰牟利可罚** | 26、22、51、30（越南语直播） | 第 38/2021 号议定书：组织迷信活动罚款，据称最高 4,000 万越南盾，组织翻倍；借民间信仰牟利的占卜被视为违法；2024-07 律所文章讨论 TikTok 上为牟利发占卜视频 / 直播可被罚；2026-05 新规提高「算胎儿性别」罚款至 500–700 万越南盾 | https://lawnet.vn/ngan-hang-phap-luat/en/tu-van-phap-luat/trach-nhiem-hinh-su/is-tarot-fortune-telling-a-violation-against-the-law-of-vietnam-383624 ；https://lawnet.vn/en/laws/posting-videos-and-livestreams-for-fortune-telling-on-tiktok-is-it-a-legally-permitted-activity-165678.html （2024-07-23）；https://news.tuoitre.vn/vietnam-to-levy-higher-fine-of-up-to-570-for-revealing-fetal-sex-from-may-15-103260508165543012.htm （2026-05） | 🟡（律所问答，罚额需对议定书原文） |
| F9 | **印尼：新刑法第 252 条（2026 年全面生效）** | 43（护身符）、26、22；任何卖「法术 / 下降头 / 改运」的服务 | 宣称有超自然能力并提供「致人痛苦或死亡」服务可罚；以此为业加重。针对的是 santet（黑巫术），普通塔罗 / 星座不在字面范围内；学界批评难以举证 | https://wikiwand.com/en/articles/2023_Indonesian_Criminal_Code ；https://jdih.pemalangkab.go.id/resource/media/3__Analisis_Yuridis_Tentang_Tindak_Pidana_Menyatakan_Diri_Mempunyai_Kekuatan_Gaib.pdf | 🟡 |
| F10 | 泰国：**没查到**占卜相关法律；只有 E1 的 Stripe 泰国主体禁令 | 26、37、43 | — | — | ❓ |

---

## 二、海外起号技术门槛清单（Yixuan的未知项）

> **先说可信度**：这一块的搜索结果**几乎全是卖 eSIM、代理 IP、指纹浏览器、开户服务的商家软文**，说法互相矛盾。下表把「需要什么」和「常见坑」分开写，每条标来源性质。**真正的答案要靠一手实测**（R6 线下手段）。
> 另外：搜到的很多「技巧」本质是**规避平台地区判定**，可能违反 TikTok 服务条款，带来封号与资金冻结风险——这里只记录行业说法，不是建议。

### 1. TikTok 账号（对应 #30、35、36、37）

| 项 | 需要什么 | 常见坑 | 来源 / 信度 |
| --- | --- | --- | --- |
| 网络与地区判定 | 平台会交叉比对 **IP、GPS 定位、SIM 国家码、系统语言 / 时区、设备**等信号 | 手机里残留国内 SIM、定位权限开着、注册与登录在不同国家来回切、切回国内网络 → 触发风控 / 「0 播放」 | microesim.com、relyvpn.com（卖 eSIM / VPN 的）· ⚠️ |
| VPN / 代理 | 只解决「连得上」 | **VPN 不保证过风控**；平台仍会单独评估 IP、设备、邮箱、手机号与行为是否可信 | relyvpn.com · ⚠️ |
| SIM 卡 | 据称影响初始地区 | 说法冲突：有的说必须换当地 SIM，有的说其他信号不一致时 SIM 没用 | 多篇软文 · ⚠️ |
| 新号行为 | 先正常浏览、慢慢完善资料 | 注册后立刻像机器人一样大量操作 → 限流 / 验证 | relyvpn.com · ⚠️ |
| 「0 播放」成因 | — | AMZ123 文章归因于 SIM 定位，推荐「代理 + 指纹浏览器」，但自己也承认「不绝对」，且文章有拼接痕迹 | amz123.com · ⚠️ |
| 平台对「伪装海外」的态度 | — | 抖音 2025-01 处置过万余个「有海外 IP 但非海外注册」的仿冒账号——这是抖音不是 TikTok，但说明平台层面的地区风控真实存在 | ithome.com（2025-01）· 🟡 |
| 正规路径 | 搜索摘要建议：正式业务用 TikTok Shop / 商业账号官方渠道，在目标国配备**真实本地主体、手机号、办公环境** | — | 搜索工具总结 · 🟡 |

### 2. TikTok LIVE 与变现（对应 #30）

| 项 | 门槛 | 来源 / 信度 |
| --- | --- | --- |
| 开播 | **18+**（官方）；粉丝约 **1,000**（第三方，有说 16 岁可播的冲突说法） | tiktok.com/community-guidelines ✅；ttcalculator.net 等 🟡 |
| 收礼物 | **18+**（韩国 19+）；部分国家开放直播但限制礼物 | 第三方 🟡 |
| 进推荐流 | 以**导流站外**为主要目的的 LIVE 不进 For You、可能限制变现（见 C1） | 官方 ✅ |
| Creator Rewards | 18+、1 万粉、30 天 10 万播放、原创 >1 分钟、**所在国家须在开放名单内**（名单本轮未拿到） | 第三方 2026 · 🟡 |
| AI 内容 | 逼真 AI 内容须打标（见 C4） | 官方 ✅ |

### 3. TikTok Shop 美区跨境店（对应 #37、41、44）

| 项 | 要求（2025-10 第三方指南为主） | 冲突 / 坑 | 来源 / 信度 |
| --- | --- | --- | --- |
| 主体 | **中国内地或香港公司营业执照**，经营范围覆盖类目；**不支持个体户** | — | sellersprite.com（2025-10）；tt123.com · 🟡 |
| 履约 | **美国本地发货能力**（海外仓或 FBA 多渠道） | — | 同上 · 🟡 |
| 经营证明 | 第三方平台店铺链接 + **美国站近 12 个月 GMV 截图** | 另一篇称已不需要三方平台证明——两篇矛盾；2024-01 旧文的「亚马逊单店 GMV ≥ 200 万美元」已过时 | tt123.com · 🟡 |
| 邀请码 | 珠宝类目或国内抖音知名品牌可申请邀请码入驻 | 「合伙人」是否算「抖音知名品牌」——**未知** | sellersprite.com · 🟡 |
| 可迁移经验 | Yixuan已有**泰国 TikTok Shop** 店铺经验（PLAN 资源盘点），东南亚店的开店流程可复用；美区规则不同 | — | PLAN.md |

### 4. Meta 投流（对应 #1、2 Web2App 漏斗）

| 项 | 要求 / 说法 | 来源 / 信度 |
| --- | --- | --- |
| 开户 | 中国大陆企业一般**须经 Meta 官方认证代理开户**；也有人尝试自助 BM，驳回率高 | ithome.com（2026-07）；china.com（2026-08）· 🟡（多为代理商软文） |
| 一级代理 | 据称大陆一级代理 **11 家**，2024–2026 名单未变；2025 年初起返点大幅下调 | baijing.cn · 🟡 |
| 封户连坐 | 2026 年风控交叉验证账户、主体、支付方式、设备，**一个户违规可能连坐同主体其他户**；高返点账户常是来路不明的「黑户」，封户后资金难追回 | ithome.com · ⚠️ |
| 玄学素材 | 见 B1 / B2：个人属性政策、兴趣定向已删 | 🟡 |

### 5. YouTube / Instagram（对应 #31、32、34）

| 项 | 情况 | 信度 |
| --- | --- | --- |
| YouTube 收款 | YPP 按 **AdSense 国家**卡；大陆是否可收**本轮未证实**（背景知识：历来不支持大陆、支持香港）→ 可能需要香港或海外主体 / 个人身份 | 🟡 / ❓ |
| Instagram | **本轮未查**（注册、限流、变现资格） | ❓ |

### 6. 收款主体（贯穿所有方向）

- Stripe 按**主体所在国**适用限制清单（E1）：主体放在泰国 / 日本 / 墨西哥，psychic services 据转述直接被禁；放在美国 / 香港的规则**本轮未核**。
- 主体选在哪（香港公司、美国 LLC、东南亚）会同时决定：Stripe 能否用、YouTube 能否收款、TikTok Shop 走跨境店还是本土店、税务——**这些交叉影响本轮都没有查**，列为缺口。

---

## 三、缺口（诚实说明）

**被网络拦住、没对原文的（R2 / R6 有条件时补）**：
- Meta 广告标准原文（transparency.meta.com）、TikTok 广告政策手册（ads.tiktok.com）、Google Ads 政策（support.google.com）、Etsy 现行 House Rules（etsy.com）、Stripe 限制清单原文（stripe.com）。要打开需在会话网络设置里放行这些域名。

**搜了没查到的**：
- TikTok 广告 / LIVE / Shop 是否**点名**占卜、塔罗、水晶（三处都只找到通用条款）。
- Amazon 对占卜服务与法术商品的规则；PayPal 是否点名 psychic；玄学的**专属 MCC 码**。
- **玄学类目专属的退款率、拒付率**——只有通用订阅 App 2%–5%、SaaS 0.8%–1.5%。
- 泰国占卜相关法律；菲律宾、马来西亚、日本、韩国、中东、拉美的相关法律。
- 美国除宾州、马里兰外的州法；这些州法对**跨州线上服务**是否适用。
- 英国现行法的准确名称与生效日期（FMA 1951 何时被什么取代）。
- 加州以外各州自动续费法清单。

**没来得及搜的**：
- Instagram 起号与变现资格；Apple 开发者账号以中国主体注册的要求；Apple IAP 抽成比例。
- TikTok 美国业务 2026 年股权 / 运营主体变化对中国团队开号、开店的影响。
- WhatsApp / Telegram / LINE 机器人（#22）的商业政策。
- 欧盟 DSA、AI Act 对「AI 解读」类产品的透明度要求（#15–20）。
- 海外税务（美国销售税、欧盟 VAT 对数字服务）。
- 中国侧：跨境收款结汇、数据出境（用户出生数据存回国内服务器）——对中国团队可能是硬约束，未查。

**下一轮建议补检**（预算允许时）：放行上述 5 个域名后逐一对原文；查 Stripe 美国 / 香港主体对 psychic 的现行规定；查 TikTok Shop 美区「crystals」类目审核实例；查 FTC 对占卜 / 星座 App 的 ROSCA 案（若有）。
