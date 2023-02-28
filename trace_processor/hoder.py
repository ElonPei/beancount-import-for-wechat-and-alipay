import os
import time

from import_manager.trace_loader import load_all_trace
from trace_processor.account_match import account_match
from trace_processor.amount import amount
from trace_processor.payment_on_behalf import payment_on_behalf
from trace_processor.refund import refund
from trace_processor.trace_change import trace_change
from trace_processor.transfer import transfer


def holder_processor():
    # 导入所有流水
    t1 = time.time()
    df = load_all_trace()
    t2 = time.time()
    print('load_all_trace', len(df), t2 - t1)

    # 执行流水转换配置
    df = trace_change(df)
    t3 = time.time()
    print('trace_change', len(df), t3 - t2)

    # 金额收支处理
    df = amount(df)
    t4 = time.time()
    print('amount', len(df), t4 - t3)

    # 代付处理
    df = payment_on_behalf(df)
    t5 = time.time()
    print('payment_on_behalf', len(df), t5 - t4)

    # 退款处理
    df = refund(df)
    t6 = time.time()
    print('refund', len(df), t6 - t5)

    # 资金调拨标记
    df = transfer(df)

    # 账户匹配
    df = account_match(df)
    t7 = time.time()
    print('account_match', len(df), t7 - t6)

    df.fillna("", inplace=True)
    df = df.sort_values(by='date')
    return df


if __name__ == '__main__':
    all_df = holder_processor()
    all_df.to_csv('example.csv', index=False)
    os.system('open example.csv')
