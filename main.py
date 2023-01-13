from import_manager.trace_loader import load_wechat_trace

if __name__ == '__main__':
    df = load_wechat_trace()
    print("微信流水加载成功，共 %s 条数据" % len(df))
    print(df.head())