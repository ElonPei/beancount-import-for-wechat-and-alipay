from export_manager.file_export import beans_to_file, accounts_to_file
from import_manager.trace_loader import load_wechat_trace, load_alipay_trace
from trace_convert.convert import convert
from trace_convert.trace_account import export_account_data

content_path = '/Users/peiel/PycharmProjects/beancount-import-for-wechat-and-alipay/out/'

if __name__ == '__main__':
    # wechat_df = load_wechat_trace()
    # wechat_beans = convert(wechat_df)
    # beans_to_file(file=content_path + 'wechat.bean', beans=wechat_beans)

    alipay_df = load_alipay_trace()
    alipay_beans = convert(alipay_df)
    beans_to_file(file=content_path + 'alipay.bean', beans=alipay_beans)

    accounts_to_file(file=content_path + 'account.bean', accounts=export_account_data())
