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


def match_expenses(bean):
    expenses = AccountConf.expenses
    # 绝对匹配
    if bean.location in expenses:
        return expenses[bean.location], bean.location + '->' + expenses[bean.location]
    if bean.desc in expenses:
        return expenses[bean.desc], bean.desc + '->' + expenses[bean.desc]
    # 模糊匹配
    for text, account in expenses.items():
        if text in bean.location or text in bean.desc:
            return account, text + '->' + account
    return expenses['未知'], None


def match_assets(bean):
    assets = AccountConf.assets
    if bean.pay_way == '' or bean.pay_way == '/':
        return assets['未知']
    if bean.pay_way in assets:
        return assets[bean.pay_way]
    return None


def match_liabilities(bean):
    # 兼容招行交易时的描述
    if '&' in bean.pay_way:
        bean.pay_way = bean.pay_way.split('&')[0]
    liabilities = AccountConf.liabilities
    if bean.pay_way in liabilities:
        return liabilities[bean.pay_way]
    return None


def match_payment_account(bean):
    account_assets = match_assets(bean)
    if account_assets:
        return account_assets
    account_liabilities = match_liabilities(bean)
    if account_liabilities:
        return account_liabilities
    raise Exception('无法判断付款账户', bean)


def match_receive_account(bean):
    account_assets = match_assets(bean)
    if account_assets:
        return account_assets
    account_income, _ = match_income(bean)
    if account_income:
        return account_income
    raise Exception('无法判断收款账户', bean)


def match_income(bean):
    income = AccountConf.income
    if bean.trace_obj in income:
        return income[bean.trace_obj], bean.trace_obj + '->' + income[bean.trace_obj]
    for text, account in income.items():
        if text in bean.trace_obj:
            return account, text + '->' + account
    return income['未知'], None


def convert_account(beans):
    for bean in beans:
        item = bean.items[0]
        if bean.income_and_expenses == '支出':
            # 使用匹配来确定支出的类型
            item.account, item.account_rule = match_expenses(bean)
            bean.items.append(Item(account=match_payment_account(bean)))
            pass
        if bean.income_and_expenses == '收入':
            # trace_obj 是收入来源
            item.account, item.account_rule = match_income(bean)
            bean.items.append(Item(account=match_receive_account(bean)))
            pass
        if bean.income_and_expenses == '调拨':
            pass

    return beans


def row_to_dict(row):
    return {
        "date": row['date'],
        "trace_type": row['trace_type'],
        "trace_obj": row['trace_obj'],
        "goods": row['goods'],
        "income_and_expenses": row['income_and_expenses'],
        "amount": row['amount'],
        "pay_way": row['pay_way'],
        "status": row['status'],
        "source": row['source'],
    }


def convert(df):
    print(df.head())
    beans = []
    for index, row in df.iterrows():
        org_row = row_to_dict(row)

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

        new_row = row_to_dict(row)

        item = Item(account=pay_way, amount=amount_format(amount, row))
        bean = Bean(date=datetime_format(date),
                    trace_type=trace_type,
                    location=trace_obj,
                    desc=goods,
                    items=[item],
                    income_and_expenses=income_and_expenses,
                    pay_way=pay_way,
                    trace_obj=trace_obj,
                    log_org_trace=org_row,
                    log_change_rule=change_rule,
                    log_new_trace=new_row)
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
