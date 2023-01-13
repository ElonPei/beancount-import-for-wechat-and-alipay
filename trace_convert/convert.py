from import_manager.trace_loader import load_wechat_trace
from trace_convert.bean import Bean, Item

content_path = '/Users/peiel/PycharmProjects/beancount-import-for-wechat-and-alipay/out/'


def datetime_format(obj):
    return obj[:10]


def amount_format(obj, income_and_expenses):
    if '收入' in income_and_expenses:
        return - float(obj[1:])
    if '支出' in income_and_expenses:
        return obj[1:]
    # raise Exception('无法判断收支情况', income_and_expenses)
    return 0


def beans_to_file(file, beans):
    content = ''
    for bean in beans:
        title = bean.date + ' * "' + bean.location + '" "' + bean.desc + '"'
        content = content + title + '\n'
        for item in bean.items:
            content = content + item.account + ' ' + str(item.amount) + ' ' + item.currency + '\n'
        content = content + '\n'
    with open(file, 'w+') as f:
        f.write(content)


def load_rule():
    return None


def convert(df):
    print(df.head())
    beans = []
    for index, row in df.iterrows():
        date = row['交易时间']
        trace_type = row['交易类型']
        trace_obj = row['交易对方']
        good = row['商品']
        income_and_expenses = row['收/支']
        amount = row['金额(元)']
        pay_way = row['支付方式']
        status = row['当前状态']

        print('交易时间 -> ', date)
        print('交易类型 -> ', trace_type)
        print('交易对方 -> ', trace_obj)
        print('商品 -> ', good)
        print('收/支 -> ', income_and_expenses)
        print('金额(元) -> ', amount)
        print('支付方式 -> ', pay_way)
        print('当前状态 -> ', status)
        print()

        item = Item(account=pay_way, amount=amount_format(amount, income_and_expenses))
        bean = Bean(date=datetime_format(date), location=trace_obj, desc=trace_type, items=[item])
        beans.append(bean)
    return beans


if __name__ == '__main__':
    wechat_df = load_wechat_trace()
    wechat_beans = convert(wechat_df)
    beans_to_file(file=content_path + 'wechat.bean', beans=wechat_beans)
