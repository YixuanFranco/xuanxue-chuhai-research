# 多语种查词 · 多语种区域查词（非英语市场）

> 调研日期：2026-11-01 · 方法：哥飞式查词（看每个词搜出来是谁）· 执笔：Claude（子代理）
> 信度标记：✅ 搜索结果直接可见 / 🟡 单一来源或间接推断 / ⚠️ 未经本次搜索验证（凭背景知识，仅作线索）

## 0. 先说方法局限（读结论前必看）

1. **搜索工具不是 Google 本地 SERP。** 本次用的 WebSearch 是美国区通用搜索，结果明显偏向新闻稿、App Store 页、聚合评测，且混入大量**被劫持域名上的垃圾 PDF**（如 `*.govt.lc`、`dev.chyronhego.com` 上的「Carta Astral Gratis Grupo Venus」）。所以「前几名是谁」只能当**近似信号**，不能等同于当地 Google 第一页。要定稿须用 Ahrefs/Semrush 或本地 IP 实搜复核。
2. **搜索预算在第 37 次调用时用尽**（整轮共享 200 次上限）。**德语 / 法语 / 阿拉伯语 / 土耳其语 4 个语种一个词都没搜到**，印地语只搜了 3 个词，AstroTalk 收入也没查成。这些格子下面一律写「未查」，没有拿背景知识冒充查词结果。
3. 每个语种实际搜的词数：西 6 / 葡 6 / 日 6 / 韩 6 / 泰 6（含 1 个市场规模词）/ 印尼 4 / 越 3 / 印地 3 / 德法 0 / 阿土 0。**印尼、越南、印地没达到每个语种 6–8 个词的要求。**

---

## 1. 一句话结论

**非英语市场的「免费工具位」整体比英语弱，但每个市场弱的地方不一样。** 日、韩、印度的头部 App 和平台很强，靠「免费引流、真人或 AI 付费咨询」赚钱，正面打不进去。西语、葡语（巴西）、印尼语、越南语的搜索结果大多是新闻站每天发的星座稿、电商博客（Shopee）、零售商博客，还有垃圾页面，**真正好用的工具站很少**。所以「非英语市场竞争更弱」**大体成立，但只在工具类词上成立**，而且多半是付费习惯也弱的市场。

---

## 2. 语种竞争强度总表

| 语种 | 核心玩家（本次搜到的标 ✅） | 强度 | 明显空白 | 付费习惯 |
|---|---|---|---|---|
| **印度（印地/印度英语）** | AstroTalk ✅、Clickastro ✅、AstroSage ✅（他人文章提及）、AnyTimeAstro ✅、OnlineJyotish ✅、媒体 Amar Ujala / Aaj Tak / Prabhat Khabar ✅ | **强** | Kundli 基础工具已饱和；SERP 里出现 `*.pages.dev`、`vercel.app` 新站（graha-life、darshya、e-puja-platform）🟡，说明长尾仍有人在试，但头部太强 | 强：真人按分钟付费咨询（AstroTalk 模式）⚠️ 收入未查到 |
| **韩语** | 점신（테크랩스）✅、포스텔러（운칠기삼）✅、네이버 운세（搜索内置）✅、위키사주 ✅、银行 App 免费运势（신한라이프、NH농협）✅ | **强** | 免费供给太多：Naver 和银行都在免费送运势，工具站没有位置；只剩垂直细分，比如 AI 解读、속궁합这类擦边词 🟡 | 强：위키사주 单次 1,000–15,000 원 ✅；점신 营收「突破 200 亿韩元」（只见于报告目录标题）🟡 |
| **日语** | Yahoo!占い（500+ 种）✅、LINE占い ✅、マイナビニュース（每日星座 / 九星）✅、livedoor ✅、ザッパラス ✅、ココナラ ✅ | **强**（大众词）／**中**（东洋占术工具词） | 「四柱推命 無料 命式」排在前面的是海外多语站 masterseanchan.com 和 PR TIMES 新品稿 ✅，说明**本土没有压倒性的命式工具站**；九星気学「今日の運勢」被媒体每日稿包揽，没有工具 ✅ | 强：電話占い、有料鑑定导流成熟；奈良县消费者中心专门就「免费占卜转高额鉴定」发过警示 ✅ |
| **葡语（巴西）** | Personare ✅（星盘、塔罗、是否塔罗都被它包下）、Band（转载 Personare）✅、Astro.com ✅、miniwebtool / calculacentro（数字学）✅ | **中** | 数字学（numerologia）由通用计算器站 miniwebtool 占位 ✅，**没有本土专门玩家**；星盘只有 Personare 一家独大，完整版付费，免费版只讲太阳和上升 ✅ | 中：Personare 卖付费完整报告（约 25 页）✅ |
| **越南语** | 新闻站 baoquocte / doanhnghiephoinhap ✅、Shopee 博客 ✅、零售商博客 viettelstore / phongvu / mytour ✅、tuvi 类站（tuvicohoc、yeutuvi、tracuulasotuvi）🟡、Thái Âm / Lịch Vạn Niên App ✅ | **中** | 「xem bói」的前几名是**卖手机和电器的零售商博客** ✅，这是弱竞争的典型信号；「lá số tử vi」排盘出现海外站 masterseanchan ✅；官媒（Nhân Dân）把网上算命定性为「4.0 时代迷信」✅，有政策风险 | 弱到中 ⚠️ |
| **西语（拉美/西班牙）** | 新闻门户（La República、El Español、Expreso、Diario de Cuyo、Cronista、El Universal）✅、Bodas.net（配对）✅、miniwebtool / hacecuentas（数字学）✅、AstroBindi、mercurioretrogrado.com（星盘）✅ | **中偏弱**（工具词） | 「tarot gratis」「tarot sí o no」两个大词的前几名**几乎全是赞助软文和垃圾页**（periodicodeibiza 赞助稿、shapes.inc、劫持域名）✅，没有一个像样的本土塔罗工具占位；「carta astral gratis」被垃圾 PDF 刷屏 ✅ | 中：西班牙有电话塔罗（806 / +34 号码）导流文化 ✅（Hotmart 商品页可见），拉美偏低 ⚠️ |
| **泰语** | Thairath 占卜频道 ✅、The Thaiger ✅、Shopee 博客 ✅、HDmall ✅、ดวง Live（真人直播，2,000+ 位占卜师）✅、cosmenet ✅ | **中** | 「ไพ่ทาโรต์ ดูดวง ออนไลน์」「ดูดวงวันเกิด」排在前面的是 **Shopee 博客和新闻稿**，没有专门的塔罗工具 ✅；吉祥号码（เลขมงคล）由银行、餐饮点评、手机资讯站的文章占位，**没有好用的号码计算器** ✅ | 强（真人）：49 泰铢 / 题、90 泰铢 / 题，电话 200–300 泰铢 / 小时 ✅；73.8% 的受访者偏好通过网站或社交媒体获取占卜 ✅ |
| **印尼/马来** | detik ✅、JawaPos ✅、Kompas TV ✅、Shopee 博客 ✅、primbon.com ✅、kalenderku.id ✅、weton 计算 App（多款独立开发者作品）✅ | **弱** | **印尼语塔罗是空白**：搜「tarot gratis online bahasa indonesia」找不到一个本土印尼语塔罗站，结果全是 Tokopedia 卖实体牌和英文 App ✅；shio 2026 由新闻稿和 Shopee 占位，没有工具 ✅ | 弱 ⚠️ |
| **德语**（11-02 补） | astrowoche ✅、Astrodienst astro.com ✅、web.de ✅、一串 .de 塔罗站 ✅、多语种 upastrology ✅ | **中偏强** | 不是空白：塔罗、星盘都是专门站分食，没有一家独大；多语种工具站能拿星盘词第一 ✅ | 中：Astrodienst 卖完整报告 ✅，价格未查 |
| **法语**（11-02 补） | AsiaFlash ✅、horoscope.fr ✅、tarot.fr ✅、medium.fr 等通灵平台 ✅ | **强** | 只有星盘词是中小站分食；塔罗和 voyance 是付费通灵的导流口 ✅ | 强：电话 / 真人通灵导流成熟 ✅，价格未查 |
| **阿拉伯语**（11-02 补） | 埃及 / 黎巴嫩新闻站 ✅、islamweb ✅、解梦站（ruyaak、ahlam.ai）✅ | **弱** | 塔罗前排混英文站 ✅；咖啡杯占卜只有两三个小站（含 AI 读图）✅ | 未查（宗教合规风险最大 ⚠️，解梦比占卜更容易被接受 🟡） |
| **土耳其语**（11-02 补） | Hürriyet ✅、mynet / onedio ✅、一串 fal / tarot EMD 站 ✅、astroasist ✅ | **中偏强** | 咖啡占卜和塔罗都有六七个 EMD 站在抢，不是空白 ✅ | 未查（真人看咖啡杯照片很普遍 ✅） |

