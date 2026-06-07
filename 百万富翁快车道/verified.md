# 百万富翁快车道 — 三重验证通过的候选

> 通过率: 25/49 (51%) — 合并去重后共49个独立方法论，通过25个

---

- id: v01
  title: 三条路线图对比框架（人行道/慢车道/快车道）
  type: framework
  source_chapter: 4, 15, 37
  source_quote: |
    你可以有以下3个财务路线图：人行道路线图。慢车道路线图。快车道路线图。在这3个路线图中存在着不同的心理学和信念体系，分别决定着每个路线图的行动。
  summary: |
    将人的财富策略分为三条路线：人行道（无计划、即时满足、债务驱动，财富=收入+债务）、慢车道（牺牲今天换取未来，靠工作和复利，财富=工作收入+市场投资）、快车道（创业建立系统，财富=净利润+资产价值）。每条路线有其对应的思维路标和数学公式，可用于诊断自己当前所处的财务路线并确定切换方向。
  V1_cross_domain:
    passed: true
    evidence:
      - 第4章: 首次提出三条路线图的定义和各自的财富公式
      - 第15章: 通过慢车道7个危险论证慢车道并非安全选择，反向佐证路线图框架的诊断价值
      - 第37章: 通过设定终点四步法说明如何从快车道视角设计生活目标
  V2_predictive_power:
    passed: true
    novel_question: 一个年收入30万的程序员，没有储蓄但每月还房贷车贷，属于哪条路线？
    derived_answer: 看似慢车道（有稳定工作），但债务驱动的消费模式（房贷车贷）使其实际上接近人行道——财富公式中收入被债务吞噬，可自由支配时间为负。他需要先切断寄生性债务才能进入真正的慢车道，然后向快车道切换。
  V3_exclusivity:
    passed: true
    why_not_common: 普通人通常认为工作储蓄投资是唯一正路，创业和借钱消费被分别对待。作者将三者放在同一轴线上用同一套数学公式对比，揭示了它们的内在一致性和数学本质差异，这是独特视角。
  tags: [路线图, 诊断, 财富策略, 认知框架, 核心]

- id: v02
  title: 不可控的有限平衡（慢车道数学批判）
  type: reasoning_method
  source_chapter: 12, 15
  source_quote: |
    不可控的有限平衡证明了慢车道是毫无出路的。你怎么可能在慢车道上致富呢？你得到一份高薪工作，存钱，省吃俭用，投资股市，就这样重复50年。
  summary: |
    一种数学推理方法，用于分析任何财富策略的内在缺陷。核心逻辑：拆解策略的财富公式，检查其变量是否同时满足可控和无限两个条件。慢车道公式的两个变量——工作时间上限24小时/天、投资收益率受市场制约——既不可控也有限度。
  V1_cross_domain:
    passed: true
    evidence:
      - 第12章: 首次提出慢车道财富公式并拆解其变量不可控、有限
      - 第15章: 慢车道的7个风险作为该推理方法的具体后果展开
  V2_predictive_power:
    passed: true
    novel_question: 一个靠出租多套房产收租的包租公，他的财富公式是否也存在不可控的有限平衡问题？
    derived_answer: 是的。其财富公式为财富=租金收入x房产数量，租金收入受市场行情制约（不可控），房产数量受资金和贷款额度制约（有限）。一旦房产市场下跌或空置率上升，收入骤降。
  V3_exclusivity:
    passed: true
    why_not_common: 大多数理财建议只告诉你存钱投资而不分析其数学结构。作者用数学公式拆解加变量可控性分析的方法批判慢车道，这种用数学解剖财富策略的思维工具是独特的。
  tags: [数学推理, 慢车道批判, 公式拆解, 变量分析, 核心]

