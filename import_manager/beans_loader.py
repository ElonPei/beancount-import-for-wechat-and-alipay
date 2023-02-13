import glob
import os
import re

import pandas as pd

bean_path = '/Users/peiel/Library/Mobile Documents/com~apple~CloudDocs/Personal/财务/beancount'


def starts_with_date(string):
    pattern = re.compile("^\d{4}-\d{2}-\d{2}")
    match = pattern.match(string)
    return True if match else False


def extract_tags(transaction_line):
    tags = []
    fields = transaction_line.split(" ")
    for field in fields:
        if field.startswith("#"):
            tags.append(field)
    return " ".join(tags)


def load_remark_info():
    lines = []
    for f in glob.glob(os.path.join(bean_path, 'wechat.bean')):
        with open(f, "r") as file:
            lines = file.readlines()
    lines_list = [line.strip() for line in lines if line.startswith("\tid:") or line.startswith("\tremark:") or starts_with_date(line)]
    lines_list = [line.replace('\t', '') for line in lines_list]
    lines_list = [line.replace('\n', '') for line in lines_list]
    lines_list = [line.replace('"', '') for line in lines_list]

    id_list = [line.split(':')[1].strip() for line in lines_list if line.startswith('id:')]
    remark_list = [line.split(':')[1].strip() for line in lines_list if line.startswith('remark:')]
    tags_list = [extract_tags(line) for line in lines_list if starts_with_date(line)]

    df = pd.DataFrame({
        "id": id_list,
        "remark": remark_list,
        "tags": tags_list,
    })
    df = df[df['remark'] != ""]
    return df


if __name__ == '__main__':
    print(load_remark_info())
