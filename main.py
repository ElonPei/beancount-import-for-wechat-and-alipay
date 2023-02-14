from export_manager.file_export import accounts_to_file, export_beans_to_workspace
from import_manager.trace_loader import load_all_trace
from trace_convert.convert import convert
from trace_convert.trace_account_conf import get_all_account_list

content_path = '/Users/peiel/Library/Mobile Documents/com~apple~CloudDocs/Personal/财务/beancount'

if __name__ == '__main__':
    df = load_all_trace()
    beans = convert(df)
    export_beans_to_workspace(content_path, beans)

    accounts_to_file(file=content_path + '/account.bean', accounts=get_all_account_list())
