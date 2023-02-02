account_map = {
    "assets": {
        "/": "Assets:Unknown",
        "余额宝": "Assets:Alipay:YuEBao",
        "余利宝": "Assets:Alipay:YuLiBao",
        "余额": "Assets:Alipay:YuE",
        "零钱通": "Assets:Wechat:LingQianTong",
        "零钱": "Assets:Wechat:LingQian",
        "工商银行(6086)|工商银行|中国工商银行|中国工商银行储蓄卡(6086)|工商银行(9687)": "Assets:ICBC",
        "招商银行(4481)|招商银行储蓄卡(4481)": "Assets:CMB",
        "民生银行(9564)|中国民生银行储蓄卡(9564)": "Assets:MSB",
        "中国农业银行储蓄卡(2970)|中国农业银行|(2970)|农业银行|农业银行(2970)": "Assets:CAB",
        "中国建设银行|中国建设银行储蓄卡(0475)": "Assets:CCB",
        "广发银行": "Assets:GDB",
        "网商银行储蓄卡(0763)": "Assets:MYbank",
        "北京银行储蓄卡(4991)": "Assets:BCB",
        "交通银行储蓄卡(8186)": "Assets:BOCOM",
    },
    "liabilities": {
        "招商银行(5250)|招商银行(1787)|招商银行|招商银行信用卡(5250)": "Liabilities:CreditCard:CMB",
        "广发银行信用卡(4537)": "Liabilities:CreditCard:GDB",
        "花呗|花呗分期|花呗分期(6期)": "Liabilities:Alipay:HuaBai",
    },
    "expenses": {
        # 居家
        "中国电信|中国移动|中国联通": "Expenses:Home:Phone",  # 手机话费
        "房贷": "Expenses:Home:Mortgage:Loan",  # 房贷
        "水费|电费|燃气费": "Expenses:Home:SDRQ",  # 水电燃气
        "物业": "Expenses:Home:WYF",  # 物业费
        "快递|顺丰|速运|中通|快件|寄件费|菜鸟|中国邮政": "Expenses:Home:Delivery",  # 快递费
        "理发|美发": "Expenses:Home:Haircut",  # 理发费
        "漏记款": "Expenses:Home:Omission",  # 漏记款
        "窗帘": "Expenses:Home:Fix", # 装修

        # 餐饮
        "武圣|西餐|饭|餐厅|饭店|必胜客|餐饮|弄堂里|外婆家|吉野家": "Expenses:Food:Dine",
        "水果": "Expenses:Food:DrinkFruit",  # 饮料水果
        "盒马|叮咚买菜": "Expenses:Food:Vegetables",  # 买菜原料
        "联华|十足|全家|超市|711|罗森|友宝|喜士多|富华门市|智能货柜|便利店": "Expenses:Food:Snacks",
        "饿了么|美团|外卖": "Expenses:Food:Delivery",  # 外卖
        "面包|牛奶|酸奶": "Expenses:Food:BreadMilk",  # 面包店
        "星巴克|COSTA|咖啡厅|喜茶": "Expenses:Food:Starbucks",  # 咖啡

        # 医疗健康
        "医院|挂号|门诊": "Expenses:Health:Medical ",  # 门诊&药品

        # 娱乐
        "电影": "Expenses:Entertainment:Movie ",  # 电影
        "旅游": "Expenses:Entertainment:Travel ",  # 旅游度假
        "酒店": "Expenses:Entertainment:Hotel ",  # 酒店住宿

        # 交通
        "国航|南航|东航|中国国家航空|南方航空|东方航空|航空": "Expenses:Transport:Airline",  # 飞机
        "12306|火车票": "Expenses:Transport:Railway",  # 火车
        "公交|北京一卡通": "Expenses:Transport:GongJiao",  # 公交车
        "高速|通行费": "Expenses:Transport:Gaosu",  # 高速过路费
        "地铁": "Expenses:Transport:Subway",  # 高速过路费
        "单车|骑行": "Expenses:Transport:Danche",  # 单车
        "洗车": "Expenses:Transport:WashCar",  # 洗车
        "打车|滴滴出行|曹操|高德打车|代驾|专车|智慧出行": "Expenses:Transport:TAXI",  # 打车
        "中石油|中石化|石化|石油|浙石油|中国石化|中国石油|中化|加油": "Expenses:Transport:Car:Oil",  # 加油
        "4S店": "Expenses:Transport:Car:Maintenance",  # 保养维修
        "平安保险|人保|太保": "Expenses:Transport:Car:Insurance",  # 车险
        "停车|临时车缴费|停车费|浙A|统一公共支付平台": "Expenses:Transport:Car:Parking",  # 停车费
        "河北省公安厅交通警察总队": "Expenses:Transport:Car:Penalty", # 罚款

        # 购物
        "鞋|衣服|银泰|天街|屈臣氏|印象城|袜子|内裤|pay|NIKE|李宁|迪卡侬|优衣库|GAP|gxg": "Expenses:Shopping:Clothing ",  # 服饰鞋包
        "Apple Store|玩客云|大疆|树莓派|U盘|显卡|小米|ATX电源|迅雷|iCloud|iSlide|switch|App Store|applestore|BandwagonHost|域名|网卡|服务器|硬盘|NAS|内存|路由器|airpods|macbook|Mac|iPhone|iphone|苹果电子产品|SEIKO精工|手表维修": "Expenses:Shopping:Digital ",

        # 电子数码
        "面包机|高压锅": "Expenses:Shopping:Home ",  # 家居百货
        "茅台|红酒|葡萄酒": "Expenses:Shopping:Wine ",  # 酒
        "当当|书|中信出版": "Expenses:Shopping:Book ",  # 买书
        "化妆品": "Expenses:Shopping:Makeup ",  # 化妆护肤
        "充电宝|充电": "Expenses:Shopping:ChongDianBao ",  # 充电宝充电
        "淘宝|京东|拼多多|旗舰店|月饼|考拉|专营店": "Expenses:Shopping:DianShang ",  # 电商
        "商品|商户单号|商户订单|订单号|订单编号": "Expenses:Shopping:ShangPin ",  # 商品

        # 人情
        "礼物": "Expenses:Relationship:Gift",  # 礼物
        "礼金": "Expenses:Relationship:Relative",  # 礼金
        "孝敬": "Expenses:Relationship:FilialPiety",  # 孝敬
        "红包|转账": "Expenses:Relationship:RedEnvelope",  # 转账&红包
        "收钱码收款": "Expenses:Relationship:ShouQianMa",  # 收钱码收款

        # 经营
        "阿里云": "Expenses:Business:CloudServer", # 云服务器
        "域名": "Expenses:Business:Domain", # 云服务器

    },
    "income": {
        "余额宝": "Income:MoneyFund:Alipay:YuEBao",
        "转账": "Income:TransferIn",
        "退款": "Income:Refund",
    },
    "equity": {
        "DEFAULT": "Equity:Opening-Balances"
    }
}