- id: v03
  title: 可控的无限平衡（快车道数学优势）
  type: reasoning_method
  source_chapter: 18
  source_quote: |
    快车道财富公式的关键是要有一个很高的限速，或者无限制的价值范围。这将创造杠杆。而你的产品或服务所在的市场决定了你的上限。
  summary: |
    与慢车道相反的快车道数学框架。快车道公式（财富=净利润+资产价值）中的变量——净利润=销售数量x利润率——同时具有可控性和无限性。资产价值=净利润x行业乘数，乘数通常为2-17倍，每增加1美元净利润可产生数倍的资产增值。
  V1_cross_domain:
    passed: true
    evidence:
      - 第18章: 提出快车道财富公式和可控的无限平衡概念
      - 第29章: 5条戒律中的规模戒律和时间戒律都是该框架的推论
      - 第35章: 三条高速快车道选择框架也是基于此数学优势
  V2_predictive_power:
    passed: true
    novel_question: 一个SaaS创业者，月利润从1万美元增长到5万美元，他的公司估值变化了多少？
    derived_answer: 假设SaaS行业乘数为6-10倍，月利润5万美元即年利润60万美元，公司估值在360万-600万美元之间。利润增长5倍但估值增长30-50倍，解释了为什么快车道创业者的账面财富增长比利润增长快得多。
  V3_exclusivity:
    passed: true
    why_not_common: 普通人知道赚钱和公司值钱是两回事，但很少用净利润x行业乘数这个公式量化理解其杠杆效应。作者将估值公式简化为可操作的思维工具，指出每赚1美元=资产增值数倍这一反直觉杠杆。
  tags: [数学推理, 快车道论证, 公式拆解, 杠杆效应, 核心]

- id: v04
  title: 5条戒律（NEEDS）检查框架
  type: decision_framework
  source_chapter: 29, 30, 31, 32, 33, 34
  source_quote: |
    用影响力定律照亮你的快车道，用5条快车道戒律做个检查。需求戒律、进入戒律、控制戒律、规模戒律、时间戒律。5条快车道戒律是快车道的试金石，可以用来验证你选择的道路。
  summary: |
    一个结构化决策框架，用于评估一个生意是否具有快车道潜力。包含5个维度的检查：N（需求戒律）——生意是否解决真实需求；E（进入戒律）——是否有进入壁垒；C（控制戒律）——是否掌握业务核心控制权；S（规模戒律）——是否有规模扩展潜力；T（时间戒律）——是否与个人时间脱钩。
  V1_cross_domain:
    passed: true
    evidence:
      - 第29章: 首次引入5条戒律作为统一框架
      - 第30-34章: 分别展开每条戒律的详细论证和案例
      - 第35章: 三条高速快车道选择框架以5条戒律为评估标准
  V2_predictive_power:
    passed: true
    novel_question: 一个AI绘画自媒体账号（在小红书接广告变现）是否符合快车道标准？
    derived_answer: 需求戒律（通过）、进入戒律（不通过——壁垒极低）、控制戒律（不通过——依赖平台算法）、规模戒律（部分通过——广告模式天花板低）、时间戒律（不通过——需持续更新）。通过2/5，属于兼职收入而非快车道业务。
  V3_exclusivity:
    passed: true
    why_not_common: 大多数创业评估框架关注市场规模、竞争分析等传统维度。作者用5个高度浓缩的问题从快车道数学原理推导出的一套检查清单，每个问题都直接关联到财富公式的变量可控性和无限性。
  tags: [决策框架, 生意评估, 快车道验证, 检查清单, 核心]

- id: v05
  title: 生产者vs消费者思维转换框架
  type: thinking_model
  source_chapter: 17, 32, 36
  source_quote: |
    要将生活的焦点重新聚焦生产，而不是消费。当你重新将你的思维从多数人（消费者）调整到少数人（生产者）的思维，你才能有效地转换团队和忠诚度。
  summary: |
    一个认知转换模型：将世界分为生产者（少数人、创造者、富人）和消费者（大多数人、消耗者、穷人）。要致富必须从消费者的思维方式切换为生产者的思维方式——从购买产品转为销售产品，从找工作转为提供工作。
  V1_cross_domain:
    passed: true
    evidence:
      - 第17章: 提出生产者vs消费者的核心区分
      - 第32章: 搭便车者vs驾驶者的区分是该框架的延伸
      - 第36章: 机会发现（抱怨到需求转换）是生产者思维的具体应用
  V2_predictive_power:
    passed: true
    novel_question: 一个经常在知乎上回答专业问题的人，如何用生产者/消费者框架评估自己的行为？
    derived_answer: 纯粹的免费回答是消费者行为（消耗时间、不产生收入、为平台创造内容）。转为生产者行为：将高质量回答集结成付费电子书、开设付费专栏或咨询、建立专业社群。
  V3_exclusivity:
    passed: true
    why_not_common: 虽然做生产者而不是消费者听起来像常识，但作者将其具体化为一系列可操作的二元对照（卖vs买、提供工作vs找工作、收息vs付息），并且与财富公式的数学原理挂钩。
  tags: [认知转换, 思维模型, 生产者心态, 定位, 核心]

