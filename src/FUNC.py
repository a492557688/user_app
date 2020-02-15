def  linesStr_to_lineDic(lineString):
    lineString=lineString.strip()
    lines = lineString.split("\n")
    lines = [line.strip() for line in lines]
    return [{dengyustr.split("=")[0]:dengyustr.split("=")[1] for dengyustr in line.split("||") }   for line in lines  ]
def  lineList_to_lineDic(lineList):
    lines = [line.strip() for line in lineList]
    return [{dengyustr.split("=")[0]:dengyustr.split("=")[1] for dengyustr in line.split("||") }   for line in lines  ]


if __name__ == '__main__':
    strs="""dport=80||flag=40962||len=74||ack=0||dip=101.226.26.253||load_len=0||time=1581382018500284||sip=10.0.0.2||type=tcp||sport=48768||win=65535||seq=1585350604
dport=48768||flag=20498||len=54||ack=1585350605||dip=10.0.0.2||load_len=0||time=1581382018545540||sip=101.226.26.253||type=tcp||sport=80||win=65535||seq=10366
dport=80||flag=20496||len=54||ack=10367||dip=101.226.26.253||load_len=0||time=1581382018546192||sip=10.0.0.2||type=tcp||sport=48768||win=65535||seq=1585350605"""
    print(linesStr_to_lineDic(strs))