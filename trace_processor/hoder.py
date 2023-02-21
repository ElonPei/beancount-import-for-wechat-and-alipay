import os
import time

from import_manager.trace_loader import load_all_trace
from trace_processor.account_match import account_match
from trace_processor.amount import amount
from trace_processor.refund import refund
from trace_processor.trace_change import trace_change


def holder_processor():
    t1 = time.time()
    df = load_all_trace()
    t2 = time.time()
    print('load_all_trace', len(df), t2 - t1)
    df = trace_change(df)
    t3 = time.time()
    print('trace_change', len(df), t3 - t2)
    df = amount(df)
    t4 = time.time()
    print('amount', len(df), t4 - t3)
    df = refund(df)
    t5 = time.time()
    print('refund', len(df), t5 - t4)
    df = account_match(df)
    t6 = time.time()
    print('account_match', len(df), t6 - t5)

    df.fillna("", inplace=True)
    df = df.sort_values(by='date')
    return df


if __name__ == '__main__':
    all_df = holder_processor()
    all_df.to_csv('example.csv', index=False)
    os.system('open example.csv')
