def beans_to_file(file, beans):
    """
    导出 beans 对象到文件
    :param file: 目标文件
    :param beans: 源 beans 对象
    :return:
    """
    content = ''
    for bean in beans:
        title = bean.date + ' * "' + bean.location + '" "' + bean.desc + '"'
        content = content + title + '\n'

        # 注释
        content = content + '\t; org: ' + ''.join(['{0}->{1} '.format(k, v) for k,v in bean.source_trace.items()]) + '\n'
        content = content + '\t; change_rule: ' + '\n'
        content = content + '\t; new: ' + '\n'

        for item in bean.items:
            content = content + '\t' + (item.account if item.account else 'Assets:Unknown') + ' ' + (str(item.amount) if item.amount else '') + ' ' + (item.currency if item.amount else '')
            content = content + ('\t;' + item.account_rule if item.account_rule else '') + '\n'
        content = content + '\n'
    with open(file, 'w+') as f:
        f.write(content)

def accounts_to_file(file, accounts):
    content = ''
    for account in accounts:
        content = content + '1993-02-13 open ' + account + ' CNY' + '\n'

    content = content + '1993-02-13 open ' + 'Expenses:Unknown' + ' CNY' + '\n'
    content = content + '1993-02-13 open ' + 'Income:Unknown' + ' CNY' + '\n'

    with open(file, 'w+') as f:
        f.write(content)