**竞争强度排序（只排查过的语种，强 → 弱）：**
印度 ≈ 韩国 > 日本（大众词） > 巴西 > 越南 ≈ 泰国 > 西语（工具词） > 印尼
（11-02 补查后插入：法语 ≈ 日本（大众词），德语 ≈ 土耳其语 介于日本和巴西之间，阿拉伯语 ≈ 印尼）🟡

---

## 3. 每个语种的词表明细

> 「类型」一列：工具站 / 内容站 / App / 平台 / 媒体 / 论坛 / 垃圾页

### 3.1 西班牙语

| 词 | 前几名（域名 · 类型） | 判断 | 理由 |
|---|---|---|---|
| horóscopo de hoy | larepublica.pe、elespanol.com、diariodecuyo.com.ar、expreso.com.pe、eldia.com.do（媒体）；App Store「Horoscopo de Hoy」（App） | **强** ✅ | 各国新闻门户每天发稿，权重高，量大，工具站插不进去 |
| tarot sí o no | periodicodeibiza.es 赞助稿 ×4、mercadolibre、toolmage、gumroad、垃圾 PDF | **空白** ✅ | 没有一个本土专门工具站；前几名是赞助软文和聚合目录 |
| tarot gratis | docs.shapedplugin.com、saad.da.gov.ph、ilc-2022.enea.it 等**被劫持站点的垃圾页**、periodicodeibiza 赞助稿、Hotmart（引导到电话号码） | **空白（但已被黑帽占位）** ✅ | 大词没有正规玩家。但被垃圾页刷屏本身说明有人在用黑帽抢流量，正规新站需要时间才能拿到信任 |
| carta astral gratis | cronista.com、expreso.ec（媒体教程）；bindi-online.com/astrobindi、mercurioretrogrado.com（工具站）；大量垃圾 PDF | **一般** ✅ | 有 2–3 个真工具，但都不是大品牌 |
| numerología | miniwebtool.com/es、hacecuentas.com（通用计算器站）、numerologiagratis.net、cronista（媒体） | **一般偏空白** ✅ | 占位的是通用计算器，不是专门做数字学的站 |
| compatibilidad de signos | todojujuy、redgol、cronista、laopinion、marie-claire.es、bodas.net、eluniversal.com.mx（媒体）；myrahpenaloza.com | **一般** ✅ | 几乎全是媒体文章，只有 bodas.net 有一个计算器；做交互式配对工具有空间 |

**核心玩家：** 拉美各国新闻门户（星座频道）、El Universal、Marie Claire ES、Bodas.net、miniwebtool。
**空白：** 塔罗（gratis / sí o no）、数字学、配对计算器。

### 3.2 葡萄牙语（巴西）

| 词 | 前几名 | 判断 | 理由 |
|---|---|---|---|
| horóscopo do dia | folhabv、ohoje、opovo、bemparana、band.com.br/horoscopo/personare、dgabc（媒体） | **强** ✅ | 跟西语一样，媒体每天发稿；Band 直接转载 Personare 的内容 |
| tarot online grátis | personare.com.br（tarot-do-dia）×2、App Store（Meu Tarot、Tarot Diário）、astrosofa.com | **强** ✅ | Personare 占位很稳 |
| mapa astral grátis | personare.com.br ×5、astro.com、my-zodiac-ai.com、App | **强** ✅ | Personare 自称「巴西最大的占星门户」（自述）；免费样本只给太阳和上升，完整版付费 |
| Personare 品牌词 | 几乎全是 personare.com.br 自己的页面 | — | 确认 Personare 有上百篇内容支撑 SEO，还上线了 AI 问答功能 ✅ |
| tarot sim ou não | personare.com.br ×4、agazeta.com.br、vocepergunta | **强** ✅ | 又被 Personare 拿下 |
| numerologia calcular | miniwebtool.com/br ×5、calculacentro.com、concursosnobrasil、catracalivre、band、iweaver.ai | **一般偏空白** ✅ | 通用计算器站和内容农场占位，没有本土专门的数字学品牌 |

**核心玩家：** Personare（一家独大）、Band 媒体、Astro.com、miniwebtool、Astrosofa。
**空白：** 数字学（numerologia）工具；占星和塔罗基本被 Personare 锁定。

### 3.3 日语

