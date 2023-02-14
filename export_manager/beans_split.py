from import_manager.trace_loader import load_wechat_trace
from trace_convert.convert import convert


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


if __name__ == '__main__':
    wechat_df = load_wechat_trace()
    wechat_beans = convert(wechat_df)
    yd = split_bean_by_year(beans=wechat_beans)
    for y, ybs in yd.items():
        print(y, len(ybs))
        md = split_beans_by_month(ybs)
        for m, mbs in md.items():
            print(y + m, len(mbs))
