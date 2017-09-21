import scanner,ssh,iplist
import datetime,time
import optparse,os,sys

def main():
    parser = optparse.OptionParser('\n -t --threads <threads>\n -i --ip <ip range>\n -u --username <username.txt>\n -p --password <password.txt>')
    parser.add_option('-t','--threads', dest='threads', type='int', default=100,
                      help='threads number [default=100]\n')
    parser.add_option('-i','--ip',dest='ip',type='string',
                      help='ip range. like 192.168.1.1 or 192.168.1.0/24 or 192.168.1.1-100 or 192.168.1.0-192.168.3.255')
    parser.add_option('-u','--username', dest='username', type='string', default='username.txt',
                      help='username file. Default username.txt')
    parser.add_option('-p','--password', dest='password', type='string', default='password.txt',
                      help='password file. Default password.txt')
    options = {}
    (options,args) = parser.parse_args()
    # sitting...
    scanner.threadNum = options.threads
    ssh.usernamefile = options.username
    ssh.passwordfile = options.password

    print(options.threads)
    print(options.ip)
    print(options.username)
    print(options.password)

    print('Start at %s.' % time.asctime())
    start_time = datetime.datetime.now()
    if options.ip is None or ''==options.ip:
        print('ip range input error.')
        return
    ip_range = iplist.getIPList(options.ip)
    if ip_range is None or ''==ip_range:
        print('ip range input error.')
        return
    scanner.portScanner(ip_range)
    end_time = datetime.datetime.now()
    print("End at %s. scan use %s" % (time.asctime(),(end_time - start_time)))


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