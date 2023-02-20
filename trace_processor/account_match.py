from import_manager.trace_loader import load_all_trace
from trace_processor.trace_change import trace_change


def account_match(df):



    return df


if __name__ == '__main__':
    all_df = load_all_trace()
    print(len(all_df))
    all_df = trace_change(all_df)
    all_df = account_match(all_df)
    print(all_df.head())
    print(all_df.columns)

    all_df.to_csv('example.csv', index=False)
