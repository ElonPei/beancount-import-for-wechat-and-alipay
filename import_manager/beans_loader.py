import fnmatch
import os
import re

import pandas as pd


def find_all_auto_bean_file():
    beans_paths = []
    bean_path = '/Users/peiel/Library/Mobile Documents/com~apple~CloudDocs/Personal/财务/beancount'
    # 遍历目录树查找所有符合条件的文件
    for root, dirs, files in os.walk(bean_path):
        for filename in fnmatch.filter(files, '*auto.bean'):
            # 输出文件名或者执行其他操作
            beans_paths.append(os.path.join(root, filename))
    return beans_paths


def starts_with_date(string):
    pattern = re.compile("^\d{4}-\d{2}-\d{2}")
    match = pattern.match(string)
    return True if match else False


def extract_tags(transaction_line):
    transaction_line = re.sub(r'\"[^\"]+\"', '', transaction_line)
    tags = []
    fields = transaction_line.split(" ")
    for field in fields:
        if field.startswith("#"):
            tags.append(field)
    return " ".join(tags)


def load_custom_info():
    lines = []
    for f in find_all_auto_bean_file():
        if '/accounts/' in f:
            continue
        with open(f, "r") as file:
            lines = lines + file.readlines()
    lines_list = [line.strip() for line in lines if
                  line.startswith("\tid:") or
                  line.startswith("\tremark:") or
                  starts_with_date(line) or
                  line.startswith("\trelation:")]
    lines_list = [line.replace('\t', '') for line in lines_list]
    lines_list = [line.replace('\n', '') for line in lines_list]

    id_list = [line.split(':')[1].strip().replace('"', '') for line in lines_list if line.startswith('id:')]
    remark_list = [line.split(':')[1].strip().replace('"', '') for line in lines_list if line.startswith('remark:')]
    relation_list = [line.split(':')[1].strip().replace('"', '') for line in lines_list if line.startswith('relation:')]
    tags_list = [extract_tags(line) for line in lines_list if starts_with_date(line)]

    if len(remark_list) != len(id_list):
        remark_list = ['' for _ in range(len(id_list))]
    if len(relation_list) != len(id_list):
        relation_list = ['' for _ in range(len(id_list))]
    if len(tags_list) != len(id_list):
        tags_list = ['' for _ in range(len(id_list))]

    df = pd.DataFrame({
        "id": id_list,
        "remark": remark_list,
        "relation": relation_list,
        "tags": tags_list,
    })
    df = df[(df['remark'].notnull()) & (df['remark'] != '') | (df['relation'].notnull()) & (df['relation'] != '') | (
        df['tags'].notnull()) & (df['tags'] != '')]
    df.drop_duplicates(subset=['id'], keep='first', inplace=True)
    return df


if __name__ == '__main__':
    print(load_custom_info())
