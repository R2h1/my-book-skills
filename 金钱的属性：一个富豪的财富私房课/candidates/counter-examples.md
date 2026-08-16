# 候选反例池 — 《金钱的属性：一个富豪的财富私房课》
> 阶段 1 反例提取器产出（由主流程补写）。供阶段 2 B 段使用。

- id: ce01
  title: 急功近利（想尽快变成富人）
  type: counter-example
  source_chapter: 要想成为富人，绝不能急功近利
  source_quote: |
    "想要成为富人的人最常犯的错误，就是总是一门心思想尽快成为富人。一旦产生想要尽快
    成为富人的野心，就很难做出正确的判断，容易上当受骗。"
  failure_mode: |
    把"尽快致富"当作目标，导致被高收益诱惑、忽视风险、感情用事投资、加杠杆，
    最终失败；运气好一时成功者也携带着必然失败的条件。
  mechanism: |
    急切心态本质是攀比与炫耀，剥夺了理性判断所需的耐心；越急越容易把"运气"当成
    "能力"。
  warning_signs:
    - 总想"一两年暴富"
    - 被高收益项目吸引时心跳加速
    - 没耐心学习基础
  bound_to:
    - "慢变富"
    - "复利双刃剑"
  tags: [counter-example, cognitive-bias, greed]

- id: ce02
  title: 贪婪与泡沫（欲望滋生风险）
  type: counter-example
  source_chapter: 风险最大的时候也是风险最小的时候
  source_quote: |
    "欲望滋生风险。当欲望转移到大众身上时，就会产生所谓的乐观泡沫，泡沫会带来暴跌。"
  failure_mode: |
    在牛市人人贪婪时跟风追高，把"泡沫"当作"趋势"，最终在暴跌中损失惨重。
  mechanism: |
    大众的乐观情绪自我强化，价格脱离价值；作者警告"比恐慌更可怕的是贪婪和泡沫"。
  warning_signs:
    - 身边人都在讨论同一个投资
    - "这次不一样"的论调盛行
    - 价格短期暴涨
  bound_to:
    - "风险最大时风险最小"
    - "远离暴利"
  tags: [counter-example, bubble, greed]

- id: ce03
  title: 随波逐流入市（没有计划、没有学习）
  type: counter-example
  source_chapter: 通过股市赚到钱的人的三个特征
  source_quote: |
    "一听别人说股票市场处于百年不遇的大好时机，就一下子把所有钱都聚拢起来心急火燎、
    冒冒失失地投入进去。……完全没有计划，甚至完全没有学习过相关知识。"
  failure_mode: |
    看到别人赚钱就冲动入市，用全部积蓄甚至借钱/加杠杆炒股，无计划无学习，追涨杀跌，
    最终本金如冰激凌般融化。
  mechanism: |
    把股市当赌场、把"别人的建议"当依据；资金含"急钱"（学费/婚礼）会质变。
  warning_signs:
    - 入市前一个月还没关注过股市
    - 1-2小时内选定股票
    - 用下月要用的钱买入
  bound_to:
    - "投资赢家资格11问"
    - "每分钱的时间属性"
  tags: [counter-example, herd, speculation]

- id: ce04
  title: 用"急钱"投资（结婚/学费/杠杆的钱）
  type: counter-example
  source_chapter: 每分钱都有不同的时间流逝状态
  source_quote: |
    "这些凑起来的钱可能还包含着下个月要交的大学学费或用来筹备明年婚礼的费用，这些费用
    可是要马上派上用场的。有人借钱炒股，甚至还有人加两三倍的杠杆借钱购买股票。"
  failure_mode: |
    拿期限短的急钱（结婚、学费、生活费）去做需要长期等待的投资，或在里面混入杠杆，
    一旦波动就被迫割肉，本金与生活质量双输。
  mechanism: |
    "急钱"没有等待的时间，遇到下跌只能被迫卖出；杠杆则把波动放大到致命。
  warning_signs:
    - 投资的钱几个月内要用
    - 借钱/杠杆入市
    - 跌一点就睡不着
  bound_to:
    - "每分钱的时间属性"
    - "只用5年内用不到的钱投资"
  tags: [counter-example, time-horizon, leverage]

- id: ce05
  title: 滚信用卡/提前花未来的收入
  type: counter-example
  source_chapter: 攒不住钱的原因
  source_quote: |
    "绝对不要提前花费未来的收入。把信用卡剪掉，请使用借记卡。……信用卡公司利用累计
    积分这种手段引导消费者进行不必要的消费。"
  failure_mode: |
    用信用卡预支未来收入、为攒积分多消费，导致消费失控、攒不下钱、复利站到债务一边。
  mechanism: |
    信用卡把"未来收入"提前变成"今天的可支配"，模糊了真实支付能力；积分奖励是
    引导过度消费的诱饵。
  warning_signs:
    - 每月还款还不足账单
    - 为积分而购物
    - 用分期付款买非必需品
  bound_to:
    - "攒钱机制（剪信用卡）"
    - "复利双刃剑"
  tags: [counter-example, consumption, credit-card]