- id: v06
  title: 影响力定律
  type: thinking_model
  source_chapter: 21, 33
  source_quote: |
    影响力定律是说，不管在规模上还是在数量上，你在一个实体中影响的人越多，你获取的财富就越多。简单说就是，影响百万人就能赚到百万美元。
  summary: |
    一个绝对的财富定律：你影响的人数（规模）或影响的深度（等级）决定了你的财富数额。规模是指销售数量，等级是指单位利润。规模+等级结合则产生亿万财富。
  V1_cross_domain:
    passed: true
    evidence:
      - 第21章: 首次提出影响力定律，以数学方式论证
      - 第33章: 规模戒律是影响力定律的直接应用
  V2_predictive_power:
    passed: true
    novel_question: 一个知识付费博主，年收入50万，课程售价199元，如何用影响力定律分析他的增长瓶颈？
    derived_answer: 他的规模约2500名学员，远未达到百万人级别。要突破50万年收入，要么扩大规模到25万人，要么提高等级到19900元的高端咨询。两条路需要完全不同的策略。
  V3_exclusivity:
    passed: true
    why_not_common: 大多数人说要赚钱就要帮助更多人，但作者将这一直觉量化成数学关系（影响百万人=百万美元），并拆解为规模x等级两个维度，使其可分析、可计算。
  tags: [财富定律, 规模, 等级, 商业评估, 核心]

- id: v07
  title: 需求戒律——解决需求而非满足自我
  type: principle
  source_chapter: 30, 36, 40
  source_quote: |
    停止从你自私的愿望、角度想问题，不管想的是金钱、梦想，还是你喜欢的事情。相反，寻找需求、问题、痛点、服务缺陷和情绪。
  summary: |
    生意的唯一目的是解决别人的问题，而不是满足你自己的愿望。90%的新业务在5年内失败，因为它们建立在自私的内部需求基础上。先给予，再索取。
  V1_cross_domain:
    passed: true
    evidence:
      - 第30章: 需求戒律作为5条戒律的第一条，详细论证
      - 第36章: 机会发现方法论——从抱怨中识别需求
      - 第40章: 抱怨分类框架中，无效投诉暴露未满足需求
  V2_predictive_power:
    passed: true
    novel_question: 某公司想开发一款AI宠物翻译器，用需求戒律评估。
    derived_answer: 典型的需求戒律违反案例。宠物主人真正的痛点是宠物健康监测、行为问题解决、走失找回，而不是知道猫在说什么。产品满足猎奇心，非真实痛点。
  V3_exclusivity:
    passed: true
    why_not_common: 大多数创业建议说做你热爱的事或找到蓝海市场。作者将需求戒律提升为创业的第一原则，指出90%的失败源于从自我出发而非市场需求。先给予再索取的反直觉顺序是独特洞察。
  tags: [NEEDS戒律, 需求, 创业核心, 核心]

- id: v08
  title: 进入戒律——低壁垒等于拥堵赛道
  type: principle
  source_chapter: 31
  source_quote: |
    "低进入壁垒的生意不是一条可依赖的道路，因为容易进入导致了竞争激烈和堵塞。"
  summary: |
    避免做人人都能10分钟内开始的生意。高进入壁垒意味着竞争小、利润高。
  V1_cross_domain:
    passed: true
    evidence:
      - 第31章: 进入戒律的正式提出和论证
      - 第31章（不同段落）: 大家都在做反向指标
      - 第36章: 不要因为有人在做就放弃原则
  V2_predictive_power:
    passed: true
    novel_question: 2025年大量创业者涌入AI大模型赛道，用进入戒律分析。
    derived_answer: 底层（训练基础模型）壁垒极高——符合；上层（AI应用）壁垒极低——违反。
  V3_exclusivity:
    passed: true
    why_not_common: 提炼为可操作戒律并与大家都在做反向指标联系。
  tags: [NEEDS戒律, 进入壁垒, 竞争, 核心]

