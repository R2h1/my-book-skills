# 置身事内：中国政府与经济发展 — Batch2 验证通过清单

> 来源候选池：principles.md (p01-p45) + counter-examples.md (x01-x25) + glossary.md (g01-g24)
> 验证方法：V1 跨域 / V2 预测力 / V3 独特性
> 批次：batch2，id 前缀 v50-v138
> 生成日期：2026-05-17

---

## 第一部分：原则 (Principles) — v50-v90 (41条)

---

```yaml
id: v50
title: 事权与外部性匹配原则
source_chapter: 第一章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第1章: 核心理论框架，外部性决定政府层级
    - 第5章: 城市化中土地配置的外部性问题
    - 第8章: 政府角色转型需要重新校准事权边界
V2_predictive_power:
  passed: true
  novel_question: "如果某个经济特区的产业污染影响到邻近省份，从外部性原则看应该由哪级政府管？"
  derived_answer: "污染具有跨省外部性，不能仅由特区所在地政府管，需要中央或省级以上政府介入协调。否则特区只会考虑本地收益而不承担全部成本。"
V3_exclusivity:
  passed: true
  why_not_common: "常识中政府权责划分常被视为政治博弈或历史惯例的结果，但作者将外部性理论系统化为一套可操作的事权划分分析框架——什么事该谁管，看影响范围有多大。这不是日常讨论中会使用的分析维度。"
```

---

```yaml
id: v51
title: 信息优势决定实际权威原则
source_chapter: 第一章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第1章: 形式权威与实际权威的区分
    - 第3章: 地方官员在信息上的优势解释了其实际自主性
    - 第4章: 中央产业政策在地方执行中的信息偏差
V2_predictive_power:
  passed: true
  novel_question: "为什么大公司CEO有最终决定权，但具体项目往往由中层经理说了算？"
  derived_answer: "因为CEO拥有形式权威（名义决定权），而中层经理掌握具体信息（客户需求、技术细节和技术团队能力），实际权威来自信息优势而非职位高低。如果CEO试图绕过中层亲自做所有技术决策，反而可能因信息不足做出错误判断。"
V3_exclusivity:
  passed: true
  why_not_common: "日常认知中'权力来自职位'是常见偏见。作者将组织理论中形式权威与实际权威的区分引入中国政府治理分析，揭示了'县官不如现管''上有政策下有对策'的制度根源，这个分析视角具有高度独特性。"
```

---

```yaml
id: v52
title: 激励相容设计原则
source_chapter: 第一章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第1章: 激励相容是事权划分三原则之一
    - 第3章: 官员任期短与投资冲动的激励不相容
    - 第4章: 产业政策中企业激励与政府目标的一致性问题
V2_predictive_power:
  passed: true
  novel_question: "为什么'环保一票否决'在地方执行效果远不如GDP考核？"
  derived_answer: "因为环保考核是'底线约束'而非'正向激励'——只要不出大问题就能过关，而GDP增长直接关联官员晋升和财政收益。激励不相容导致环保目标写在文件上但落实不到位。除非环保也进入晋升的正面考核权重，否则激励永远偏向经济增长。"
V3_exclusivity:
  passed: true
  why_not_common: "激励相容的经济学概念本身非作者原创，但作者将其系统应用于中国央地政府关系分析，揭示了属地管理为何是中国特色的激励相容设计，以及为何许多中央政策在地方走样。这种将抽象理论落地为制度诊断工具的能力是独特的。"
```

---

```yaml
id: v53
title: 事权决定财权原则
source_chapter: 第二章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第1章: 事权划分是全书分析的起点
    - 第2章: 分税制改革后地方事权不变但财权上收
    - 第3章: 地方为履行事权被迫创新融资工具（城投）
    - 第5章: 公共服务按户籍配置而非根据实际事权范围
V2_predictive_power:
  passed: true
  novel_question: "如果中央将社保统筹层级从市级提到全国，地方政府的财政压力会怎样变化？"
  derived_answer: "社保事权上收会减轻地方支出压力，即使中央不增加转移支付，地方也会有更多财力用于其他事务。反之，如果中央只收财权而不减事权（如分税制的做法），地方必然另寻财源——这正是土地财政的根源。"
V3_exclusivity:
  passed: true
  why_not_common: "常识直觉是'有多少钱办多少事'，但作者论证了在中国治理逻辑中是反过来的——先有事权（发展任务），然后才需要相应的财权。这个因果顺序是理解中国财政体制的关键，也是全书分析逻辑的起点，具有高度独特性。"
```

