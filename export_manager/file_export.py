def beans_to_file(file, beans):
    """
    导出 beans 对象到文件
    :param file: 目标文件
    :param beans: 源 beans 对象
    :return:
    """
    content = ''
    for bean in beans:
        content = content + '; ' + ''.join(['{0}->{1} '.format(k, v) for k,v in bean.source_trace.items()]) + '\n'
        title = bean.date + ' * "' + bean.location + '" "' + bean.desc + '"'
        content = content + title + '\n'
        for item in bean.items:
            content = content + item.account + ' ' + (str(item.amount) if item.amount else '') + ' ' + (item.currency if item.amount else '') + '\n'
        content = content + '\n'
    with open(file, 'w+') as f:
        f.write(content)
