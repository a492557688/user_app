def  linesStr_to_lineDic(lineString):
    lineString=lineString.strip()
    lines = lineString.split("\n")
    lines = [line.strip() for line in lines]
    return [{dengyustr.split("=")[0]:dengyustr.split("=")[1] for dengyustr in line.split("||") }   for line in lines  ]
def  lineList_to_lineDic(lineList):
    lines = [line.strip() for line in lineList]
    return [{dengyustr.split("=")[0]:dengyustr.split("=")[1] for dengyustr in line.split("||") }   for line in lines  ]

def domian_dic_to_db_dic(data,uuid):
    '''转换到数据库的键值对形式'''
    '''    {"ipinfo":{"tcp":{},"dns":{}}}           '''
    data_list=[]
    for k,v in data.items():
        li=[]
        client,server=k.split("|")
        client_ip,client_port=client.split(":")
        ip,server_port=server.split(":")
        domain=v["cdn"].get("url")
        t_mobile=v["cdn"].get("t_mobile")
        company=v["cdn"].get("company","未知")
        dns_delay=v["cdn"].get("dns_delay",0)
        dns_suc=v["cdn"].get("dns_suc",0)
        Tcpbulddelay=v["tcp"].get("Tcpbulddelay",0)
        tcp_suc_rate=v["tcp"].get("tcp_suc_rate",0)
        li.extend([uuid,domain,ip,t_mobile,company,dns_delay,Tcpbulddelay,dns_suc,tcp_suc_rate])
        data_list.append(li)
    return data_list