---

```yaml
id: v54
title: 土地资本化撬动信用原则（银根连着地根）
source_chapter: 第三章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第2章: 土地财政是土地资本化的前提
    - 第3章: 城投公司以土地抵押撬动信贷
    - 第5章: 居民按揭将个人收入资本化到房产
    - 第6章: 银行信贷与土地价值同涨同跌的顺周期
V2_predictive_power:
  passed: true
  novel_question: "如果中国推行严格的房产税且地价下跌30%，银行体系会面临多大冲击？"
  derived_answer: "土地是银行信贷的核心抵押物，地价下跌意味着抵押物贬值→银行收缩信贷→企业资金链断裂→抛售资产→地价进一步下跌的债务-通缩螺旋。由于地方融资平台和房企的大部分贷款都以土地为抵押，地价下跌的冲击会沿着'土地→城投→银行→经济'链条传导。"
V3_exclusivity:
  passed: true
  why_not_common: "常识说'土地是财富之母'，但作者深刻揭示了土地作为信用基石的具体机制——土地不会移动、不会消失，天然适合做抵押品，这使得土地成为中国金融体系扩张的物理锚点。'银根连着地根'这个高度凝练的表述是作者对中国特色金融体系的精辟概括。"
```

---

```yaml
id: v55
title: 分税制改革因果规则
source_chapter: 第二章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第2章: 分税制改革本身
    - 第3章: 催生城投公司和土地金融
    - 第4章: 影响地方政府招商引资行为
    - 第5章: 导致土地财政、高房价和城市化模式
    - 第7章: 重投资轻消费的结构失衡源头
V2_predictive_power:
  passed: true
  novel_question: "如果1994年分税制改革的收入分成比例改为地方拿大头，中国今天的经济结构会有什么不同？"
  derived_answer: "地方财政压力大幅减轻，土地财政和土地金融的需求会小得多。房价可能不会如此暴涨（地方无需高价卖地），地方债务问题也会轻很多。但另一方面，中央宏观调控能力可能减弱，转移支付体系难以建立，地区间差距可能更加悬殊。"
V3_exclusivity:
  passed: true
  why_not_common: "很多人知道分税制改革，但作者构建了一个完整的因果链条——分税制→地方财政压力→土地财政→土地金融→高房价/地方债/结构失衡。这条因果链贯穿全书，将看似无关的现象（高房价、地方债、产能过剩、贸易冲突）统一到一个解释框架中，具有高度系统性。"
```

---

```yaml
id: v56
title: 土地财政双轨定价规则
source_chapter: 第二章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第2章: 双轨定价机制的完整描述
    - 第4章: 低价工业用地招商引资
    - 第5章: 供应商住用地推高房价
V2_predictive_power:
  passed: true
  novel_question: "为什么中国工业用地价格远低于住宅用地，而发达国家两者差距很小？"
  derived_answer: "因为中国地方政府实行差异化供地策略——压低工业用地吸引投资换税收（长期收益），抬高商住用地赚取出让金（短期收益）。发达国家地方政府不承担同等发展任务，没有动力干预土地定价。这种双轨制是中国独特的财政-发展模式的产物。"
V3_exclusivity:
  passed: true
  why_not_common: "常识中'卖地赚钱'是对土地财政的简化理解。但作者揭示了地方政府在土地市场上同时扮演两个角色——工业用地的'补贴者'和商住用地的'垄断者'，这种双轨定价机制的内在逻辑是大多数人不了解的。"
```

---

