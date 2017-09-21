import IPy
import re

def getIPList(ipstr):
    ipList = []
    if re.search(r'/',ipstr) is not None:
        try:
            ipy_ip = IPy.IP(ipstr)
        except:
            return None
        for x in ipy_ip:
            if x.strNormal() not in ipy_ip.net().strNormal() and x.strNormal() not in ipy_ip.broadcast().strNormal():
                ipList.append(x.strNormal())
    elif re.search(r'-',ipstr) is not None:
        sip = re.compile('(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})').findall(ipstr)
        start_ipaddr = str(sip[0][0])+'.'+str(sip[0][1])+'.'+str(sip[0][2])+'.'+str(sip[0][3])
        try:
            IPy.IP(start_ipaddr)
        except:
            return None
        #xxx.xxx.xxx.aaa-bbb
        if len(sip) is 1:
            endnum = re.compile('-(\d+)').findall(ipstr)
            end_ipaddr = str(sip[0][0])+'.'+str(sip[0][1])+'.'+str(sip[0][2])+'.'+str(endnum[0])
            try:
                IPy.IP(end_ipaddr)
            except:
                return None
            for x in range(int(sip[0][3]),int(endnum[0])+1):
                if x==0 or x==255:
                    continue
                ipList.append(str(sip[0][0])+'.'+str(sip[0][1])+'.'+str(sip[0][2])+'.'+str(x))
        # xxx.xxx.xxx.xxx-xxx.xxx.xxx.xxx
        elif len(sip) is 2:
            end_ipaddr = str(sip[1][0])+'.'+str(sip[1][1])+'.'+str(sip[1][2])+'.'+str(sip[1][3])
            try:
                IPy.IP(end_ipaddr)
            except:
                return None
            mask_flag = 0
            if sip[0][2] != sip[1][2]:
                mask_flag = 1
            if sip[0][1] != sip[1][1]:
                mask_flag = 2
            if sip[0][0] != sip[1][0]:
                mask_flag = 3
            if mask_flag == 3:
                for ip1 in range(int(sip[0][0]),int(sip[1][0])+1):
                    for ip2 in range(0,256):
                        for ip3 in range(0,256):
                            for ip4 in range(1,255):
                                ipList.append(str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' + str(ip4))
            if mask_flag == 2:
                for ip1 in range(int(sip[0][0]),int(sip[1][0])+1):
                    for ip2 in range(int(sip[0][1]),int(sip[1][1])+1):
                        for ip3 in range(0,256):
                            for ip4 in range(1,255):
                                ipList.append(str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' + str(ip4))
            if mask_flag == 1:
                for ip1 in range(int(sip[0][0]),int(sip[1][0])+1):
                    for ip2 in range(int(sip[0][1]),int(sip[1][1])+1):
                        for ip3 in range(int(sip[0][2]),int(sip[1][2])+1):
                            for ip4 in range(1,255):
                                ipList.append(str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' + str(ip4))
            if mask_flag == 0:
                for ip1 in range(int(sip[0][0]),int(sip[1][0])+1):
                    for ip2 in range(int(sip[0][1]),int(sip[1][1])+1):
                        for ip3 in range(int(sip[0][2]),int(sip[1][2])+1):
                            for ip4 in range(int(sip[0][3]),int(sip[1][3])+1):
                                if ip4==0 or ip4==255:
                                    continue
                                ipList.append(str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' + str(ip4))
        else:
            return None
    else:
        try:
            #check input
            IPy.IP(ipstr)
        except:
            return None
        ipList.append(ipstr)
    return ipList

# # al = getIPList('192.168.1.3-25')
# al = getIPList('192.168.1.0-192.168.2.255')
# # al = getIPList('192.168.1.0/24')
# if al is None:
#     print('input error')
# else:
#     for x in al:
#         print(x)