- id: v09
  title: 控制戒律——自己驾驶，不要搭便车
  type: principle
  source_chapter: 32
  source_quote: |
    "如果你不是在快车道上驾车，那么你便坐在乘客位上，由其他人掌控方向盘。"
  summary: |
    控制你的财务计划。搭便车者把控制权让给了别人，赚到的只是零头。
  V1_cross_domain:
    passed: true
    evidence:
      - 第32章: 控制戒律的正式提出
      - 第32章（不同段落）: 谷歌AdSense被终止的亲身经历
      - 第19章: 连锁加盟陷阱
  V2_predictive_power:
    passed: true
    novel_question: 抖音带货达人，用控制戒律分析他的生意风险。
    derived_answer: 严重违反控制戒律。依赖平台算法和政策，收入可能一夜归零。需建立私域。
  V3_exclusivity:
    passed: true
    why_not_common: 将控制权提升为财富公式核心变量，指出控制权缺失是搭便车者本质特征。
  tags: [NEEDS戒律, 控制, 搭便车, 核心]

- id: v10
  title: 规模戒律——规模决定财富天花板
  type: principle
  source_chapter: 33
  source_quote: |
    "在当地或者一个只能容纳少部分人的水池里很难找到规模。"
  summary: |
    生意的规模决定财富天花板。本地小店服务几百人，互联网公司服务全球。
  V1_cross_domain:
    passed: true
    evidence:
      - 第33章: 规模戒律的正式提出
      - 第21章: 影响力定律是理论基础
      - 第35章: 三条高速快车道的选择以规模潜力为标准
  V2_predictive_power:
    passed: true
    novel_question: 手工艺人做定制木雕每件2000元月产20件，用规模戒律评估天花板。
    derived_answer: 年收入48万。突破：等级路线（提价到2万）或规模路线（数字化批量生产）。
  V3_exclusivity:
    passed: true
    why_not_common: 与影响力定律和财富公式严格挂钩，从模糊的做大变成可计算的数学关系。
  tags: [NEEDS戒律, 规模, 杠杆, 核心]# TEST APPEND

- id: v11
  title: 时间戒律
  type: principle
  source_chapter: 34, 19
  source_quote: |
    "时间戒律要求你的生意与你的时间脱钩。"
  summary: |
    你的业务系统应该替你做时间交易。
  V1_cross_domain:
    passed: true
    evidence:
      - 第34章: 时间戒律
      - 第19章: 摇钱树五种苗
      - 第10章: 5对2时间交易分析
  V2_predictive_power:
    passed: true
    novel_question: 独立开发者做月入5000美元SaaS但需每天处理客服，算快车道吗？
    derived_answer: 部分满足。需标准化客服、雇佣助理。
  V3_exclusivity:
    passed: true
    why_not_common: 操作化为可检验的戒律：你不在场时生意还能运转吗？
  tags: [NEEDS戒律, 时间, 被动收入, 摇钱树, 核心]

- id: v12
  title: 时间资产化
  type: reasoning_method
  source_chapter: 26, 10, 34
  source_quote: |
    "时间是生命的油箱。时间是你拥有的最伟大的资产。"
  summary: |
    时间是稀缺不可再生的，金钱充裕可再生。不要为省钱浪费时间。
  V1_cross_domain:
    passed: true
    evidence:
      - 第26章: 时间是终极资产
      - 第10章: 5对2时间交易分析
      - 第34章: 时间戒律
  V2_predictive_power:
    passed: true
    novel_question: 自由职业者每小时收费500元，花3小时比较电商平台省200元，合理吗？
    derived_answer: 不合理。3小时机会成本1500元，为省200元净亏1300元。
  V3_exclusivity:
    passed: true
    why_not_common: 将时间定义为生命的油箱，给出具体估值方法和投资方向。
  tags: [时间管理, 系统思维, 被动收入, 自由, 核心]