```yaml
id: v57
title: 官员任期与政治投资周期规则
source_chapter: 第三章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第3章: 官员任期3-4年导致投资周期
    - 第5章: '摊大饼'式城市扩张
    - 第6章: 地方债务不断累积
    - 第8章: 官员短视行为的制度根源
V2_predictive_power:
  passed: true
  novel_question: "如果地方官员任期统一延长到7年且不允许调任，投资模式会如何改变？"
  derived_answer: "官员会更关注长期项目回报而非短期GDP数字。地下管网、教育医疗等'看不见的工程'投资会增加。但另一个风险是——如果官员干得不好，长期在任反而造成更大损失。任期制的权衡在于：太短导致短视，太长又缺乏问责。"
V3_exclusivity:
  passed: true
  why_not_common: "大多数人不把官员任期和宏观经济投资周期联系起来。作者揭示了一个机制：每年约三成地级市换主要领导→新官上任头两年投资激增→全国范围的投资脉冲和债务累积。这个'政治-投资周期'概念将微观人事制度与宏观投资波动直接挂钩。"
```

---

```yaml
id: v58
title: 城投公司债务螺旋规则
source_chapter: 第三章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第3章: 城投公司运作机制的完整描述
    - 第5章: 土地价格与城投债务的关系
    - 第6章: 地方债务风险的系统分析
V2_predictive_power:
  passed: true
  novel_question: "当城投公司'借新还旧'的模式遇到利率上升周期，会怎样？"
  derived_answer: "城投债的付息成本上升，但投资回报率极低（资产回报率中位数仅0.8%），收入根本无法覆盖利息，只能依赖更多政府补贴和更大规模的借新还旧。如果利率持续上升，债务螺旋会加速——新借款中越来越大的比例用于偿还利息而非投资，最终需要中央救助或债务重组。"
V3_exclusivity:
  passed: true
  why_not_common: "城投公司是中国特色制度创新——既是企业又是政府的延伸。作者揭示了'政府注入土地→抵押贷款→基建投资→土地升值→更多土地注入'这个自我强化的债务循环，以及对'政府隐性担保'导致市场定价机制失灵的深刻分析，都是独特贡献。"
```

---

```yaml
id: v59
title: 地方政府竞争三重加剧规则
source_chapter: 第四章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第4章: 潮涌现象、时间压力和产业政策趋同
    - 第8章: 官场+市场双重竞争模型
    - 第6章: 产能过剩的宏观后果
V2_predictive_power:
  passed: true
  novel_question: "为什么中国的新能源汽车行业会出现上百家品牌的大混战？"
  derived_answer: "三大因素同时作用：市场前景明确（潮涌现象）→各地一拥而上；地方政府竞相提供补贴和土地（时间压力）→投资门槛降低；中央鼓励新能源产业（政策趋同）→不管有没有条件都上。三重因素叠加，必然出现产能严重过剩后的残酷洗牌。"
V3_exclusivity:
  passed: true
  why_not_common: "产能过剩常被简单归因为'市场失灵'或'计划经济的恶果'。但作者提出的三因素叠加分析——潮涌现象、地方官员的短期时间窗口、中央政策导致的同质化竞争——构成了一个系统性的解释框架，超越了简单归因。"
```

---

```yaml
id: v60
title: 产业政策退出机制设计原则
source_chapter: 第四章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第4章: 光伏政策退出机制缺失的教训
    - 第6章: 僵尸企业难以退出
    - 第4章: 光伏标杆电价逐步退坡的成功经验
V2_predictive_power:
  passed: true
  novel_question: "如果政府要扶持一个全新的产业（如氢能），补贴方案应该从一开始就如何设计？"
  derived_answer: "必须预先设定补贴递减的时间表和退出条件（如光伏标杆电价逐步下调的机制），让企业从一开始就知道补贴会逐步消失，从而有动力降低成本和提高效率。同时要确保低效企业的破产退出渠道畅通，避免地方政府因就业压力持续输血。"
V3_exclusivity:
  passed: true
  why_not_common: "大多数关于产业政策的讨论集中在如何进入和扶持，很少有人系统思考退出机制的设计。作者从光伏产业的教训中提炼出'退出机制两层含义'——政策本身的退出时间和低效企业的退出渠道——这是产业政策评估中常被忽视的维度。"
```

---

