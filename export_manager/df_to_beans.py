from model.bean import Item, Bean


def datetime_format(obj):
    return obj[:10]


def df_to_beans(df):
    beans = []
    for index, row in df.iterrows():
        id = row['id']
        remark = row['remark']
        relation = row['relation']
        tags = row['tags']
        date = row['date']
        trace_type = row['trace_type']
        trace_obj = row['trace_obj']
        goods = row['goods']
        income_and_expenses = row['income_and_expenses']
        amount = row['amount']
        pay_way = row['pay_way']
        status = row['status']
        order_no = row['order_no']
        source = row['source']
        owner = row['owner']
        desc_account_rule = row['desc_account_rule']
        trace_change_rule = row['trace_change_rule']

        # print('id -> ', id)
        # print('remark -> ', remark)
        # print('tags -> ', tags)
        # print('交易时间 -> ', date)
        # print('交易类型 -> ', trace_type)
        # print('交易对方 -> ', trace_obj)
        # print('商品 -> ', goods)
        # print('收/支 -> ', income_and_expenses)
        # print('金额(元) -> ', amount)
        # print('支付方式 -> ', pay_way)
        # print('当前状态 -> ', status)
        # print('订单号 -> ', order_no)
        # print('来源 -> ', source)
        # print('目标账户转换规则 -> ', desc_account_rule)
        # print('流水转换规则 -> ', trace_change_rule)
        # print()

        desc_item = Item(account=row['desc_account'], amount=amount, account_rule=desc_account_rule)
        pre_item = Item(account=row['pre_account'])

        bean = Bean(id=id,
                    remark=remark,
                    relation=relation,
                    tags=tags,
                    date=datetime_format(date),
                    datetime=date,
                    trace_type=trace_type,
                    trace_obj=trace_obj,
                    desc=goods,
                    items=[desc_item, pre_item],
                    income_and_expenses=income_and_expenses,
                    pay_way=pay_way,
                    status=status,
                    order_no=order_no,
                    source=source,
                    owner=owner,
                    trace_change_rule=trace_change_rule,
                    )
        beans.append(bean)

    return beans

