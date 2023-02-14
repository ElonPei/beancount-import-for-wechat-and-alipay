import os
from export_manager.beans_split import split_bean_by_year, split_beans_by_month


def check_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def export_beans_to_workspace(workspace, beans):
    """
    对beans按年月切分，并导出到指定的工作目录
    """
    for year, year_beans in split_bean_by_year(beans=beans).items():
        month_dict = split_beans_by_month(year_beans)
        for month, month_beans in month_dict.items():
            check_dir('%s/%s' % (workspace, year))
            beans_path = '%s/%s/%s_auto.bean' % (workspace, year, year + month)
            print(year + month, len(month_beans))
            beans_to_file(beans_path, month_beans)


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
        title = bean.date + ' * "' + bean.location + '" "' + bean.desc + '"' + (
            " " + bean.tags if bean.tags and bean.tags != "" else "")
        content = content + title + '\n'

        # 注释
        content = content + '\t; org: ' + str(bean.log_org_trace) + '\n'
        content = content + '\t; change_rule: ' + str(bean.log_change_rule) + '\n'
        content = content + '\t; new: ' + str(bean.log_new_trace) + '\n'

        # id
        content = content + '\tid: "' + str(bean.id) + '"\n'
        content = content + '\tremark: "' + str(bean.remark) + '"\n'

        for item in bean.items:
            content = content + '\t' + (item.account if item.account else 'Assets:Unknown') + (
                ' ' + str(item.amount) if item.amount else '') + (' ' + item.currency if item.amount else '')
            content = content + ('\t;' + item.account_rule if item.account_rule else '') + '\n'

        content = content + '\n'
    try:
        with open(file, 'w+') as f:
            f.write(content)
    except FileNotFoundError:
        with open(file, 'w') as f:
            f.write(content)


def accounts_to_file(file, accounts):
    content = ''
    for account in accounts:
        content = content + '1993-02-13 open ' + account + ' CNY' + '\n'
    with open(file, 'w+') as f:
        f.write(content)
