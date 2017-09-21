import scanner,iplist
import datetime,time
import optparse,os,sys

def main():
    parser = optparse.OptionParser('\n --threads <threads>\n --ip <ip range>')
    parser.add_option('--threads', dest='threads', type='int', default=100, help='threads number [default=100]\n')
    parser.add_option('--ip',dest='ip',type='string',help='ip range. like 192.168.1.1 or 192.168.1.0/24 or 192.168.1.1-100 or 192.168.1.0-192.168.3.255')
    options = {}
    (options,args) = parser.parse_args()
    scanner.threadNum = options.threads
    print('start at %s.' % time.asctime())
    start_time = datetime.datetime.now()
    scanner.portScanner(iplist.getIPList(options.ip))
    end_time = datetime.datetime.now()
    print("end at %s. scan use %s" % time.asctime(),(end_time - start_time))


if __name__ == '__main__':
    if sys.platform == 'linux-i386' or sys.platform == 'linux2' or sys.platform == 'darwin':
        SysCls = 'clear'
        os.system(SysCls)
    elif sys.platform == 'win32' or sys.platform == 'dos' or sys.platform[0:5] == 'ms-dos':
        SysCls = 'cls'
        os.system(SysCls)
    else:
        pass
    main()