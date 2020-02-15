def signal_upd(dic,client,server,siginal_dic):
    # 第一次解析 - 最后一次解析
    key = client + "|" + server
    if client + "|" + server in siginal_dic:
        key = client + "|" + server
    elif server + "|" + client in siginal_dic:
        key = server + "|" + client
    else:
        siginal_dic.setdefault(key, {})
        siginal_dic[key].setdefault("first_sigin_time", dic["time"])  # 首保时间
        siginal_dic[key].setdefault("laster_time", 0)  # 最后一次时间
        siginal_dic[key].setdefault("halength", 0)
        siginal_dic[key].setdefault("send_times", 0)  # 后面加 开始为0
        siginal_dic[key].setdefault("echo_times", 0)  # 后面加 开始为0
        siginal_dic[key].setdefault("protocol", dic["type"])
        siginal_dic[key].setdefault("srv_port", dic["dport"])
        siginal_dic[key].setdefault("srv_ip", dic["dip"])
        siginal_dic[key].setdefault("cliip", dic["sip"])
        siginal_dic[key].setdefault("cli_ip", dic["sport"])
        siginal_dic[key]["halength"] += int(dic["len"])  # 数据长度+1
    # print(dic["sil"])
    # if dic["sip"] =="36.110.224.228" or  dic["dip"] =="36.110.224.228" :print(dic["sip"]+":"+dic["sport"] +"|"+ dic["dip"]+":"+dic["dport"])
    if dic["sip"] + ":" + dic["sport"] + "|" + dic["dip"] + ":" + dic["dport"] == key:
        # 说明是 发送的
        if dic["dip"] == "116.211.203.19": print(dic)
        siginal_dic[key]["send_times"] += 1
        siginal_dic[key]["laster_time"] = dic["time"]

    else:
        siginal_dic[key]["echo_times"] += 1
        siginal_dic[key]["laster_time"] = dic["time"]
        siginal_dic[key]["halength"] += int(dic["len"])  # 数据长度+1

def signal_tcp_20504(dic,client,server,signal):
    '''
    首次信令发送的时间 记录首次信令的发送时间 再记录每次信令传输的时间
    :param signal:
    :return:
    '''
    key = client + "|" + server
    if key in signal:  ##客户端给服务端发送的数据
        pass
    elif server + "|" + client in signal:  # 服务器端给客户端发送的数据
        key = server + "|" + client
        signal[key]["times_20496"].append(dic["time"])
    else:
        key = client + "|" + server
    signal.setdefault(key, {})
    signal[key].setdefault("first_20504", dic["time"])
    signal[key].setdefault("times_20496", [])
    signal[key]["times_20496"].append(dic["time"])

def signal_tcp_20496(dic,client,server,signal):
    '''
    添加信令20496传输的时间
    :param dic:
    :param client:
    :param server:
    :param signal:
    :return:
    '''
    key = client + "|" + server
    signal.setdefault(key, {})
    signal[key].setdefault("times_20496", [])
    signal[key]["times_20496"].append(dic["time"])