- id: v13
  title: 寄生性债务识别与清除
  type: thinking_model
  source_chapter: 26, 7
  source_quote: |
    "寄生性债务是条贪吃蛇，吞噬你的自由时间。"
  summary: |
    用时间成本重新定义债务。寄生性债务指任何迫使你去工作的债务。
  V1_cross_domain:
    passed: true
    evidence:
      - 第26章: 定义和时间成本分析法
      - 第7章: 生活方式奴役
      - 第13章: 教育奴役案例
  V2_predictive_power:
    passed: true
    novel_question: 刚毕业大学生月薪1万，考虑贷款20万买车，用框架分析。
    derived_answer: 时薪约57元，20万车贷=3500小时自由时间。
  V3_exclusivity:
    passed: true
    why_not_common: 引入时间成本维度——债务真实代价不是利息而是被吞噬的自由时间。
  tags: [债务分析, 时间成本, 消费决策, 自由, 核心]

- id: v14
  title: 兴趣vs承诺（红线原则）
  type: thinking_model
  source_chapter: 28, 9
  source_quote: |
    "读一本书是兴趣，而经常运用书中学到的知识则是承担责任。"
  summary: |
    兴趣（第一挡）是浅层参与。承诺（红线）是全力投入、承担责任。
  V1_cross_domain:
    passed: true
    evidence:
      - 第28章: 红线原则
      - 第9章: 承担责任
      - 第14章: 实践悖论
  V2_predictive_power:
    passed: true
    novel_question: 花2万买创业课程但从不启动项目，属于兴趣还是承诺？
    derived_answer: 纯兴趣。真正承诺是注册公司、做出原型、获取客户。
  V3_exclusivity:
    passed: true
    why_not_common: 用赛车红线比喻将区分形象化、可操作化。
  tags: [自我诊断, 承诺, 行动力, 红线, 核心]

- id: v15
  title: 执行vs点子乘法效应
  type: thinking_model
  source_chapter: 38, 39
  source_quote: |
    "点子只是乘数，执行才会带来真正的财富。"
  summary: |
    最终价值=点子价值x执行价值。点子1.6-320，执行1-10000000。
  V1_cross_domain:
    passed: true
    evidence:
      - 第38章: 提出乘法效应
      - 第39章: 世界对执行做出反馈
      - 第44章: 聚焦原则
  V2_predictive_power:
    passed: true
    novel_question: 一个花6个月写计划书未启动，另一个3周做出MVP获100用户。
    derived_answer: 第一个80x2=160。第二个10x100000=1000000。差6250倍。
  V3_exclusivity:
    passed: true
    why_not_common: 量化为乘法公式并给出具体数字，变成可计算可记忆的思维工具。
  tags: [执行, 创意, 乘法效应, 创业思维, 核心]

# test append

- id: v16
  title: 明智风险vs无谓风险辨别框架
  type: decision_framework
  source_chapter: 28
  source_quote: |
    "明智风险——下行有限且上行无限。无谓风险——下行无限且上行有限。"
  summary: |
    明智风险——下行有限且上行无限。无谓风险——下行无限且上行有限。
  V1_cross_domain:
    passed: true
    evidence:
      - 第28章: 正式提出区分
      - 第15章: 慢车道7个危险
      - 第19章: 连锁加盟陷阱
  V2_predictive_power:
    passed: true
    novel_question: 年薪50万程序员，选A)全职AI创业；B)加杠杆买800万房子。
    derived_answer: A)明智风险——下行有限可回原行业，上行无限。B)无谓风险——下行无限。
  V3_exclusivity:
    passed: true
    why_not_common: 反转常识——看似安全的慢车道可能隐藏无限下行风险。
  tags: [风险分析, 决策框架, 创业评估, 理性决策]

- id: v17
  title: 实践悖论识别框架
  type: thinking_model
  source_chapter: 14
  source_quote: |
    "有人倡导赚钱的策略，但这种策略并不会让他自己发财致富。"
  summary: |
    理财大师兜售慢车道策略但自己靠写书、演讲致富——快车道生意。
  V1_cross_domain:
    passed: true
    evidence:
      - 第14章: 实践悖论概念
      - 第32章: 投资自己的品牌
      - 第27章: 研讨会骗局
  V2_predictive_power:
    passed: true
    novel_question: 抖音博主教人定投指数基金但收入来自带货理财课程，用框架分析。
    derived_answer: 符合实践悖论。教的（定投）和做的（做内容——快车道）不一致。
  V3_exclusivity:
    passed: true
    why_not_common: 提炼为可操作的问题：他用他教的方法致富了吗？
  tags: [批判思维, 建议评估, 大师识别, 可信度, 核心]