```yaml
id: v61
title: 自主创新必须边干边学原则
source_chapter: 第四章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第4章: 京东方案例显示自主研发只能通过生产实践
    - 第4章: 光伏产业从代工到自主创新的过程
    - 第8章: '组织学习模式'的理论总结
V2_predictive_power:
  passed: true
  novel_question: "通过购买外国公司和引进技术团队，中国能实现芯片领域的自主创新吗？"
  derived_answer: "引进技术和团队是必要的起点，但远远不够。真正的自主创新只能通过自己的生产实践来积累——在制造过程中发现问题、改进工艺、与上下游深度互动。单纯靠购买无法获得默会知识（tacit knowledge），这就像光看菜谱永远学不会做菜。"
V3_exclusivity:
  passed: true
  why_not_common: "常识中'砸钱引技术'被认为是创新捷径。但作者论证了技术创新只能通过'边做边学'的亲身体验积累——买不来的默会知识只能通过实践获得。这个分析框架超越了简单的'引进消化吸收再创新'的官方表述。"
```

---

```yaml
id: v62
title: 比较优势可创造原则
source_chapter: 第四章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第4章: 京东方和韩国产业培育案例
    - 第8章: 发展目标与发展过程的讨论
    - 第4章: 产业政策的理论基础
V2_predictive_power:
  passed: true
  novel_question: "非洲国家是否应该接受仅出口原材料（比较优势），还是尝试培育制造业？"
  derived_answer: "如果仅遵循静态比较优势，发展中国家将永远困在低附加值环节。政府可以主动培育新的比较优势——如韩国用30年时间创造了造船和电子产业的比较优势。但前提是：政府必须有足够的政策能力和市场规模来支撑学习期的亏损。"
V3_exclusivity:
  passed: true
  why_not_common: "正统经济学认为比较优势是先天禀赋决定的，政府干预只会扭曲资源配置。作者挑战了这一教条，用韩国和中国的案例论证比较优势可以通过'边做边学'创造。这是经济学理论中的一个重大争议立场。"
```

---

```yaml
id: v63
title: 成功的政策需要协商和妥协原则
source_chapter: 第二章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第2章: 分税制改革的谈判过程
    - 第4章: 产业政策制定中的利益博弈
    - 第8章: 渐进改革方法论
V2_predictive_power:
  passed: true
  novel_question: "为什么一些在学术上论证严密的改革方案（如房产税）迟迟无法推进？"
  derived_answer: "因为政策落地不是学术论证的逻辑推导，而是多方利益博弈的结果。房产税改革涉及中央地方、城市农村、有房无房、多房少房等无数利益群体的博弈，如果无法找到各方都能接受的利益妥协方案，理论上再完美的政策也推不动。"
V3_exclusivity:
  passed: true
  why_not_common: "许多政策分析者将政策视为理性设计的结果，但作者揭示了政策形成过程的本质——成功的政策背后是成功的协商和妥协。用分税制改革的谈判案例（朱镕基逐个省份谈判、在关键条款上让步）生动说明了这一原则。"
```

---

```yaml
id: v64
title: 官场加市场双重竞争模型
source_chapter: 第八章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第4章: 地方政府招商引资竞争的实际表现
    - 第8章: 双重竞争模型的系统阐述
    - 第1-3章: 各级政府在事权-财权约束下的竞争行为
V2_predictive_power:
  passed: true
  novel_question: "官场+市场体制中，为什么会出现'富省穷财政'与'穷省富财政'同时存在的现象？"
  derived_answer: "因为官员竞争是零和博弈（晋升名额有限）而市场竞争是正和博弈（可互利共赢）——两种逻辑叠加导致复杂后果。经济发达地区的地方政府可能有更多财政资源，但官员的晋升竞争也更激烈，反而可能导致过度投资。欠发达地区虽然收入少但竞争压力也小（反正GDP上不去），反而可能更保守。"
V3_exclusivity:
  passed: true
  why_not_common: "这个模型将政治学（官员晋升竞争）与经济学（市场竞争）整合为统一分析框架。三个特点——政治激励挂钩经济表现、市场竞争约束官员、经济表现提供及时反馈——构成理解中国增长模式的独特视角。"
```

---

