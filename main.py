from conf_manager.account_conf import get_assets_account_list, get_equity_account_list, get_expenses_account_list, \
    get_income_account_list, get_liabilities_account_list
from export_manager.df_to_beans import df_to_beans
from export_manager.file_export import accounts_to_file, export_beans_to_workspace
from trace_processor.hoder import holder_processor


content_path = '/Users/peiel/Library/Mobile Documents/com~apple~CloudDocs/Personal/财务/beancount'

def read_beancount_account(account):
    path = content_path + '/accounts/%s.bean' % account
    with open(path, 'r') as f:
        lines = f.readlines()
        lines = [item for item in lines if 'open' in item]
        lines = [item.split(' ')[2].replace("\n", "").strip() for item in lines]
        return lines


if __name__ == '__main__':
    # 交易流水
    # df = holder_processor()
    # beans = df_to_beans(df)
    # export_beans_to_workspace(content_path, beans)

    # 账户配置
    org_assets_list = read_beancount_account("assets")
    assets_list = get_assets_account_list()
    assets_list = [item for item in assets_list if item not in org_assets_list]
    accounts_to_file(file=content_path + '/accounts/assets_auto.bean', accounts=assets_list)

    org_equity_list = read_beancount_account("equity")
    equity_list = get_equity_account_list()
    equity_list = [item for item in equity_list if item not in org_equity_list]
    accounts_to_file(file=content_path + '/accounts/equity_auto.bean', accounts=equity_list)

    org_expenses_list = read_beancount_account("expenses")
    expenses_list = get_expenses_account_list()
    expenses_list = [item for item in expenses_list if item not in org_expenses_list]
    accounts_to_file(file=content_path + '/accounts/expenses_auto.bean', accounts=expenses_list)

    org_income_list = read_beancount_account("income")
    income_list = get_income_account_list()
    income_list = [item for item in income_list if item not in org_income_list]
    accounts_to_file(file=content_path + '/accounts/income_auto.bean', accounts=income_list)

    org_liabilities_list = read_beancount_account("liabilities")
    liabilities_list = get_liabilities_account_list()
    liabilities_list = [item for item in liabilities_list if item not in org_liabilities_list]
    accounts_to_file(file=content_path + '/accounts/liabilities_auto.bean', accounts=liabilities_list)
