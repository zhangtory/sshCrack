# sshCrack
多线程破解指定网段内的ssh。

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

设置扫描线程数，默认100
```
python sshcrack --threads 200
```

设置扫描网段
```
python sshcrack --ip 192.168.1.1
python sshcrack --ip 192.168.1.0/24
python sshcrack --ip 192.168.1.1-100
python sshcrack --ip 192.168.1.1-192.168.3.200
```