```yaml
id: v65
title: 政府角色随发展阶段转型原则
source_chapter: 第八章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第1-4章: 发展早期政府主导的积极效果
    - 第5-7章: 政府主导模式的负面效果显现
    - 第8章: 转型必要性的理论总结
V2_predictive_power:
  passed: true
  novel_question: "中国目前的经济发展阶段是否已经达到需要政府大规模退出经济干预的门槛？"
  derived_answer: "不能简单用GDP水平划线。当基础设施已基本完善（投资边际回报下降）、服务业占比超过工业、劳动力开始短缺、技术前沿逼近时，政府主导投资的组织优势就在下降，负面效应在上升。中国目前正处于这个转型期——东部沿海地区可能已过门槛，中西部可能尚未到达。"
V3_exclusivity:
  passed: true
  why_not_common: "非黑即白的两派观点（政府干预永远好 vs 政府干预永远坏）都很常见。作者提供了一个动态视角——角色有效性取决于发展阶段，早期有效的方式后期可能变成负担。这个'辩证的阶段论'超越了简单意识形态对立。"
```

---

```yaml
id: v66
title: 发展目标不等于发展过程原则
source_chapter: 第八章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第2章: 双轨制改革（价格双轨）
    - 第5章: 户籍和土地制度改革
    - 第8章: 方法论总结
    - 第8章: 三线建设的'无心插柳'效应
V2_predictive_power:
  passed: true
  novel_question: "如果中国现在就实行全民普选、独立司法、完全市场经济，经济会发展得更好吗？"
  derived_answer: "不能确定。发达国家的制度安排是它们发展到一定阶段的产物，而非发展的前提。照搬目标状态忽略了路径依赖和初始条件——在制度基础设施不完善时强行推开一套'理想制度'，可能导致混乱而非发展。这也解释了为什么苏联和东欧的'休克疗法'结果远不如中国的渐进改革。"
V3_exclusivity:
  passed: true
  why_not_common: "大多数讨论混淆了'应该达到什么状态'（目标）和'如何从A走到B'（过程）。作者强调发展路径不是目标状态的简单映射，这是全书最具方法论深度的贡献之一。"
```

---

```yaml
id: v67
title: 渐进改革需要缓冲机制原则
source_chapter: 第八章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第2章: 双轨制改革为国企改革留缓冲
    - 第5章: 户籍改革中的渐进式市民化
    - 第8章: '离土不离乡'的乡镇企业缓冲
V2_predictive_power:
  passed: true
  novel_question: "如果中国在1990年代就取消所有价格管制，结果会怎样？"
  derived_answer: "很可能导致剧烈的通货膨胀和社会动荡，就像俄罗斯'休克疗法'那样。价格双轨制虽然造成了腐败（'官倒'现象），但它为社会提供了适应市场经济的缓冲期——国有企业在计划轨道上维持基本生产，非国有企业则在市场轨道上逐步成长。没有缓冲机制的改革可能效率更高，但成本和风险也更高。"
V3_exclusivity:
  passed: true
  why_not_common: "纯效率视角的批评者常指责中国改革中的'扭曲'和'不彻底'。作者为这些看似低效的缓冲机制提供了辩护：改革节奏和方向同样重要，缓冲机制虽然扭曲但为受影响群体留出了适应时间。"
```

---

```yaml
id: v68
title: 债务-通缩循环预警规则
source_chapter: 第六章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第3章: 地方债务累积机制
    - 第6章: 债务-通缩螺旋的系统分析
    - 第5章: 房价下跌可能触发连锁反应
V2_predictive_power:
  passed: true
  novel_question: "日本1990年代泡沫破裂后的'失去的三十年'会在中国上演吗？"
  derived_answer: "中国面临类似风险但有不同条件。相同之处：都是资产泡沫+债务累积+人口老龄化的组合。不同之处：中国政府有更强的宏观调控能力、资本账户未完全开放提供了缓冲、城市化率仍有提升空间。预警信号包括：地价持续下跌、银行不良率快速上升、城投债违约蔓延。"
V3_exclusivity:
  passed: true
  why_not_common: "债务有风险是常识，但作者构建了完整的预警模型——三条信号（债务缺乏弹性、收入弹性大、资产抛售连锁反应）和传导机制（债务过重→抛售资产→资产跌价→信贷收缩→资金链断裂）。"
```

---

