def split_bean_by_year(beans):
    beans_dict = {}
    for bean in beans:
        year = bean.date[:4]
        if year not in beans_dict:
            beans_dict[year] = list()
        year_beans = beans_dict[year]
        year_beans.append(bean)
    return beans_dict


def split_beans_by_month(beans):
    beans_dict = {}
    for bean in beans:
        month = bean.date[5:7]
        if month not in beans_dict:
            beans_dict[month] = list()
        month_beans = beans_dict[month]
        month_beans.append(bean)
    return beans_dict
