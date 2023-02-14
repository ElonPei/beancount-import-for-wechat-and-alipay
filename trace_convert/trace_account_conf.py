import os
import yaml


def load_account_conf(conf_path):
    with open(conf_path, "r") as file:
        return yaml.safe_load(file)


def revert_to_map(input_dict):
    d = dict()
    for k, v in input_dict.items():
        for item in v:
            d[item] = k
    return d


class AccountConf:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    trace_change = load_account_conf('%s/../conf/trace_change_conf.yml' % dir_path)

    dict_assets = load_account_conf('%s/../conf/account_assets_conf.yml' % dir_path)
    assets = revert_to_map(dict_assets)
    dict_equity = load_account_conf('%s/../conf/account_equity_conf.yml' % dir_path)
    equity = revert_to_map(dict_equity)
    dict_expenses = load_account_conf('%s/../conf/account_expenses_conf.yml' % dir_path)
    expenses = revert_to_map(dict_expenses)
    dict_income = load_account_conf('%s/../conf/account_income_conf.yml' % dir_path)
    income = revert_to_map(dict_income)
    dict_liabilities = load_account_conf('%s/../conf/account_liabilities_conf.yml' % dir_path)
    liabilities = revert_to_map(dict_liabilities)


def get_all_account_list():
    account_list = []
    account_list.extend(list(AccountConf.dict_assets.keys()))
    account_list.extend(list(AccountConf.dict_equity.keys()))
    account_list.extend(list(AccountConf.dict_expenses.keys()))
    account_list.extend(list(AccountConf.dict_income.keys()))
    account_list.extend(list(AccountConf.dict_liabilities.keys()))
    return account_list


if __name__ == '__main__':
    print(AccountConf.trace_change)
    print(AccountConf.assets)
    print(AccountConf.equity)
    print(AccountConf.expenses)
    print(AccountConf.income)
    print(AccountConf.liabilities)
    print(get_all_account_list())
