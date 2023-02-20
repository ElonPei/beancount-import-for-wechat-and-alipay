import os

from import_manager.trace_loader import load_all_trace
from trace_processor.account_match import account_match
from trace_processor.amount import amount
from trace_processor.refund import refund
from trace_processor.trace_change import trace_change

if __name__ == '__main__':
    all_df = load_all_trace()
    all_df = trace_change(all_df)
    all_df = amount(all_df)
    all_df = refund(all_df)
    all_df = account_match(all_df)
    all_df.to_csv('example.csv', index=False)
    os.system('open example.csv')
