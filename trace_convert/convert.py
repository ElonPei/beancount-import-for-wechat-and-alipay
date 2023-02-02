from export_manager.file_export import beans_to_file
from import_manager.trace_loader import load_wechat_trace, load_alipay_trace
from model.bean import Bean, Item
from trace_convert.trace_account import convert_account, convert_trace_change

content_path = '/Users/peiel/PycharmProjects/beancount-import-for-wechat-and-alipay/out/'


def datetime_format(obj):
    return obj[:10]


def amount_format(obj, row):
    income_and_expenses = row['income_and_expenses']

    if '$' in obj or '¥' in obj:
        obj = obj[1:]
    if '收入' in income_and_expenses:
        return - float(obj)
    if '支出' in income_and_expenses or '调拨' in income_and_expenses:
        return float(obj)
    raise Exception('无法判断收支情况', income_and_expenses)


def load_rule():
    return None


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
    beans_to_file(file=content_path + 'wechat.bean', beans=wechat_beans)

    alipay_df = load_alipay_trace()
    alipay_beans = convert(alipay_df)
    beans_to_file(file=content_path + 'alipay.bean', beans=alipay_beans)
