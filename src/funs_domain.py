def _domain_qr0(dic,qr_0_host):
    host = dic.get("host")
    qr_0_host.setdefault(host, {})
    qr_0_host[host].setdefault("first_dns_time", dic.get("time"))
    qr_0_host[host].setdefault("first_dns_times", 0)
    qr_0_host[host]["first_dns_times"] += 1


def domain_qr0(dic,qr_0_host):
    host = dic.get("host")
    # print("domain_qr0", host, dic.get("time"))
    qr_0_host.setdefault(host, {})
    qr_0_host[host]["first_dns_time"]=dic["time"]
    qr_0_host[host].setdefault("first_dns_times", 0)
    qr_0_host[host]["first_dns_times"] += 1



def domain_qr1(dic,qr_0_host,qr_1_ip):
    host = dic.get("host")
    # print("domain_qr1", host, dic.get("time"))
    qr_0_host.setdefault(host, {})
    dns_delay = round((int(dic.get("time")) - int(qr_0_host[dic["host"]]["first_dns_time"])) / 1000, 2)
    dns_suc = round(1 / qr_0_host[dic["host"]]["first_dns_times"] * 100, 2)

    ips = [i for i in dic.get("ip").split(";") if i]
    for ip in ips:
        qr_1_ip[ip] = {"url": dic.get("host"), "dns_delay": dns_delay, "dns_suc": dns_suc}
        # print(qr_1_ip)
def domain_40962(dic,client,server,qr_1_ip,domain_dic):
    key = client + "|" + server
    # domain_dic[key]["dns"]= qr_1_ip.get(dic["dip"])
    domain_dic.setdefault(key,{})
    domain_dic[key].setdefault("tcp", {})
    domain_dic[key]["tcp"].setdefault("Tcp_first_time", dic["time"])
    domain_dic[key]["tcp"].setdefault("Tcp_first_seq", dic["seq"])


def domain_40296(dic,client,server,domain_dic):
    key = client + "|" + server
    if key not in domain_dic: return  # 192.168 的情况
    domain_dic[key]["tcp"].setdefault("Tcp_complete_seq", dic["seq"])
    domain_dic[key]["tcp"].setdefault("Tcp_complete_time", dic["time"])
    domain_dic[key]["tcp"]["Tcpbulddelay"] = round(
        (int(domain_dic[key]["tcp"]["Tcp_complete_time"]) - int(domain_dic[key]["tcp"]["Tcp_first_time"])) / 1000, 2)