| 词 | 前几名 | 判断 | 理由 |
|---|---|---|---|
| 占い 無料 | weekly.ascii.jp、iphone-mania（评测）、Yahoo!占い / LINE占い（平台，正文提到）、my-best.com（评测）、Stella App | **强** ✅ | Yahoo!占い 有 500 多种占卜，LINE占い 是免费引流加付费鉴定的成熟模式 |
| タロット占い 無料 | App Store（多款）、my-best、app-liv、macotakara（评测） | **强** ✅ | App 生态成熟（ザッパラス、ジューン澁澤监修的 App） |
| 星座占い 今日 | news.livedoor.com、news.mynavi.jp（媒体每日排行）、App | **强** ✅ | 门户每天发排行稿，工具站没有位置 |
| 四柱推命 無料 | **masterseanchan.com/ja（海外多语排盘站）**、prtimes（新品工具发布稿）、bcnretail、jenova.ai、命式表 App（付费） | **一般 → 有空白** ✅ | 排在第一的是海外站，本土工具没有压倒性优势，2024–2026 年还有新工具在发 PR，说明这个词还没被吃透 |
| 九星気学 今日の運勢 | news.mynavi.jp ×9 | **一般** ✅ | 被一家媒体的每日稿包场，没有交互工具（比如吉方位计算） |
| 手相 | zexy、newsweekjapan、oggi（媒体）、coconala（平台博客）、iweaver.ai（AI 看手相）、weblio | **一般** ✅ | 以媒体科普为主；AI 看手相已经有海外玩家进来了 |

**核心玩家：** Yahoo!占い、LINE占い、ザッパラス、マイナビニュース、ココナラ。
**空白：** 东洋占术的**交互工具**（四柱推命命式、九星吉方位）。大众词（星座、塔罗）不要碰。

### 3.4 韩语

| 词 | 前几名 | 判断 | 理由 |
|---|---|---|---|
| 무료 사주 | brunch.co.kr ×2（推荐文）、daum（Naver 万岁历使用教程）、wikitree、App「생일의 비밀」、masterseanchan.com/ko、당근마켓（个人命理师） | **强** ✅ | Naver 搜索本身就内置免费사주和万岁历，工具站要跟搜索引擎自己的功能抢 |
| 사주 앱 매출 | innoforest 报告（运七技三 / 포스텔러、테크랩스 / 점신、피플벤처스） | — | 有三家公司规模大到值得研究机构写报告 ✅ |
| 궁합 | App「모두의 궁합」、wikitree、inblog.ai/sajutight（新玩家内容站）、gusle.kr、Tian Qi（masterseanchan 子站） | **一般** ✅ | 위키사주 免费；inblog 上的新站「사주타이트」在用擦边内容（속궁합）抢流量 🟡 |
| 오늘의 운세 | getcha、wikitree、ajunews、news-wa、imaeil、kyeonggi（媒体） | **强** ✅ | 媒体每天发稿 |
| 2026 신년운세 무료 | daum、App Store 포스텔러 ✅、점신 ✅、o2u 博客、idelighter 博客 | **强** ✅ | 两大 App 加 Naver、银行（신한라이프、NH농협）、한국경제，免费供给非常多 |
| 타로 무료 온라인 | App Store ×2、jenova.ai、creati.ai、toolmage、aitoolsspace（AI 工具目录） | **一般** ✅ | 本土没有塔罗网站占位，前几名是**英文 AI 工具的韩语目录页**；说明韩国塔罗主要在 App 里 |

**核心玩家：** 점신、포스텔러、네이버 운세、위키사주、银行和保险 App。
**空白：** 网页端塔罗；但韩国用户主要在 App 和 Naver 内，网页 SEO 的价值本身就低 🟡。

### 3.5 泰语

| 词 | 前几名 | 判断 | 理由 |
|---|---|---|---|
| ดูดวง | App「ดวง Live」×2、dailynews、thaipublica、hdmall.co.th、silpa-mag、trueplookpanya | **一般** ✅ | 真人直播 App 加医疗电商 HDmall 的副业页面。**医疗电商能排进前几名，说明这个词没有专门的强站** |
| ดูดวงความรัก | thairath.co.th ×7、cosmenet | **强** ✅ | Thairath 的占卜频道包场 |
| ไพ่ทาโรต์ ดูดวง ออนไลน์ | shopee.co.th 博客 ×2、thairath ×2、pptvhd36、my-best、appgoblin | **空白** ✅ | 排在前面的是电商博客和科普文章，**没有一个塔罗抽牌工具** |
| ดูดวงวันเกิด | shopee 博客、thethaiger.com ×7、LINE Today | **一般** ✅ | 媒体按星期几出生发每日稿，没有生日计算工具 |
| เลขมงคล เบอร์โทรศัพท์ | shopee 博客、krungsri（银行）、gotoknow、siamphone、wongnai、bangkokbiznews、checkraka | **空白** ✅ | 都是文章，**没有一个可以直接输入号码的计算器**。泰国人还有专门买吉祥号码的习惯（运营商也卖），这个空白值得关注 |

**核心玩家：** Thairath、The Thaiger、ดวง Live、HDmall、Shopee 博客（⚠️ 背景知识中还有 myhora、horoworld、Sanook / Kapook 占卜频道，本次没搜到，不计入）。
**空白：** 塔罗工具、吉祥号码计算器、生日 / 星期几工具。

### 3.6 印尼语 / 马来语

| 词 | 前几名 | 判断 | 理由 |
|---|---|---|---|
| ramalan zodiak hari ini | detik.com ×15、jawapos、shopee.co.id | **强（媒体）** ✅ | detik 包场；内容多为翻译 Hindustan Times 和 Astrotalk |
| primbon jawa weton | orami、inews、suara ×3、kumparan、popbela（App 推荐文）、journalarta、kalenderku.id、kapanlagi | **一般** ✅ | 有 primbon.com 和 kalenderku 两个工具，其他都是「推荐 weton App」的文章；工具体验可能很老旧 🟡 |
| shio 2026 | jawapos、shopee.co.id、kontan、merahputih、sonora、kompas.tv、popbela | **一般偏空白** ✅ | 全是媒体每日稿，没有输入出生年份就出结果的工具 |
| tarot gratis（印尼语） | tokopedia（卖实体牌）、英文 AI 工具、学术论文、App Store 英文 App | **空白** ✅ | 搜不到任何本土印尼语塔罗站，是本次最干净的空白 |

**核心玩家：** detik、JawaPos、Kompas、Shopee 博客、primbon.com。
**空白：** 印尼语塔罗、shio 工具、现代化的 weton 和配对工具。

### 3.7 越南语

| 词 | 前几名 | 判断 | 理由 |
|---|---|---|---|
| tử vi 2026 | shopee.vn 博客 ×4、App「Thái Âm - Tử Vi」、AI Tử Vi App、doanhnghiephoinhap、baoquocte、mytour、Lịch Vạn Niên App | **一般** ✅ | Shopee 和旅游平台（mytour）的博客能排在前面，说明这个词没有强势的专门站 |
| xem bói online miễn phí | viettelstore ×2、phongvu ×2、mytour、fptshop（**全是电子零售商博客**）、sggp / nhandan（官媒批评） | **空白（有政策风险）** ✅ | 零售商博客占据前几名，竞争很弱；但官媒把它定性为迷信 |
| lá số tử vi | 刷屏的 Google Docs、**masterseanchan.com/vi**、fptshop / phongvu（ChatGPT 教程）、baoquocte（推荐 tuvicohoc） | **一般 → 有空白** ✅ | 排盘工具有本土站（tuvicohoc、yeutuvi），但海外多语站能进前几名，说明本土站权重不高 |

