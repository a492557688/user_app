def http_20504(dic,client,server,data):
    key = client + "|" + server  # 默认情况
    if client + "|" + server in data:
        key = client + "|" + server
    elif server + "|" + client in data:
        key = server + "|" + client
    else:  # 第一次
        key = client + "|" + server
        clicachecontrol = dic.get("cc", "未携带")
        clicontenttype = dic.get("ct", "未携带")
        data[key] = {dic["ack"]: {"clicachecontrol": clicachecontrol,
                                  "clicontenttype": clicontenttype,
                                  "btime": int(dic["time"]) / 1000,
                                  "host": server, "first_http_time": dic["time"],
                                  "url": dic.get("host", server) + dic.get("url", "")}}  # url 当没有host时就是ip
        return
    if dic["seq"] in data[key]:  # 已经存在就不创建了不好吧
        # 回应发出的 ququests
        end_http_time = round((int(dic["time"]) - int(data[key][dic["seq"]]["first_http_time"])) / 1000, 2)
        data[key][dic["seq"]]["end_http_time"] = end_http_time
        if dic.get("ct"):
            data[key][dic["seq"]]["host"] = data[key][dic["seq"]]["url"]  # 成功响应 就替换host 作为url 否则就以 server:port 作为url
            data[key][dic["seq"]]["srvcachecontrol"] = dic.get("cc", "未携带")
            srvcontenttype = dic.get("ct")
            data[key][dic["seq"]]["srvcontenttype"] = srvcontenttype
            data[key][dic["seq"]]["srvcookie"] = dic.get("cookie", "")
            data[key][dic["seq"]]["linknum"] = "未知"
            data[key][dic["seq"]]["ack"] = dic["ack"]

def http_20496(dic,client,server,data):
    key = client + "|" + server  # 默认情况
    if client + "|" + server in data:
        key = client + "|" + server
    elif server + "|" + client in data:
        key = server + "|" + client
    else:
        print(key);return
    for i, j in data[key].items():
        print(i, j)