trace_change_map = {
    "goods=收益发放": "income_and_expenses=收入",
    "goods=转账收款到余额宝": "income_and_expenses=调拨",
    "trace_type=零钱充值": "income_and_expenses=调拨",
    "trace_type=转入零钱通-来自零钱": "income_and_expenses=调拨",
    "trace_type=还款": "income_and_expenses=调拨",
    "goods=还款": "income_and_expenses=调拨",
    "goods=快的打车红包": "pay_way=余额,income_and_expenses=收入",
    "trace_type=提现": "income_and_expenses=调拨",
    "goods=提现": "income_and_expenses=调拨",
    "trace_type=零钱通转出-到零钱": "income_and_expenses=调拨",
    "trace_type=零钱通转出-到工商银行(6086)": "income_and_expenses=调拨",
    "goods=退款": "income_and_expenses=收入",
    "goods=余额宝-转出": "income_and_expenses=调拨",
    "goods=支付宝转入到余利宝": "income_and_expenses=调拨",
    "goods=余利宝-转出到银行卡": "pay_way=余利宝,income_and_expenses=调拨",
    "goods=余利宝-银行卡转入": "income_and_expenses=调拨",
    "goods=余利宝转出": "pay_way=余利宝,income_and_expenses=调拨",
    "trace_obj=网商银行&goods=账户结息": "pay_way=余利宝,income_and_expenses=收入",
    "goods=充值-普通充值": "income_and_expenses=调拨",
    "goods=理财赎回": "pay_way=余额宝,income_and_expenses=调拨",
    "goods=余额宝-单次转入": "income_and_expenses=调拨",
    "goods=余额宝-自动转入": "income_and_expenses=调拨",
    "goods=北京市12123交通罚没": "income_and_expenses=支出",
    "goods=理财买入": "income_and_expenses=调拨",
    "goods=收到支付宝五福的红包": "pay_way=余额",
    "goods=天天领现金活动每日红包": "pay_way=余额",
    "goods=七彩虹GTX970": "pay_way=余额",
    "trace_obj=北京一卡通&goods=转账": "pay_way=余额",
    "trace_obj=*军&goods=商品": "pay_way=余额",
    "goods=转账到银行卡": "income_and_expenses=调拨",
    "goods=转出到网商银行": "income_and_expenses=调拨",
    "goods=转出到余额": "income_and_expenses=调拨,pay_way=余额",
    "goods=定期理财-": "income_and_expenses=调拨",
    "goods=红包奖励发放": "income_and_expenses=收入,pay_way=余额宝",
    "goods=买入": "income_and_expenses=调拨",
    "goods=卖出至余额宝": "income_and_expenses=调拨",
    "goods=借呗放款至余额": "income_and_expenses=调拨",
    "goods=卖出至银行卡": "income_and_expenses=调拨",
    "goods=收钱码收款": "pay_way=余额",
    "goods=卢娇艳": "income_and_expenses=调拨",
    "goods=哈哈୧(๑•̀⌄•́๑)૭": "income_and_expenses=调拨",
    "trace_obj=卢娇艳": "income_and_expenses=调拨",
    "trace_obj=哈哈୧(๑•̀⌄•́๑)૭": "income_and_expenses=调拨",
}