- id: v18
  title: 财富三位一体模型
  type: thinking_model
  source_chapter: 6, 7
  source_quote: |
    "财富不是由物质财产成就的，而是由家庭、健康和自由组成。"
  summary: |
    真正财富由家庭/人际关系、健康、自由三个要素构成。
  V1_cross_domain:
    passed: true
    evidence:
      - 第6章: 提出模型
      - 第7章: 生活方式奴役案例
      - 第10章: 5对2时间交易分析
  V2_predictive_power:
    passed: true
    novel_question: 获年薪200万但需每周80小时、月出差3周，用模型评估。
    derived_answer: 增强金钱但破坏健康、家庭、自由。比年薪50万朝九晚五更贫穷。
  V3_exclusivity:
    passed: true
    why_not_common: 结构化为三要素模型并与快车道挂钩。
  tags: [财富定义, 价值观, 幸福模型, 生活评估]

- id: v19
  title: 抱怨是金矿
  type: reasoning_method
  source_chapter: 36, 40
  source_quote: |
    "机会用可以预见的词句表明自己的存在。"
  summary: |
    从日常抱怨中发现商业需求。反向推导就是未满足的需求。
  V1_cross_domain:
    passed: true
    evidence:
      - 第36章: 机会发现
      - 第40章: 客户抱怨四分类
      - 第30章: 需求戒律
  V2_predictive_power:
    passed: true
    novel_question: 在社交媒体搜索我讨厌XX相关帖子能发现什么商业机会？
    derived_answer: 我讨厌找停车位——停车场预约APP。我讨厌整理发票报销——企业智能报销SaaS。
  V3_exclusivity:
    passed: true
    why_not_common: 操作化为具体词汇信号清单，即学即用的需求发现工具。
  tags: [需求发现, 机会识别, 推理方法, 抱怨分析]
- id: v20
  title: 大家都在做反向指标框架
  type: reasoning_method
  source_chapter: 31, 15
  source_quote: |
    "如果每个人都去做同样的事情，肯定会失败。"
  summary: |
    大家都在做=拥堵赛道=利润微薄=即将崩溃。
  V1_cross_domain:
    passed: true
    evidence:
      - 第31章: 反向指标
      - 第15章: 慢车道经济风险
      - 第31章: 进入戒律
  V2_predictive_power:
    passed: true
    novel_question: 2025年人人讨论AI创业，亲戚问怎么用AI赚钱。用框架分析。
    derived_answer: 典型的大家都在做信号。赚钱的是卖铲子的人。
  V3_exclusivity:
    passed: true
    why_not_common: 与进入戒律挂钩的商业机会评估方法。
  tags: [反向指标, 从众心理, 投资决策, 赛道选择]
- id: v21
  title: 客户抱怨四分类处理框架
  type: decision_framework
  source_chapter: 40
  source_quote: |
    "抱怨有4类：变化、期望、无效投诉、欺诈投诉。"
  summary: |
    1)变化类；2)期望类；3)无效投诉；4)欺诈类。
  V1_cross_domain:
    passed: true
    evidence:
      - 第40章: 抱怨四分类
      - 第36章: 机会发现
      - 第40章: 超越预期的客户服务
  V2_predictive_power:
    passed: true
    novel_question: SaaS更新UI后收到大量投诉新版太难用了，用框架分析。
    derived_answer: 对变化抵触（变化类）应坚持。找不到功能（期望类）优化导航。
  V3_exclusivity:
    passed: true
    why_not_common: 提供分类系统判断哪些投诉值得深入。
  tags: [客户服务, 投诉处理, 反馈分析, 需求发现]
- id: v22
  title: 5对2时间交易分析框架
  type: reasoning_method
  source_chapter: 10
  source_quote: |
    "5对2的投资回报率是-60%。"
  summary: |
    每周5天受约束时间换2天自由时间，回报率-60%。
  V1_cross_domain:
    passed: true
    evidence:
      - 第10章: 5对2分析
      - 第26章: 寄生性债务
      - 第34章: 时间戒律
  V2_predictive_power:
    passed: true
    novel_question: 创业者每天工作14小时经营店铺，用5对2框架分析。
    derived_answer: 7对0交易。花时间搭建系统可变成0对7。
  V3_exclusivity:
    passed: true
    why_not_common: 很少有人将工作时间投入计算为投资回报率。-60%是反直觉视角。
  tags: [时间分析, 投资回报, 工作评估, 生活方式]
