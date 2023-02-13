def beans_to_file(file, beans):
    """
    导出 beans 对象到文件
    :param file: 目标文件
    :param beans: 源 beans 对象
    :return:
    """
    content = ''
    i = 1
    for bean in beans:
        print('>>', i)
        i = i + 1
        title = bean.date + ' * "' + bean.location + '" "' + bean.desc + '"' + '\t; ' + bean.trace_type
        content = content + title + '\n'

        # 注释
        content = content + '\t; org: ' + str(bean.log_org_trace) + '\n'
        content = content + '\t; change_rule: ' + str(bean.log_change_rule) + '\n'
        content = content + '\t; new: ' + str(bean.log_new_trace) + '\n'

        for item in bean.items:
            content = content + '\t' + (item.account if item.account else 'Assets:Unknown') + (' ' + str(item.amount) if item.amount else '') + (' ' + item.currency if item.amount else '')
            content = content + ('\t;' + item.account_rule if item.account_rule else '') + '\n'

        # id
        content = content + '\tid: "' + str(bean.id) + '"\n'

        content = content + '\n'
    with open(file, 'w+') as f:
        f.write(content)


def accounts_to_file(file, accounts):
    content = ''
    for account in accounts:
        content = content + '1993-02-13 open ' + account + ' CNY' + '\n'
    with open(file, 'w+') as f:
        f.write(content)
