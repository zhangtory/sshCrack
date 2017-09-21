# sshCrack
多线程破解指定网段内的ssh。
先扫描22端口是否开启，若开启再进行密码破解，从而节省时间。

## 安装依赖
```
pip install paramiko
pip install IPy
```

## 使用方法
显示帮助
```
python sshcrack -h
```

设置扫描线程数,默认100
```
python sshcrack -t 200
python sshcrack --threads 200
```

设置用户名文件,默认使用username.txt
```
python sshcrack -u user.txt
python sshcrack --username user.txt
```

设置密码文件,默认使用password.txt
```
python sshcrack -p passwd.txt
python sshcrack --password passwd.txt
```

设置扫描网段,必须要设置
```
python sshcrack -i 192.168.1.1
python sshcrack -i 192.168.1.0/24
python sshcrack --ip 192.168.1.1-100
python sshcrack --ip 192.168.1.1-192.168.3.200
```