- id: v23
  title: 摇钱树五种苗分类框架
  type: thinking_model
  source_chapter: 19, 34
  source_quote: |
    "有5种生意的苗木可以成长为摇钱树。"
  summary: |
    1)租赁系统（A）；2)计算机/软件系统（A-）；3)内容系统（B+）；4)分销系统（B）；5)人力资源系统（C）。
  V1_cross_domain:
    passed: true
    evidence:
      - 第19章: 摇钱树分类
      - 第34章: 时间戒律
      - 第35章: 三条高速快车道
  V2_predictive_power:
    passed: true
    novel_question: 在线教育创业者自己录课并亲自答疑，如何提升被动等级？
    derived_answer: 目前内容（B+）和人力（C）混合。提升：录播FAQ替代直播答疑。
  V3_exclusivity:
    passed: true
    why_not_common: 按被动收入潜力（A到C级）分类，从时间自由角度选择业务类型。
  tags: [业务分类, 被动收入, 系统设计, 商业模式]
- id: v24
  title: 利润变量控制框架
  type: thinking_model
  source_chapter: 18
  source_quote: |
    "通过增加转化率提高销售数量。1%的提升带来每天480美元利润。"
  summary: |
    利润=销售数量x利润率。三种控制方式：提高转化率、增加流量、提高利润率。
  V1_cross_domain:
    passed: true
    evidence:
      - 第18章: 利润变量控制
      - 第18章: 资产价值乘法器
      - 第33章: 规模戒律
  V2_predictive_power:
    passed: true
    novel_question: 月收入10万电商店，转化率2%，客单价200元，月流量2.5万。如何翻倍？
    derived_answer: 组合策略：转化率2%到3%（+50%），流量2.5万到3.3万（+33%），客单价200到240元（+20%），组合=2.4倍。
  V3_exclusivity:
    passed: true
    why_not_common: 简化为三个可操纵变量，强调乘法效应。
  tags: [利润控制, 增长策略, 运营框架, 乘法效应]
- id: v25
  title: 三条高速快车道选择框架
  type: decision_framework
  source_chapter: 35
  source_quote: |
    "3条高速快车道：互联网生意、创新产品或服务、创造规模效应。"
  summary: |
    1)互联网生意；2)创新产品或服务；3)创造规模效应。
  V1_cross_domain:
    passed: true
    evidence:
      - 第35章: 三条高速快车道
      - 第29章: 5条戒律
      - 第19章: 摇钱树
  V2_predictive_power:
    passed: true
    novel_question: 有餐饮管理经验但不懂编程的人如何选择快车道方向？
    derived_answer: 最匹配规模效应——成功餐饮模式通过连锁/加盟复制。
  V3_exclusivity:
    passed: true
    why_not_common: 给出三条具体可验证的高速路，每条与5条戒律严格对齐。
  tags: [创业路径, 快车道, 选择框架, 商业模式]
## 通过的反例（作为B段素材保留）

以下反例本身不独立成skill，但因其对已验证技能有直接支撑价值，保留在此作为B段素材。

- id: ce01
  title: 慢车道的数学骗局
  bound_to: [v02, v03]
  bound_as: B段素材

- id: ce04
  title: 实践悖论
  bound_to: [v17]
  bound_as: B段素材

- id: ce05
  title: 寄生性债务陷阱
  bound_to: [v13]
  bound_as: B段素材

- id: ce07
  title: 网络营销的幻觉
  bound_to: [v09]
  bound_as: B段素材

- id: ce08
  title: 连锁加盟陷阱
  bound_to: [v09, v11]
  bound_as: B段素材

- id: ce09
  title: 从众陷阱
  bound_to: [v08, v20]
  bound_as: B段素材

- id: ce12
  title: 搭便车者风险
  bound_to: [v09]
  bound_as: B段素材

- id: ce13
  title: 把兴趣当成承诺
  bound_to: [v14]
  bound_as: B段素材

- id: ce17
  title: 生活方式奴役
  bound_to: [v18]
  bound_as: B段素材

- id: ce18
  title: 复利神话
  bound_to: [v02]
  bound_as: B段素材

- id: ce19
  title: 注意力分散
  bound_to: [v15]
  bound_as: B段素材