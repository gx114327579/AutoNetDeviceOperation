import AutoOperation as AO

__version__ = '0.1.0'


def main():
    path = open('config').readline().strip('\n\r ')
    dv = AO.DeviceInfo('devices.csv')
    for lst in dv.getinfolist():
        do = AO.DeviceOper(lst, path)
        try:
            do.oper()
            with open(do.wrpath + 'log.log', 'a+') as log:
                log.write('Hostname: {}, IP: {}, 已成功完成所有命令\n'.format(do.hostname, do.ip))
        except:
            with open(do.wrpath + 'log.log', 'a+') as log:
                log.write('Hostname: {}, IP: {}, 未完成指令，请检查\n'.format(do.hostname, do.ip))


if __name__ == '__main__':
    main()
