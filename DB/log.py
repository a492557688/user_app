import  logging
formatter=logging.Formatter('%(asctime)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%m-%d %H:%M:%S %p',)
mysqlfilename = f'../logs/mysqllogs.log'
scriptfilename = f'../logs/scriptlogs.log'
#创建handle
streamHandler=logging.StreamHandler()
mytsqlfileHandler=logging.FileHandler(mysqlfilename)
scriptHandler=logging.FileHandler(scriptfilename)
#为handle 设置格式
streamHandler.setFormatter(formatter)  #
mytsqlfileHandler.setFormatter(formatter)
scriptHandler.setFormatter(formatter)

#创建使用的 logger
logger1_mysql=logging.getLogger('mysql')
logger2_script=logging.getLogger('script')
# 为使用的logger 存handle  一个控制台 一个本地
logger1_mysql.addHandler(streamHandler)
logger1_mysql.addHandler(mytsqlfileHandler)
logger2_script.addHandler(streamHandler)
logger2_script.addHandler(scriptHandler)
#为logger 设置等级
logger1_mysql.setLevel(10)
logger2_script.setLevel(10)