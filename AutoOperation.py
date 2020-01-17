import DeviceConnect as dc
import re


# infolst = ['hostname', 'ip', 'username', 'password', 'enable', 'sshport', 'telnetport']


class DeviceInfo:

    def __init__(self, devices_file):
        self.file = devices_file

    def getinfolist(self):
        with open(self.file) as device_info:
            flag = False
            for line in device_info:
                if flag:
                    lst = re.split(',', line.strip('\n'))
                    yield lst
                flag = True


class DeviceOper:

    def __init__(self, lst, wrpath):
        self.hostname = lst[0]
        self.ip = lst[1]
        self.module = lst[2]
        self.username = lst[3]
        self.password = lst[4]
        self.enable = lst[5]
        self.sshport = lst[6]
        self.telnetport = lst[7]
        if wrpath.startswith('./'):
            self.wrpath = ''
        else:
            self.wrpath = wrpath

    def oper(self):
        device = dc.SSH(self.ip, self.username, self.password)
        device.connect()
        device.disable_paging()
        device.set_enable(self.enable)

        with open('Commands/' + self.module) as commands:
            for line in commands:
                line = line.strip('\n')
                if line:
                    rst = device.command(line)
                    with open(self.wrpath + self.hostname + '.log', 'a+') as wr:
                        wr.write(rst)

        device.close()