- id: ce06
  title: 炫耀性消费（漂亮的垃圾）
  type: counter-example
  source_chapter: 漂亮的垃圾
  source_quote: |
    "有些东西，即便再漂亮，也是垃圾。垃圾就应该被丢掉或被收走，没理由花着钱被垃圾的
    美丽诱惑。"
  failure_mode: |
    为显得富有而买奢侈品、把家塞满"漂亮却无用"的东西，钱花在不创造资产的地方，
    资产结构被消费侵蚀。
  mechanism: |
    把"消费"当"身份证明"，用物质填补自我存在感的缺失；炫耀性消费永远没有尽头。
  warning_signs:
    - 买前要确认别人是否看得到
    - 家中有大量未拆封/未使用物品
    - 用消费证明自己"配得上"
  bound_to:
    - "漂亮的垃圾（消费诊断）"
    - "攒钱机制"
  tags: [counter-example, consumption, vanity]

- id: ce07
  title: 把赌注押在专家预测上
  type: counter-example
  source_chapter: 经济专家真能预测经济前景吗
  source_quote: |
    "比这些人的言论更可怕的是将赌注押在这些人的意见上并拼上自己全部财产的人。……
    '不知道'才是正确答案。"
  failure_mode: |
    听信专家/名人/电视节目对股价、利率、大盘的预测并据此重仓下注，把别人的意见当
    决策依据。
  mechanism: |
    没有人能准确预测宏观/短期走势；专家只展示说对的，隐藏说错的；"自以为知道其实
    不知道"最危险。
  warning_signs:
    - 问"这只股票会涨吗"
    - 根据电视/抖音大V推荐买入
    - 迷信"股神"预测
  bound_to:
    - "专家与经济预测不可信"
    - "社会权威要心存怀疑"
  tags: [counter-example, authority, prediction]

- id: ce08
  title: 把运气当成实力（自满）
  type: counter-example
  source_chapter: 反复的运气是实力，重复的失败是习惯
  source_quote: |
    "陷入自满的瞬间，对那些具有偶然性的事情就会深信不疑，认为运气就是实力，把推测都
    当作知识。运气是绝对不会重复的。"
  failure_mode: |
    偶尔成功（中奖、抄底成功）后误以为是自己实力，放松学习与纪律，凭"运气"进行
    草率投资，一次错误即全盘皆输。
  mechanism: |
    运气无规则，把运气当实力会停止积累真正的技能；"反复的运气是实力，重复的失败是习惯"。
  warning_signs:
    - 近期连赢后自认"天生会投资"
    - 不再学习、不再谨慎
    - 把推测说得像事实
  bound_to:
    - "慢变富"
    - "大富由天（运气认知）"
  tags: [counter-example, overconfidence, luck]

- id: ce09
  title: 把保险当储蓄
  type: counter-example
  source_chapter: 保险不是储蓄
  source_quote: |
    "购买储蓄型保险的前7年，要从保费中扣除保险代理人的提成等营销费用……在大部分
    情况下，购买保险后的5～6年内的本金都处于赤字水平。"
  failure_mode: |
    把储蓄型/终身/年金等保险当投资或储蓄，被高额销售佣金（约16个月保费）吞噬，
    提前退保拿不回本金，回报甚至低于银行利息。
  mechanism: |
    保险以风险定价，营销费用（GA补贴、代理人提成）被摊进保费；"保险不是储蓄"，
    储蓄型保险的收益结构对客户不利。
  warning_signs:
    - 用"储蓄""理财""养老"话术推销
    - 前几年退保损失大
    - 年缴保费占收入比例过高
  bound_to:
    - "保险不是储蓄"
  tags: [counter-example, insurance, financial-product]

- id: ce10
  title: 对权威无条件信任（深陷阴谋论/不独立思考）
  type: counter-example
  source_chapter: 聪明之人反而容易深陷阴谋论中
  source_quote: |
    "越是聪明高知的人越容易陷入阴谋论中，因为他们对不确定性尤为反感。……陷入阴谋论的
    瞬间也就脱离了常识。"
  failure_mode: |
    高知者因反感不确定性而接受阴谋论/权威论断，放弃独立思考，脱离常识，做出错误投资
    与人生判断。
  mechanism: |
    用"模糊语言+复杂术语"包装的解释比事实更容易被接受；对专家、权威的意见应持
    怀疑而非归顺。
  warning_signs:
    - "你自己知道就行"的内部消息
    - 相信"都是庄家/势力操纵"
    - 用复杂术语掩盖无法验证的断言
  bound_to:
    - "社会权威要心存怀疑"
    - "专家与经济预测不可信"
  tags: [counter-example, conspiracy, thinking]

