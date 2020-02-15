import os
def getConfigPath(filename=''):
    path = '../config/'
    if not os.path.exists(path):
        os.makedirs(path)
    path += filename
    return path