（「tarot」这个越南语词没有单独搜；上一行的零售商博客里提到了 tarot.com.vn 和 thienmenh.net 🟡）

**核心玩家：** Shopee 博客、新闻站、零售商博客、tuvi 系列站、Lịch Vạn Niên App。
**空白：** 现代化的排盘和解读产品；但要先评估政策风险。

### 3.8 印地语 / 印度英语

| 词 | 前几名 | 判断 | 理由 |
|---|---|---|---|
| kundli matching free | 刷屏的 Clickastro 垃圾 PDF、Clickastro App、kundli.muthu.co、theweek.in（App 对比）、freepressjournal（榜单）、graha-life.pages.dev、darshya.pages.dev、appliedjyotish、onlinejyotish | **强** ✅ | 老品牌 Clickastro（1984 年创立）、AstroSage、AstroTalk 都有免费工具；有大量新的 pages.dev 站在试长尾 |
| janam kundali free | sites.google 博客、techjockey、mypanchang、onlinejyotish、vedicfeed、roxyapi、anytimeastro、appliedjyotish | **强** ✅ | 工具多到泛滥，同质化严重 |
| aaj ka rashifal（horoscope in hindi） | amarujala、prabhatkhabar、patrika、dnaindia、aajtak（媒体）；astrotalk.com/hi ×2 | **强** ✅ | 印地语大报加 AstroTalk 包场 |
| kundli（单词） / AstroTalk 收入 | 未查（预算用尽） | 未查 | — |

**核心玩家：** AstroTalk、AstroSage、Clickastro、AnyTimeAstro、印地语大报。
**空白：** 本次没有发现明显空白；免费 Kundli 工具已经是红海。

### 3.9 德语 / 法语 · 3.10 阿拉伯语 / 土耳其语

~~**全部未查**：horoskop heute、tarot kostenlos、horoscope du jour、tirage tarot gratuit、الأبراج اليوم、kahve falı、tarot falı 这 7 个词都没有搜，原因是搜索预算用尽。需要补跑。~~ → 11-02 已补 16 个词，见文末「补查」节 3.9–3.12。
⚠️ 待验证的线索（背景知识，**不能当结论用**）：土耳其 kahve falı（咖啡占卜）有「拍咖啡杯照片、由真人或 AI 解读」类 App（如 Faladdin），值得补查；阿拉伯语市场有宗教合规风险，要单独评估。

---

## 4. 最值得进入的 3 个语种及理由

| 排名 | 语种 | 切入词 | 理由 | 主要风险 |
|---|---|---|---|---|
| 1 | **西班牙语** | tarot gratis / tarot sí o no / numerología / compatibilidad de signos | 人口最大的非英语拉丁字母市场之一；两个塔罗大词的前几名**都是赞助软文和垃圾页** ✅，数字学由通用计算器占位 ✅；英文塔罗工具可以直接本地化；西班牙有电话塔罗付费的传统 ✅ | 黑帽垃圾页已经在抢位，新域名需要时间积累信任；拉美付费能力偏低 ⚠️ |
| 2 | **葡萄牙语（巴西）** | numerologia（全套计算器加解读）、星盘或塔罗的长尾细分 | 数字学没有本土专门玩家 ✅；Personare 证明了巴西用户愿意为「完整报告」付费 ✅；打法是避开 Personare 的核心词，从数字学切入 | Personare 在占星和塔罗上一家独大，正面打不动 |
| 3 | **日语（只做东洋占术工具）** | 四柱推命 無料 命式 / 九星気学 吉方位 / 手相（AI） | 付费意愿是所有语种里最强的 ✅（電話占い、有料鑑定）；四柱推命排在第一的是海外多语站 ✅，九星只有媒体稿 ✅，说明**工具位还空着**；中文团队做八字、九星有天然内容优势 | 星座、塔罗等大众词由 Yahoo! 和 LINE 把持，不要碰；日本消费者对「免费转高额」很警惕 ✅，变现要克制 |

**候补：**
- **印尼语**：塔罗完全空白，竞争最弱，但付费弱 ⚠️，适合广告变现或作为多语矩阵的一部分。
- **泰语**：吉祥号码计算器和塔罗工具是空白；真人付费习惯强（49–90 泰铢 / 题）✅，可以考虑「工具引流，接真人或 AI 付费解读」。
- **越南语**：竞争弱，但官媒定性为迷信，有政策风险。

**一个跨语种发现：** masterseanchan.com 同时出现在日语「四柱推命」、韩语「무료 사주」、越南语「lá số tử vi」的结果里 ✅，它是一个**已经在做多语种八字 / 紫微排盘程序化 SEO 的玩家**。这说明两件事：①「东方命理工具 × 多语种」这条路确实有人在走，而且能排上去；② 它就是这条路上最直接的对标对象，下一轮应该专门拆它的流量和变现方式。

---

## 5. 市场规模 / 代表公司收入

| 市场 | 数字 | 来源 | 信度 |
|---|---|---|---|
| 泰国 | 精神类商品和服务市场约 3.04–4.56 亿美元（泰国商会大学估算，经 Guardian 转述） | 搜索结果摘要（Taipei Times / inkl 等转载） | 🟡 |
| 泰国 | 疫情后占卜支出约 50 亿泰铢 / 年（约 1.5 亿美元），之前约 40 亿；数字出自初创公司 A Duang | Reuters，经 The Star / Euronews / Cyprus Mail 转载（2022） | 🟡（数字来自企业自述） |
| 泰国 | 73.8% 的受访者偏好通过网站或社交媒体获取占卜服务 | 同上 | 🟡 |
| 泰国 | Allied Market Research 有《Thailand Astrology Market》报告，数字未见 | alliedmarketresearch.com | 未查到具体数字 |
| 韩国 | 점신（테크랩스）营收「突破 200 亿韩元」，只见于报告目录标题，年份不明 | innoforest.co.kr 报告 NS00000275 | 🟡 |
| 韩国 | 포스텔러约 5% 的内容收费，但营收主要来自这部分 | 同上 | 🟡 |
| 日本 | 占い市场规模 | **未查到**（预算用尽） | — |
| 印度 | AstroTalk 收入 | **未查到**（搜索被预算拦截） | — |
| 巴西 / 西语 / 印尼 / 越南 / 德法 / 阿土 | 市场规模 | **未查到** | — |

> 按 CLAUDE.md 规则 2 的精神：上面所有数字都是二手转述或企业自述，**不能作为推算的输入**。

---

## 6. 来源

