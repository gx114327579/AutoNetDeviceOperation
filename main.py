import AutoOperation as AO
import threading
import time
import functools
import logging

FORMAT = '%(asctime)-15s\t%(levelname)s %(module)s %(funcName)s %(message)s'
path = open('config').readline().strip('\n\r ')
logging.basicConfig(format=FORMAT, level=20)
logger = logging.getLogger(__name__)
file_h = logging.FileHandler(path + 'log.log')
file_h.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(file_h)

__version__ = '0.2.0'


# TODO 路径使用PATH模块
# TODO 日志使用logging模块，抽象相应代码

def timer(*args, **kwargs):
    def _timer(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = fn(*args, **kwargs)
            end = time.time() - start
            print("Total seconds: {:.3f}".format(end))
            return result

        return wrapper

    return _timer


def main():
    # lock = threading.Lock()

    dv = AO.DeviceInfo('devices.csv')

    @timer()
    def oper(lst, path):
        do = AO.DeviceOper(lst, path)
        try:
            do.oper()
            logger.info('Hostname: {}, IP: {}, 已成功完成所有命令'.format(do.hostname, do.ip))

        except:
            logger.info('Hostname: {}, IP: {}, 未完成指令，请检查'.format(do.hostname, do.ip))

    for lst in dv.getinfolist():
        threading.Thread(target=oper, args=(lst, path)).start()
        print(threading.active_count())


if __name__ == '__main__':
    main()
