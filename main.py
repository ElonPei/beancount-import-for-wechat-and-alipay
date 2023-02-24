from export_manager.df_to_beans import df_to_beans
from export_manager.file_export import accounts_to_file, export_beans_to_workspace
from trace_processor.hoder import holder_processor


content_path = '/Users/peiel/Library/Mobile Documents/com~apple~CloudDocs/Personal/财务/beancount'

if __name__ == '__main__':
    df = holder_processor()
    beans = df_to_beans(df)

    export_beans_to_workspace(content_path, beans)
    accounts_to_file(file=content_path + '/account.bean', accounts=get_all_account_list())
