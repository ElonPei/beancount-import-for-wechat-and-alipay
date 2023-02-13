import glob
import os

import pandas as pd

bean_path = '/Users/peiel/Library/Mobile Documents/com~apple~CloudDocs/Personal/财务/beancount'


def load_remark_info():
    lines = []
    for f in glob.glob(os.path.join(bean_path, 'wechat.bean')):
        with open(f, "r") as file:
            lines = file.readlines()
    lines_list = [line.strip() for line in lines if line.startswith("\tid:") or line.startswith("\tremark:")]
    lines_list = [line.replace('\t', '') for line in lines_list]
    lines_list = [line.replace('\n', '') for line in lines_list]
    lines_list = [line.replace('"', '') for line in lines_list]

    id_list = [line.split(':')[1].strip() for line in lines_list if line.startswith('id:')]
    remark_list = [line.split(':')[1].strip() for line in lines_list if line.startswith('remark:')]

    df = pd.DataFrame({"id": id_list, "remark": remark_list})
    df = df[df['remark'] != ""]
    return df


if __name__ == '__main__':
    print(load_remark_info())