```yaml
id: v69
title: 负债率分析不能只看整体原则
source_chapter: 第三章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第3章: 地方债的纵向层级差异
    - 第3章: 地区间的横向差异
    - 第6章: 整体数字掩盖局部风险
V2_predictive_power:
  passed: true
  novel_question: "中央政府的债务率在安全范围内，为什么还需要担心中国的债务问题？"
  derived_answer: "因为欠债的不是抽象的'中国政府'而是具体的个体——地方融资平台、县级政府、西部欠发达省份。一个中西部县级政府的债务率可能是全国平均数的数倍。正如作者所说'某人欠1亿，全国人民每人出几分钱就能还，但足以压垮这个人'。分析债务必须穿透总量看局部。"
V3_exclusivity:
  passed: true
  why_not_common: "大多数媒体报道和宏观经济分析都用'中国债务占GDP比'这个总体数字。但作者强调这个数字掩盖了极其不均的分布——越基层负担越重，越往西部风险越高。这个穿透结构看局部的思维方法是分析债务问题的独特方法论。"
```

---

```yaml
id: v70
title: 银行信贷顺周期风险规则
source_chapter: 第六章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第3章: 土地作为抵押物与信贷扩张
    - 第5章: 房地产抵押贷款
    - 第6章: 信贷顺周期的完整分析
V2_predictive_power:
  passed: true
  novel_question: "为什么央行降息降准（宽松货币政策）在经济下行期效果越来越差？"
  derived_answer: "因为银行信贷的顺周期行为：经济下行时银行担心不良率上升而捂紧口袋，即使央行释放流动性，钱也流不到实体企业，而是在金融体系内空转。在中国尤其严重——银行信贷与土地价值深度绑定，经济下行意味着地价下跌，抵押物贬值进一步抑制放贷意愿。"
V3_exclusivity:
  passed: true
  why_not_common: "银行的顺周期行为是全球现象，但作者揭示了中国特色的顺周期机制——与土地金融的深度绑定使得顺周期效应被放大。'晴天送伞，雨天收伞'这个生动概括加上中国特有的'银根连着地根'，形成了独特的分析框架。"
```

---

```yaml
id: v71
title: 影子银行风险识别规则
source_chapter: 第六章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第3章: 城投公司的融资需求是影子银行的驱动力
    - 第6章: 影子银行运作机制和风险
    - 第6章: '资管新规'后的风险暴露
V2_predictive_power:
  passed: true
  novel_question: "如何从一家企业的财务报表中判断它可能通过影子银行融资？"
  derived_answer: "关注几个信号：账上有大量'应收款项类投资'或'买入返售金融资产'；负债端有大量理财产品或其他非存款类负债；利息支出远超正常贷款利率水平；资金用途不透明。影子银行资金成本通常比银行基准利率高50%-100%。"
V3_exclusivity:
  passed: true
  why_not_common: "影子银行是专业术语，但作者将其置于'土地金融'框架中理解——它是地方政府融资需求与银行监管约束之间博弈的产物。'按下葫芦起了瓢'的描述揭示了一个重要洞见：只要地方政府的融资需求不减，任何监管都会催生新的绕道方式。"
```

---

```yaml
id: v72
title: 收入不平等容忍度隧道效应规则
source_chapter: 第五章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第5章: 隧道效应与贫富差距的分析
    - 第7章: 经济增速下降与社会容忍度
    - 第8章: 发展阶段的转折判断
V2_predictive_power:
  passed: true
  novel_question: "为什么近年来中国社会对收入不平等的讨论比十年前更加激烈，即使基尼系数可能已经稳定？"
  derived_answer: "因为隧道效应——关键不在于不平等本身有多大，而在于穷人的队伍是否还在前进。经济增速放缓后，低收入群体收入增长停滞，即使贫富差距没有扩大，社会容忍度也会急剧下降。年轻人面临就业压力和高房价时，对'拼爹'现象的不满是隧道效应减弱的典型表现。"
V3_exclusivity:
  passed: true
  why_not_common: "隧道效应（Hirschman提出）虽非作者原创，但将其嵌入中国发展分析框架是独到的——它解释了为什么中国社会在高速增长期能容忍较大贫富差距，以及为什么这个容忍度可能随经济减速而快速下降。"
```

---

