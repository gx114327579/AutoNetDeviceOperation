# AutoNetDeviceOperation
CCYC Cisco Network Device Automatic Operation

请在config文件中直接写入要存放log的目录

注意目录文件可以不存在，但是路径最后一定要加"\\"或"/"符号，具体视操作系统决定

Commands文件目录下存放的文件以设备型号命名，内部每条命令占一行

devices.csv文件中列明要收集的设备，因型号不同，所以每module要有对应的命令集文件

例如：devices.csv中第三列型号是"3560"，要求在Commands文件夹中一定要有"3560"这个文件，里边存放着此种类型设备要执行的命令

最后请检查log.log文件
