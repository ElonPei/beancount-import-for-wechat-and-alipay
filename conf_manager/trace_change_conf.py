import os

from conf_manager.util import load_account_conf


class TraceChangeConf:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    trace_change = load_account_conf('%s/../conf/trace_change_conf.yml' % dir_path)


if __name__ == '__main__':
    print(TraceChangeConf.trace_change)