- id: ce11
  title: 无限再投资/侵占家庭资产（宋老板式）
  type: counter-example
  source_chapter: 对投资一往情深的宋老板和他那总是火冒三丈的妻子
  source_quote: |
    "任何一家公司都不可能把每年收益的100％用来投资。……夫妻享有共同财产……宋老板把
    生意盈利都用于再投资，侵占了妻子的份额。"
  failure_mode: |
    把100%收益全部再投入生意、不给家庭留任何钱，既违反夫妻共同财产原则，也因缺乏
    家庭现金流而埋下隐患。
  mechanism: |
    生意再好，若与家庭资产/现金流完全脱钩，等于"只有赚钱能力没有攒钱/保值能力"，
    四种能力残缺。
  warning_signs:
    - 家里看不到生意的钱
    - 再投资从不停手、不设上限
    - 配偶对财务状况一无所知
  bound_to:
    - "管理金钱的四种能力"
    - "攒钱机制"
  tags: [counter-example, family-finance, reinvestment]

- id: ce12
  title: 不懂价值就接飞刀（把接刀变成赌博）
  type: counter-example
  source_chapter: 能抓住落下的刀的人
  source_quote: |
    "投资原则只有在了解该企业的企业价值时才能够被真正实施。……没有任何一个人能依靠
    收看股市行情节目在投资上获得成功。"
  failure_mode: |
    没有价值判断、没有分批纪律就"抄底"，或依赖技术分析/行情节目预测接刀，把价值
    投资变成赌博。
  mechanism: |
    "接住落下的刀"的前提是懂企业价值；不懂价值的抄底是投机，预测行情者都是
    用包装恐惧的伪专家。
  warning_signs:
    - 抄底前没读过财报
    - 一把梭、不分批
    - 靠行情节目/技术图决定买卖
  bound_to:
    - "接住落下的刀（价值投资）"
    - "专家与经济预测不可信"
  tags: [counter-example, value-investing, speculation]

- id: ce13
  title: 只看总数不看比率（被新闻恐惧绑架）
  type: counter-example
  source_chapter: 通过新闻区分事实和投资信息的方法
  source_quote: |
    "媒体每天都在统计着各国感染者及死亡者人数……大肆煽动着恐惧感。……我关注的不是
    感染总数，而是感染比例。"
  failure_mode: |
    被媒体用总量（感染数、失业数、跌幅）制造的恐惧/狂热绑架，在情绪高点追高、
    低点割肉。
  mechanism: |
    消极/极端信息更吸睛；总量上升不等于趋势恶化，要看比率与边际变化。
  warning_signs:
    - 看到新闻标题就激动
    - 只看绝对数字不看增速/占比
    - 情绪随大盘涨跌剧烈波动
  bound_to:
    - "新闻vs投资信息"
    - "风险最大时风险最小"
  tags: [counter-example, media, bias]

- id: ce14
  title: 只在同一"架子"内分散（假分散）
  type: counter-example
  source_chapter: 鸡蛋没放进一个篮子，为什么还是都碎了
  source_quote: |
    "如果他仅投资不动产……将自己所有的财产都投入了住宅楼、土地、办公室……那么这样的
    投资行为就不能被称为分散投资。因为一旦'架子'坍塌……也会一并倒下。"
  failure_mode: |
    把所有钱押在同一资产大类（全楼市/全股市）里的不同品种，误以为已分散，实际一荣俱荣
    一损俱损。
  mechanism: |
    分散要跨资产大类（存款/债券/股票/房地产/实物），同市场内的多品种只是"同一个架子上
    的多个篮子"。
  warning_signs:
    - 全部资产都是房产
    - 全部资金都在股市
    - 以为"买了很多只股票"就是分散
  bound_to:
    - "篮子vs架子（分散投资）"
  tags: [counter-example, diversification, concentration]

- id: ce15
  title: 轻视小钱（看不起小钱的人管不好大钱）
  type: counter-example
  source_chapter: 攒不住钱的原因
  source_quote: |
    "使用信用卡的人、不操心常丢东西的人、看不起小钱的人、不进行储蓄的人、不了解投资的
    人绝对成不了富人。"
  failure_mode: |
    对小额支出、零钱、物品管理漫不经心，认为"小钱无所谓"，结果消费失控、大钱到来
    也守不住。
  mechanism: |
    小钱是大钱的"嫩芽"；对金钱的态度是统一的，看不起小钱的人对大钱同样随意。
  warning_signs:
    - 常说"就几块钱而已"
    - 东西随手丢、随处放
    - 不记账、不看小账单
  bound_to:
    - "对待他人金钱的态度"
    - "金钱即人"
  tags: [counter-example, small-money, habit]