**西语**
- [La República 星座](https://larepublica.pe/horoscopo/2024/05/09/horoscopo-de-hoy-10-de-mayo-2024-evat-598932) · [El Español](https://www.elespanol.com/sociedad/horoscopo/20231126/horoscopo-hoy-miercoles-noviembre-predicciones-trabajo-dinero-amor/811169220_0.html) · [Expreso](https://www.expreso.com.pe/variedades/horoscopo-de-hoy-conoce-las-predicciones-del-lunes-11-de-marzo-de-2024-segun-tu-signo-del-zodiaco-horoscopos-diarios-noticia/1077513/)
- [periodicodeibiza 赞助稿（tarot sí o no）](https://www.periodicodeibiza.es/pitiusas/ibiza/2021/12/17/1679987/tarot-gratis-fiable-cartas.html) · [Hotmart 电话塔罗](https://hotmart.com/es/marketplace/productos/tirada-de-tarot-gratis-llama-ya-al-34-911-438-430-para-respuestas-claras-y-reveladoras/B84527542H)
- [AstroBindi](https://bindi-online.com/astrobindi/carta-astral-gratis/) · [mercurioretrogrado.com](https://www.mercurioretrogrado.com/carta-astral) · [Cronista 星盘](https://www.cronista.com/mexico/espiritualidad/carta-astral-gratis-y-online-se-realiza-un-santiamen-y-asi-puedes-leerla)
- [miniwebtool ES](https://miniwebtool.com/es/calculadora-de-n%C3%BAmero-de-expresi%C3%B3n/) · [hacecuentas](https://hacecuentas.com/calculadora-numero-camino-vida) · [Bodas.net](https://www.bodas.net/articulos/compatibilidad-signos-zodiaco-amor--c8652) · [El Universal](https://www.eluniversal.com.mx/horoscopo/compatibilidad/)

**葡语**
- [Personare 每日塔罗](https://www.personare.com.br/tarot-do-dia) · [Personare 星盘](https://www.personare.com.br/signo/mapa-astral) · [Personare 是否塔罗](https://www.personare.com.br/tarot/tarot-sim-ou-nao) · [Personare 自称巴西最大门户](https://www.personare.com.br/conteudo/personare-maior-portal-astrologia-brasil-m187637)
- [Band × Personare](https://www.band.com.br/horoscopo/personare/noticias/horoscopo-do-dia-previsoes-dos-signos-para-hoje-sabado-18012025-202501180030) · [Astro.com](https://www.astro.com/free/free_chart_e.htm?lang=p) · [miniwebtool BR](https://miniwebtool.com/br/calculadora-de-numerologia/) · [calculacentro](https://calculacentro.com/calculadora/numerologia)

**日语**
- [weekly.ascii（Yahoo!占い）](https://weekly.ascii.jp/elem/000/001/231/1231430/) · [livedoor（LINE占い）](https://news.livedoor.com/article/detail/7613751/) · [奈良县消费者警示 PDF](https://www.pref.nara.jp/secure/196393/掲載7.6.pdf)
- [マイナビ 九星気学](https://news.mynavi.jp/article/20260911-4834048/) · [livedoor 星座排行](https://news.livedoor.com/article/detail/29901597/)
- [masterseanchan 四柱推命（日）](https://www.masterseanchan.com/ja/%e5%85%ab%e5%ad%97%e8%a8%88%e7%ae%97%e6%a9%9f-%e5%a4%aa%e9%99%bd%e6%99%82%e3%81%ab%e3%82%88%e3%82%8b%e5%9b%9b%e6%9f%b1%e6%8e%a8%e5%91%bd%e3%83%81%e3%83%a3%e3%83%bc%e3%83%88/) · [PR TIMES 四柱推命工具](https://prtimes.jp/main/html/rd/p/000000006.000181074.html) · [coconala 手相](https://coconala.com/blogs/2558151)

**韩语**
- [innoforest 运势平台报告](https://www.innoforest.co.kr/report/NS00000275) · [wikitree 무료사주](https://www.wikitree.co.kr/articles/993652) · [daum 网络万岁历](https://v.daum.net/v/WSRHdZ6b9I) · [daum 2026 新年运势](https://v.daum.net/v/20251224113503277)
- [포스텔러 App](https://apps.apple.com/KR/app/id1262949138) · [점신 App](https://apps.apple.com/KR/app/id960571015) · [inblog 사주타이트](https://inblog.ai/sajutight/남녀-사주-궁합-순위-총정리-천생연분부터-조심해야-할-조합까지-59351)

**泰语**
- [ดวง Live](https://apps.apple.com/app/id1316349233) · [thaipublica 价格](https://thaipublica.org/2023/08/newground34/) · [HDmall](https://hdmall.co.th/horoscope-tarot/index.html) · [Thairath 爱情运](https://www.thairath.co.th/horoscope/love/2274051)
- [Shopee TH 塔罗博客](https://shopee.co.th/blog/tarot-horoscope-history) · [The Thaiger](https://thethaiger.com/th/news/633070/) · [Krungsri 吉祥号码](https://www.krungsri.com/th/plearn-plearn/lucky-mobile-number-business) · [Wongnai](https://www.wongnai.com/articles/auspicious-mobile-phone-number)
- 市场规模：[Taipei Times](https://www.taipeitimes.com/News/feat/archives/2025/06/06/2003838129) · [The Star](https://www.thestar.com.my/news/nation/2022/04/19/pandemic-boom-for-fortune-telling-industry-in-thailand) · [Euronews](https://www.euronews.com/next/2022/04/15/us-health-coronavirus-thailand-fortunetellers) · [Allied MR](https://www.alliedmarketresearch.com/thailand-astrology-market-A80134) · [Nation Thailand · Ultimate Destiny](https://www.nationthailand.com/business/tech/40037717)

**印尼语**
- [detik 星座](https://www.detik.com/jateng/budaya/d-8371530/ramalan-zodiak-hari-ini-25-februari-2026-saatnya-pisces-menyelamatkan-diri) · [kalenderku 查 weton](https://kalenderku.id/cek-weton) · [journalarta](https://journalarta.com/news/2026/10/28/cek-weton-tanggal-lahir/) · [Shopee ID 生肖 2026](https://shopee.co.id/inspirasi-shopee/ramalan-shio-besok/) · [Kompas TV](https://www.kompas.tv/info-publik/652734/ramalan-shio-besok-25-februari-2026-peluang-rezeki-datang-siapa-paling-hoki) · [Tokopedia 塔罗牌](https://www.tokopedia.com/find/kartu-tarot)

**越南语**
- [Shopee VN tử vi 2026](https://shopee.vn/blog/tu-vi-2026/) · [viettelstore](https://viettelstore.vn/tin-tuc/top-website-xem-boi-bai-tarot-online-mien-phi) · [phongvu](https://phongvu.vn/cong-nghe/top-5-website-tarot-online-mien-phi-uy-tin/) · [Nhân Dân 批评](https://nhandan.vn/xem-boi-online-me-tin-di-doan-thoi-dai-40-post871503.html) · [masterseanchan 紫微（越）](https://www.masterseanchan.com/vi/lap-la-so-tu-vi-dau-so-mien-phi/) · [baoquocte · tuvicohoc](https://baoquocte.vn/bat-mi-dia-chi-tra-cuu-tu-vi-cuc-chuan-hoan-toan-mien-phi-tren-tu-vi-co-hoc-346049.html)

**印度**
- [The Week：6 款 kundli 配对 App 对比](https://www.theweek.in/konnect/economy/2026/09/24/6-best-kundli-matching-apps-compared-which-one-should-you-use.amp.html) · [Free Press Journal](https://www.freepressjournal.in/focused-view/5-most-accurate-kundli-matching-websites-in-india) · [OnlineJyotish](https://www.onlinejyotish.com/horo/) · [AnyTimeAstro](https://www.anytimeastro.com/astrology/janam-kundali) · [AstroTalk 印地语每日运势](https://astrotalk.com/hi/rashifal/aaj-ka-rashifal) · [Amar Ujala](https://www.amarujala.com/photo-gallery/astrology/predictions/aaj-ka-rashifal-11-october-know-today-horoscope-predictions-for-aries-taurus-virgo-leo-in-hindi-2024-10-10)

---

## 7. 待补（下一轮）

1. ~~德、法、阿、土 4 个语种，共 7 个词，全部补搜。~~（11-02 已补，每个语种 4 个词）
2. ~~印尼、越南、印地按要求补到每个语种 6–8 个词：越南补 tarot 和 tử vi hôm nay；印度补 kundli 和 horoscope in hindi 的单独结果。~~（11-02 各补 2 个：越南 tarot、tử vi hôm nay；印度 kundli、horoscope in hindi；印尼解梦、配对。印尼到 6 个，越南、印度到 5 个，**仍没到 6–8**）
3. 收入数据：AstroTalk FY25、日本占い市场规模（矢野経済研究所等）、점신 和 포스텔러 的公开财报。
4. ~~拆 masterseanchan.com：语种覆盖、页面数量、变现方式。~~（11-02 已拆，见 东方命理查词「补查」节；**页面数量和流量未查到**）
5. 用本地 IP 或 Ahrefs 复核「空白」判断，重点是西语塔罗、印尼语塔罗、泰语吉祥号码、日语四柱推命这 4 个。

---

## 补查（2026-11-02）

> 执笔：Claude（子代理）· 本节 22 次 WebSearch，全部 extended 模式（美国区通用搜索，**不是当地 Google**，第 0 节的局限照样适用）· 搜索量、收入：**本节都没查**

### 一句话

**德、法、土三个市场都有一批专门的本土工具站，不是空白；它们的弱点不在「没人做」，而在「站很多、没有一家独大」。** 法语和德语的塔罗、通灵词背后是成熟的「免费抽牌 → 付费电话 / 真人通灵」导流生意。阿拉伯语是这次四个语种里最弱的：塔罗前排混着英文站，咖啡杯占卜只有两三个小站，但宗教合规风险最大。🟡

一个跨语种发现：**upastrology.com 同时排在德语「geburtshoroskop berechnen」第一和法语「thème astral gratuit」第二**，**astroasist.com 同时出现在法语和土耳其语星盘词**。这和 masterseanchan 在日、韩、越语里的打法一样——多语种程序化工具站能打进本土词前排。✅

### 3.9 德语（补）

| 词 | 前几名 | 判断 | 理由 |
|---|---|---|---|
| horoskop heute | berliner-kurier.de（报纸每日稿）、astrowoche.de（老牌星座杂志）、astroportal.com、Wikipedia 杂项 | **强（媒体）** ✅ | 报纸和星座杂志包场；astroportal 页面约 102 天没更新，「新鲜度」有缝 |
| tarot kostenlos online legen | madame-lenormand.de、tarotlesen.de、astraly.de、tarot-tarot.de、kartenlegen-sofort.de、4mytarot.com/de、soultarot.de、astrolantis.de、astrolymp.de | **一般（拥挤）** ✅ | 前 9 全是德语专门塔罗站，大多「免费、免注册」；没有一家独大，但跟西语、印尼语不同，这里没有空位 |
| geburtshoroskop berechnen kostenlos | **upastrology.com/de（第一）**、astrohoroskop.org、astromantie.com、calcforlife.com/de、horoskop-paradies.ch、schicksal.com、astrocalculator（Susanne Seemann）、astrocarto.org/de、astrocarto.net/de（AI 解读） | **一般** ✅ | 本土站和多语种站混排，海外工具站能拿第一 |
| partnerhoroskop kostenlos | web.de（门户每周稿）、**astro.com（Astrodienst，免费试读版 + 付费完整版）**、astrologie-deutung.de、astrozeit24.de（约 867 天没更新）、velora-astro.de、sternzeichen.net、astrofree.de、astronumerology.app（NOVA） | **一般偏强** ✅ | Astrodienst 在德语区是主场；其余是中小站 |

**核心玩家：** astrowoche、Astrodienst（astro.com）、web.de 门户、一串 .de 塔罗站。**付费习惯：** 未查（Astrodienst 卖付费完整报告 ✅，价格未查）。

### 3.10 法语（补）

| 词 | 前几名 | 判断 | 理由 |
|---|---|---|---|
| horoscope du jour | asiaflash.com（1987 年起）、mon-horoscope-du-jour.com、horoscope.fr、idealvoyance.com、App Store ×3 | **强** ✅ | 老牌专门站 + App，日更；horoscope.fr 页面约 77 天未更新 |
| tirage tarot gratuit | astroya.fr、tarot.fr（约 40 种免费牌阵）、kardea.fr、oracles.ch（50+ 牌阵）、astrologie.fr、horoscope.fr、evozen.fr、tirage.net、voyancequalite.com | **强** ✅ | 专门站多且老；搜索摘要自己就说很多页面「把免费抽牌和付费咨询、『免费通灵』优惠混在一起」——塔罗是付费通灵的导流口，商业动力足 |
| thème astral gratuit | icalendrier.fr、**upastrology.com/fr（第二）**、astroquick.fr、astroya.fr（免费只给 5 颗行星，完整版付费）、astroastro.fr、astroasist.com/fr、out-of-nothing.life、astroo.com、infinita-corse-voyance.com、astrospirit.fr | **一般** ✅ | 中小站分食，多语种站能进前排；「免费只给一部分」的付费墙打法已有人在用 |
| voyance gratuite en ligne | espoirvoyance.com、cacarinette.com、quelvoyant.com（评测）、olivier-patrice.com、e-spacevoyance.fr、**medium.fr ×2（自称 200+ 通灵师）**、7tarot.fr、voox.online | **强** ✅ | 电话 / 视频通灵平台的主战场，「免费」是首次体验的钩子；对应英语的 online psychic，靠付费获客拼 |

**核心玩家：** AsiaFlash、horoscope.fr、tarot.fr、medium.fr 等通灵平台。**付费习惯：** 强（电话 / 真人通灵导流成熟）✅；具体价格未查。

### 3.11 阿拉伯语（补）

| 词 | 前几名 | 判断 | 理由 |
|---|---|---|---|
| الأبراج اليوم（今日星座） | youm7.com、masrawy.com、elwatannews.com ×2、mosaiquefm.net、lebanon24.com、nawa3em.com、arhoroscope.com、arabhaz.com | **强（媒体）** ✅ | 埃及、黎巴嫩、突尼斯的新闻站每天发稿；几个专门星座站内容已偏旧 |
| قراءة الفنجان اون لاين（咖啡杯占卜） | Facebook 主页、**zaracoffeebrew.com**（上传杯底照片，AI 几秒出结果，首次免费、完整版和套餐付费）、**أم نور（xn--mgbao7fonc.com，AI 读图，最多 5 张）**、alfinjan.net（真人看照片，要 WhatsApp 号码）、APKPure / Aptoide 上的安卓 App | **一般偏空白** ✅ | 只有两三个小站，AI 读图已有人进场；前排还有 Facebook 主页和 APK 下载站，说明没有像样的站。**这是本次阿拉伯语里最像机会的词**，但要先过合规 |
| تفسير الأحلام（解梦） | ar.wikipedia、aljazeera.net、mawdoo3.com、**islamweb.net ×2（教法裁定 fatwa + 咨询）**、dreams.alanbary.com、ahlamtafsir.com（伊本·西林解梦）、ruyaak.com、**ahlam.ai（AI 解梦）** | **一般** ✅ | 信息位被百科、半岛电视台和宗教网站占住；工具位有几个按伊本·西林、纳布卢西做的解梦站，已有 AI 站。注意：islamweb 的裁定是「由合格的人解梦可以」——**解梦在宗教上比星座、占卜更容易被接受** 🟡 |
| قراءة التاروت مجانا（免费塔罗） | tarot.free（英文站）、tarotreadingglobal.com、falita.app/ar（AI 多语站，还做咖啡杯、手相、星座）、tarotboard.com、arabtarot.com、gumroad、Google Workspace 插件（2022 年起没更新） | **空白** ✅ | 前排混着英文站、Gumroad 和停更插件，本土塔罗站只有 arabtarot 一家 |

**核心玩家：** 埃及和黎巴嫩新闻站、islamweb（宗教权威）、几个解梦站。**付费习惯：** 未查。⚠️ **合规**：伊斯兰教法一般禁止占卜（kahana），解梦相对被接受；做阿语市场要先单独评估，本轮没查到具体国家的法规。

### 3.12 土耳其语（补）

| 词 | 前几名 | 判断 | 理由 |
|---|---|---|---|
| kahve falı bak（咖啡占卜） | muhiku.com（博客）、nefisyemektarifleri.com（菜谱站）、modanium.com、kahvefalin.com、kahvefalibaktir.com、kahvefalin.net、falbak.net（AI / 算法）、fali.net、kahve.fali.net | **一般（拥挤）** ✅ | 前排有六七个精确匹配域名（EMD）站，上传照片看咖啡杯的流程已经很普遍；第 3.9 节提到的 Faladdin（App）没在网页结果里出现 |
| tarot falı ücretsiz | **hurriyet.com.tr（Mahmure 频道）**、tarotfali.org、tarot-fali.com、gunluktarot.com（也有 App）、popmotto.com、tarotfali.net、birfal.com、myburc.com、trendus.com、tarotburada.com | **强** ✅ | 大报 Hürriyet 排第一，后面是 9 个专门站 |
| günlük burç yorumları（每日星座） | mynet.com、sonsoz.com.tr、tgrthaber.com、ozgurkocaeli.com.tr、yildizgunlukleri.com、faldanfala.com、myburc.com、marasbugun.com.tr、onedio.com | **强（媒体）** ✅ | 全国门户和地方新闻站都在日更 |
| doğum haritası hesaplama ücretsiz（星盘） | astrokronos.com、**astroasist.com**、astrovizyon.com、astrocep.com、perigeeastrology.com、burcapp.com、dharmaastroloji.com（另有付费会员）、astroloji.org（2003 年起）、sarkacadam.com | **一般** ✅ | 一串本土中小工具站，加上多语种的 astroasist |

**核心玩家：** Hürriyet、mynet、onedio、一串 fal / tarot 精确匹配域名站。**付费习惯：** 未查（咖啡占卜「真人看照片」的模式很普遍 ✅，价格未查）。

### 3.6 印尼语（补，补到 6 个词）

| 词 | 前几名 | 判断 | 理由 |
|---|---|---|---|
| arti mimpi menurut primbon（按 primbon 解梦） | id.theasianparent.com、liputan6 ×2、suara.com、tizenesia.com、indozone、**kapanlagi ×4** | **强（媒体）** ✅ | 全是媒体长文，没有解梦工具；摘要提到有的文章用 AI 配图、文字也不通顺，内容质量低 |
| ramalan kecocokan pasangan berdasarkan tanggal lahir（按生日算配对） | tanamduit.com（理财 App 博客）、rukita.co（长租公寓博客）、jawapos、popbela、kumparan、fimela、borobudurnews、jatimnetwork、**primbon.com（唯一的工具）**、rakyatmediapers | **空白（工具位）** ✅ | 前 10 里 9 篇是「教你手算」的文章，有理财博客、公寓博客，只有 primbon.com 一个计算器。**有人在搜怎么算，却没人给一个现成的计算器**，跟 shio 2026 一样是工具空白 |

### 3.7 越南语（补，补到 5 个词）

| 词 | 前几名 | 判断 | 理由 |
|---|---|---|---|
| bói bài tarot online miễn phí | **zalopay.vn（支付 App 的活动页）**、bigstep.vn（AI）、kth-electric.com（电气公司站里的工具页）、tarot.com.vn、meobeostudio.com、cuthongthai.vn（AI，8 种牌阵）、tarotreader.me、boitarot.org | **一般** ✅ | 有几家本土塔罗站和 AI 站，但支付 App 和电气公司的页面也能进前三，说明专门站权重都不高 |
| tử vi hôm nay 12 con giáp（今日生肖运势） | suckhoedoisong.vn（卫生部主管的报纸）×2、baohatinh.vn、24h.com.vn、vtcnews.vn、2sao.vn、ngaydep.com、thanhnien.vn、xuongtuonggo.com | **强（媒体）** ✅ | 主流报纸日更包场。值得注意：**卫生部主管的报纸也在日更生肖运势**，和 Nhân Dân 把网上算命定性为迷信的说法并存——政策风险看来主要在「算命收钱」，不在「运势内容」🟡 |

### 3.8 印地语 / 印度英语（补，补到 5 个词）

| 词 | 前几名 | 判断 | 理由 |
|---|---|---|---|
| kundli | Wikipedia（同名地名 ×2）、Google Play「Kundli」App（vedicrishi）、mangalbhawan.com、vedicrishi.in、astroyogi.com、prokerala.com、ganeshaspeaks.com、mykundali.com、astrosage.com | **强** ✅ | 老牌工具站全员在场，红海 |
| horoscope in hindi today | aajtak.in、amarujala.com、hindi.webdunia.com（约 422 天未更新）、punjabkesari.in ×2、nakshtratak.com、App Store、寄生页（stripe.jhu.edu） | **强（媒体）** ✅ | 印地语大报包场，和 aaj ka rashifal 一致 |

（AstroTalk 收入已在 新灵性与 AI 查词 来源里，Outlook Business 报道 FY25，本节没重复查。）

### 来源（补查）

- 德语：[berliner-kurier](https://www.berliner-kurier.de/article/horoskop-heute-ihr-tageshoroskop-fuer-samstag-den-31-oktober-2026-10547107) · [astrowoche](https://www.astrowoche.de/tageshoroskop/heute/krebs) · [astroportal](https://www.astroportal.com/en/) · [madame-lenormand](https://www.madame-lenormand.de/tarot-orakel-kostenlos-online/) · [tarotlesen](https://tarotlesen.de/tarot-legen/) · [astraly](https://astraly.de/tarot) · [astrolantis](https://www.astrolantis.de/tarot-legesysteme/) · [astrolymp](https://www.astrolymp.de/tarot/) · [upastrology/de](https://upastrology.com/de/birth-chart) · [astrohoroskop.org](https://astrohoroskop.org/geburtshoroskop-kostenlos/) · [calcforlife](https://calcforlife.com/de/geburtshoroskop-rechner/) · [astrocarto.net/de](https://astrocarto.net/de/birth-chart-calculator) · [web.de 伴侣运势](https://web.de/magazine/unterhaltung/lifestyle/horoskop/partner/) · [astro.com 伴侣](https://www.astro.com/free/free_partner_g.htm) · [velora-astro](https://www.velora-astro.de/rechner/synastrie) · [sternzeichen.net](https://www.sternzeichen.net/partnerhoroskop/)
- 法语：[asiaflash](https://www.asiaflash.com/horoscope/horoscope-quotidien.html) · [mon-horoscope-du-jour](https://www.mon-horoscope-du-jour.com/horoscopes/quotidien/) · [horoscope.fr](https://www.horoscope.fr/horoscopes/aujourdhui) · [astroya 塔罗](https://www.astroya.fr/pages/tirage-tarot-gratuit) · [tarot.fr](https://www.tarot.fr/tarots) · [oracles.ch](https://www.oracles.ch/) · [tirage.net](https://www.tirage.net/) · [upastrology/fr](https://upastrology.com/fr/birth-chart) · [astroya 星盘](https://www.astroya.fr/pages/theme-astral-gratuit) · [astroasist/fr](https://www.astroasist.com/fr/) · [medium.fr](https://www.medium.fr/voyance) · [quelvoyant](https://quelvoyant.com/2026/03/17/voyance-gratuite-en-ligne/)
- 阿拉伯语：[youm7](https://www.youm7.com/Tags/Index?id=129424&tag=%D8%AD%D8%B8%D9%83-%D8%A7%D9%84%D9%8A%D9%88%D9%85) · [elwatannews](https://www.elwatannews.com/news/details/8387984) · [lebanon24](https://www.lebanon24.com/news/variety-news/1589597/%d8%a8%d8%b1%d8%ac%d9%83-%d8%a7%d9%84%d9%8a%d9%88%d9%85) · [zaracoffeebrew](https://www.zaracoffeebrew.com/ar) · [أم نور](https://xn--mgbao7fonc.com/) · [alfinjan.net](https://alfinjan.net/) · [islamweb 解梦裁定](https://www.islamweb.net/ar/fatwa/248524/) · [ruyaak](https://ruyaak.com/) · [ahlam.ai](https://ahlam.ai/) · [falita](https://falita.app/ar/tarot/) · [arabtarot](https://arabtarot.com/) · [tarot.free](https://tarot.free/)
- 土耳其语：[kahvefalin.com](https://www.kahvefalin.com/) · [kahvefalibaktir](https://www.kahvefalibaktir.com/) · [falbak.net](https://www.falbak.net/) · [hurriyet mahmure 塔罗](https://www.hurriyet.com.tr/mahmure/tarot-fali-bak-ucretsiz-ask-iliski-ve-kariyer-tarot-fali-acilimi-tek-3-kart-42505841) · [gunluktarot](https://gunluktarot.com/) · [mynet 星座](https://mynet.com/gunluk-burc-yorumlari-01-kasim-2026-koc-boga-ikizler-yengec-aslan-basak-terazi-akrep-yay-oglak-kova-balik-1336273-mykadin) · [onedio](https://onedio.com/astroloji/gunluk-burc-yorumuna-gore-1-kasim-2026-gunun-nasil-gececek) · [astroasist](https://www.astroasist.com/) · [astroloji.org](https://www.dogumharitasi.astroloji.org/) · [burcapp](https://burcapp.com/dogum-haritasi-hesaplama)
- 印尼 / 越南 / 印度：[kapanlagi 解梦](https://www.kapanlagi.com/feeds/arti-mimpi-menurut-primbon-jawa-panduan-lengkap-memahami-pesan-spiritual-f9b8a15c4b.html) · [primbon.com 配对](https://www.primbon.com/ramalan_cinta.htm) · [jawapos 配对](https://www.jawapos.com/zodiak/016043215/cara-hitung-ramalan-jodoh-berdasarkan-tanggal-lahir-cocokkah-hubungan-ini-dilanjutkan) · [zalopay tarot](https://zalopay.vn/boi-bai-tarot-4908) · [bigstep](https://bigstep.vn/boi-bai-tarot-online/) · [tarot.com.vn](https://tarot.com.vn/) · [suckhoedoisong](https://suckhoedoisong.vn/tu-vi-12-con-giap-hom-nay-2-11-mao-tai-van-kem-ty-dong-tien-on-dinh-169261101165312313.htm) · [astrosage kundli](https://www.astrosage.com/kundli/) · [prokerala kundli](https://www.prokerala.com/astrology/kundli/) · [aajtak](https://www.aajtak.in/religion/rashiphal) · [amarujala](https://www.amarujala.com/astrology/predictions/aaj-ka-tula-rashifal-1-november-2026-today-libra-horoscope-in-hindi-2026-10-31)
