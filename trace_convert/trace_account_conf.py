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
    trace_change = load_account_conf('../conf/trace_change_conf.yml')

    assets = revert_to_map(load_account_conf('../conf/account_assets_conf.yml'))
    equity = revert_to_map(load_account_conf('../conf/account_equity_conf.yml'))
    expenses = revert_to_map(load_account_conf('../conf/account_expenses_conf.yml'))
    income = revert_to_map(load_account_conf('../conf/account_income_conf.yml'))
    liabilities = revert_to_map(load_account_conf('../conf/account_liabilities_conf.yml'))


if __name__ == '__main__':
    print(AccountConf.trace_change)
    print(AccountConf.assets)
    print(AccountConf.equity)
    print(AccountConf.expenses)
    print(AccountConf.income)
    print(AccountConf.liabilities)
