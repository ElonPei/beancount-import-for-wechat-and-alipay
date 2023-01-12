import csv


def format_wechat_to_list(path):
    """
    格式化微信流水的格式
    删除掉头部无用的信息
    :return:
    """
    rows = read_csv_to_list(path)
    rows = delete_rows(rows, 0, 15)
    return rows


def format_alipay_to_list(path):
    """
    格式化支付宝流水的格式
    删除掉头部无用的信息
    :return:
    """
    rows = read_csv_to_list(path)
    rows = delete_rows(rows, 0, 15)
    return rows


def read_csv_to_list(path):
    with open(path, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def delete_rows(content_rows, start_idx, end_idx):
    result_rows = []
    if len(content_rows) == 0 \
            or end_idx > len(content_rows) - 1 \
            or start_idx < 0:
        return result_rows
    for idx, row, in enumerate(content_rows):
        if idx < start_idx or idx > end_idx:
            result_rows.append(row)
    return result_rows