```yaml
id: v73
title: 房价与居民债务互推规则
source_chapter: 第五章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第5章: 房价-地价-财政-基建的链条
    - 第6章: 居民债务占GDP比重急剧上升
    - 第7章: 高储蓄和消费不足
V2_predictive_power:
  passed: true
  novel_question: "如果中国房价下跌20%，对居民消费会产生多大影响？"
  derived_answer: "负向财富效应和去杠杆压力将双重打击消费。一方面，有房家庭的'纸面财富'缩水，更不敢消费；另一方面，购房者的按揭负担不变但房子贬值，可能被迫减少其他消费来还贷。此外，银行收紧信贷也会抑制消费贷款。最终结果是消费下滑→经济减速→收入下降的恶性循环。"
V3_exclusivity:
  passed: true
  why_not_common: "房价影响消费是常见话题，但作者揭示了在中国特有的制度环境中，房价、地价、财政、基建、银行、居民债务如何形成'一荣俱荣一损俱损'的复杂关系网。这个相互依赖的系统视角超越了简单的'房价高→买房难'的常识认知。"
```

---

```yaml
id: v74
title: 城市化以人为本原则
source_chapter: 第五章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第5章: '以土地为中心的城市化'批判
    - 第7章: 居民消费不足与公共服务缺失
    - 第8章: 从生产型政府向服务型政府转型
V2_predictive_power:
  passed: true
  novel_question: "为什么中国城市化率已超60%，但内需仍然不足？"
  derived_answer: "因为城市化'重量不重质'——常住人口城镇化率虽高，但大量农民工没有城市户口，无法享受教育、医疗等公共服务，消费意愿被抑制。土地的城市化快于人的城市化，2亿多常住人口没有市民化，他们的消费潜力远未被释放。"
V3_exclusivity:
  passed: true
  why_not_common: "关于城镇化的讨论大多关注率指标（城市化率多少了），但作者提出了'土地的城市化 vs 人的城市化'这一核心区分，并指出土地的资本化实质是个人收入的资本化——这一洞见将城市化、房地产、居民收入和消费纳入统一分析框架。"
```

---

```yaml
id: v75
title: 建设用地指标应随人口流动原则
source_chapter: 第五章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第3章: 土地供给的行政分配机制
    - 第5章: 指标错配导致房价分化
    - 第8章: 要素市场改革方向
V2_predictive_power:
  passed: true
  novel_question: "如果建设用地指标可以跨省自由交易，上海和北京的房价会怎样？"
  derived_answer: "建设用地指标会从欠发达地区流向发达地区，上海和北京的住宅用地供给可以大幅增加，有助于平抑房价。同时，欠发达地区通过出售指标获得可观的财政收入，不必靠低价卖地招商。但短期冲击是：发达地区政府会损失一部分卖地收入（地价下降）。"
V3_exclusivity:
  passed: true
  why_not_common: "建设用地指标的行政分配体制是计划经济遗留的产物，大多数人不了解这一制度如何扭曲了土地配置。作者揭示了'土地流向与人口流向背道而驰'这一关键矛盾——这是理解中国房价分化和区域失衡的关键制度变量。"
```

---

```yaml
id: v76
title: 国内国际失衡传导机制规则
source_chapter: 第七章
type: principle
V1_cross_domain:
  passed: true
  evidence:
    - 第4章: 产能过剩形成出口压力
    - 第5章: 消费不足
    - 第7章: 贸易顺差→贸易冲突
V2_predictive_power:
  passed: true
  novel_question: "即使中美贸易战完全停止，中国的外贸环境会根本性改善吗？"
  derived_answer: "不会。因为贸易冲突的根源在国内结构失衡——只要重生产轻消费的模式不改，产能过剩就会持续要求出口，对全球市场的冲击就不会消失。即使美国不加关税，其他国家的保护主义也会抬头。贸易问题从来不是单纯的贸易问题。"
V3_exclusivity:
  passed: true
  why_not_common: "中美贸易冲突的报道铺天盖地，但鲜有人将其追溯到中国内部的'地方政府重生产轻消费'这一制度根源。作者建立了国内结构失衡→产能过剩→出口依赖→贸易冲突的完整因果链，将贸易问题还原为国内治理问题的外部表现。"
```
```