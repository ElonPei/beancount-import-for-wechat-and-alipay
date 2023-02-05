from export_manager.file_export import beans_to_file
from import_manager.trace_loader import load_wechat_trace, load_alipay_trace
from model.bean import Bean, Item
from trace_convert.trace_account_conf import AccountConf

content_path = '/Users/peiel/PycharmProjects/beancount-import-for-wechat-and-alipay/out/'


def datetime_format(obj):
    return obj[:10]


def amount_format(amount, row):
    income_and_expenses = row['income_and_expenses']

    if '$' in amount or '¥' in amount:
        amount = amount[1:]
    if '收入' in income_and_expenses:
        return - float(amount)
    if '支出' in income_and_expenses or '调拨' in income_and_expenses:
        return float(amount)
    raise Exception('无法判断收支情况', income_and_expenses)


def load_rule():
    return None


def is_match_rule(match_rule, row):
    # trace_obj = 网商银行 & goods = 账户结息
    for item in match_rule.split('&'):
        if item.split('=')[1] not in row[item.split('=')[0]]:
            return False
    return True


def convert_trace_change(row):
    change_rule = ''
    for match_rule, result in AccountConf.trace_change.items():
        if is_match_rule(match_rule, row):
            for item in result.split(','):
                row[item.split('=')[0]] = item.split('=')[1]
                change_rule = change_rule + " " + item
    return row, change_rule


def convert_account(beans):
    for bean in beans:
        item = bean.items[0]

    return beans


def convert(df):
    print(df.head())
    beans = []
    for index, row in df.iterrows():
        org_row = row
        row, change_rule = convert_trace_change(row)

        date = row['date']
        trace_type = row['trace_type']
        trace_obj = row['trace_obj']
        goods = row['goods']
        income_and_expenses = row['income_and_expenses']
        amount = row['amount']
        pay_way = row['pay_way']
        status = row['status']
        source = row['source']

        print('交易时间 -> ', date)
        print('交易类型 -> ', trace_type)
        print('交易对方 -> ', trace_obj)
        print('商品 -> ', goods)
        print('收/支 -> ', income_and_expenses)
        print('金额(元) -> ', amount)
        print('支付方式 -> ', pay_way)
        print('当前状态 -> ', status)
        print('来源 -> ', source)
        print()

        item = Item(account=pay_way, amount=amount_format(amount, row))
        bean = Bean(date=datetime_format(date),
                    trace_type=trace_type,
                    location=trace_obj,
                    desc=goods,
                    items=[item],
                    income_and_expenses=income_and_expenses,
                    org_trace=org_row,
                    change_rule=change_rule,
                    new_trace=row)
        beans.append(bean)
    return convert_account(beans)


if __name__ == '__main__':
    wechat_df = load_wechat_trace()
    wechat_beans = convert(wechat_df)
    print(">>>>>> 1111111111111111111")
    beans_to_file(file=content_path + 'wechat.bean', beans=wechat_beans)
    print(">>>>>> 2222222222222222222")

    alipay_df = load_alipay_trace()
    alipay_beans = convert(alipay_df)
    print(">>>>>> 3333333333333333333")
    beans_to_file(file=content_path + 'alipay.bean', beans=alipay_beans)
    print(">>>>>> 4444444444444444444")
