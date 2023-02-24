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
    for bean in beans:
        title = bean.date + ' * "' + (bean.remark if bean.remark else bean.trace_obj) + '" "' + bean.desc + '"' + (
            " " + bean.tags if bean.tags and bean.tags != "" else "")
        content = content + title + '\n'

        # 注释
        content = content + '\tid: "' + str(bean.id) + '"\n'
        content = content + '\tremark: "' + str(bean.remark) + '"\n'
        content = content + '\tdatetime: "' + str(bean.datetime) + '"\n'
        content = content + '\ttrace_obj: "' + str(bean.trace_obj) + '"\n'
        content = content + '\tdesc: "' + str(bean.desc) + '"\n'
        content = content + '\tstatus: "' + str(bean.status) + '"\n'
        content = content + '\tpay_way: "' + str(bean.pay_way) + '"\n'
        content = content + '\torder_no: "' + str(bean.order_no) + '"\n'
        content = content + '\tsource: "' + str(bean.source) + '"\n'
        content = content + '\ttrace_change_rule: "' + str(bean.trace_change_rule) + '"\n'

        for item in bean.items:
            content = content + '\t' + (item.account if item.account else 'Assets:Unknown') + (
                ' ' + str(item.amount) if item.amount or item.amount==0.0 else '') + (' ' + item.currency if item.amount or item.amount==0.0 else '')
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
        content = content + '2014-01-01 open ' + account + ' CNY' + '\n'
    with open(file, 'w') as f:
        f.write(content)
