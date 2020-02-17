from tools.zhuanhuan import *
from funs_domain import *
from func_http import *
from funs_signal import *
import sys ,os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
f=open("../file/af4bebd0-54ca-ffca-ca7c-25c7814574cd.txt")
data=linesStr_to_lineDic(f.read())
signal_dic={}
qr_0_host={}
qr_1_ip={}
domain_dic={}
http_dic={}

for dic  in data :
    client = dic.get("sip") + ":" + dic.get("sport")
    server = dic.get("dip") + ":" + dic.get("dport")
    if dic.get("qr") == "0":
        domain_qr0(dic,qr_0_host)
    elif dic.get("qr") == "1" and dic.get("ip"):
        domain_qr1(dic,qr_0_host,qr_1_ip)
    elif dic.get("flag")== '40962':
        domain_40962(dic,client,server,qr_1_ip,domain_dic)
    elif dic.get("flag")=="20496":
        domain_40296(dic,client,server,domain_dic)
    # 以下处理信令
    elif dic.get("type") =='udp':
        signal_upd(dic,client,server,signal_dic) #处理updtype==udp的信令
    elif dic.get("flag") == "20504":
        signal_tcp_20504(dic,client,server,signal_dic)
        http_20504(dic,client,server,http_dic)
    elif dic.get("flag")  == '20496':
        signal_tcp_20496(dic,client,server,signal_dic)
        http_20496(dic,client,server,signal_dic)

#过滤掉没有有通过 DNS 发起tcp 连接的 dmain-info
##为每个ip 添加cdn信息
for k,v in qr_1_ip.items():
    tcpData=list(filter( lambda ipinfo:k in ipinfo,domain_dic))  #过滤出有通过 DNS 发起tcp 连接的 TCP-info
    for ip  in tcpData:
        domain_dic[ip]["cdn"]=v
domain_dic={ip:info for ip,info in domain_dic.items() if info.get("cdn") }
db_list=domian_dic_to_db_dic(domain_dic,"af4bebd0-54ca-ffca-ca7c-25c7814574cd")
from DB.tables import  Domain
# print(db_list)
# print(Domain().query("domain,ip,dnsreplydelay,tcpbuilddelay,dns_suc_rate,tcp_suc_rate"))
Domain().insert_data(db_list)