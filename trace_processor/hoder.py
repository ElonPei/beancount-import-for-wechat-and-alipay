import os

from import_manager.trace_loader import load_all_trace
from trace_processor.account_match import account_match
from trace_processor.amount import amount
from trace_processor.refund import refund
from trace_processor.trace_change import trace_change


def holder_processor():
    df = load_all_trace()
    df = trace_change(df)
    df = amount(df)
    df = refund(df)
    df = account_match(df)
    df = df.sort_values(by='date')
    return df


if __name__ == '__main__':
    all_df = holder_processor()
    all_df.to_csv('example.csv', index=False)
    os.system('open example.csv')