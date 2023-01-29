account_map = {
    "assets": {
        "余额宝": "Assets:Alipay:YuEBao",
        "余利宝": "Assets:Alipay:YuLiBao",
        "零钱": "Assets:Wechat:LingQian",
        "零钱通": "Assets:Wechat:LingQianTong",
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

        # 餐饮
        "水果": "Expenses:Food:DrinkFruit",  # 饮料水果
        "盒马|叮咚买菜": "Expenses:Food:Vegetables",  # 买菜原料
        "西餐|饭|餐厅|饭店|必胜客|餐饮|弄堂里|外婆家": "Expenses:Food:Invite",  # 请客吃饭
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
        "公交": "Expenses:Transport:GongJiao",  # 公交车
        "高速|通行费": "Expenses:Transport:Gaosu",  # 高速过路费
        "地铁": "Expenses:Transport:Subway",  # 高速过路费
        "单车|骑行": "Expenses:Transport:Danche",  # 单车
        "洗车": "Expenses:Transport:WashCar",  # 洗车
        "打车|滴滴出行|曹操|高德打车|代驾|专车|智慧出行": "Expenses:Transport:TAXI",  # 打车
        "中石油|中石化|石化|石油|浙石油|中国石化|中国石油|中化|加油": "Expenses:Transport:Car:Oil",  # 加油
        "4S店": "Expenses:Transport:Car:Maintenance",  # 保养维修
        "平安保险|保险|人保|太保": "Expenses:Transport:Car:Insurance",  # 车险
        "停车|临时车缴费|停车费|浙A|统一公共支付平台": "Expenses:Transport:Car:Parking",  # 停车费

        # 购物
        "鞋|衣服|银泰|天街|屈臣氏|印象城|袜子|内裤|pay|NIKE|李宁|迪卡侬|优衣库|GAP|gxg": "Expenses:Shopping:Clothing ",  # 服饰鞋包
        "Apple Store|玩客云|大疆|树莓派|U盘|显卡|小米|ATX电源|迅雷|iCloud|iSlide|switch|App Store|applestore|BandwagonHost|域名|网卡|服务器|硬盘|NAS|内存|路由器|airpods|macbook|Mac": "Expenses:Shopping:Digital ",

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

    },
    "income": {
        "余额宝": "Income:MoneyFund:Alipay:YuEBao",
        "转账": "Income:TransferIn",
        "退款": "Income:Refund",
    },
    "liabilities": {
        "招商银行(5250)": "Liabilities:CreditCard:CMB",
        "花呗": "Liabilities:Alipay:HuaBai",
    },
    "equity": {
        "DEFAULT": "Equity:Opening-Balances"
    }
}

trace_change_map = {
    "goods=收益": "income_and_expenses=收入",
}
