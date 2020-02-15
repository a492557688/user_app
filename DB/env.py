import os
def getEnvironment():
    ENV = os.getenv('SERVER_ENV')
    if ENV is not None and len(ENV) > 0:
        env = ENV
    else:
        env = 'LOCAL'
    return env

def getMysqlCfg():
    env = getEnvironment()
    if env == 'PROD':
        host = '127.0.0.1'
        port = 3306
        username = 'root'
        password = '123'
    elif env == 'TEST':
        host = '127.0.0.1'
        port = 3306
        username = 'root'
        password = '123'
    else:
        host = '127.0.0.1'
        port = 3306
        username = 'root'
        password = '123'
    return host, port, username, password
if __name__ == '__main__':
        print(getEnvironment())