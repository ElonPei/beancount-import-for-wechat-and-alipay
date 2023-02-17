from import_manager.trace_loader import load_all_trace
from trace_processor.trace_account_conf import AccountConf


def trace_change(df):
    conf = AccountConf.trace_change
    print(conf)
    return df


if __name__ == '__main__':
    all_df = load_all_trace()
    print(len(all_df))
    all_df = trace_change(all_df)
    print(all_df.head())
