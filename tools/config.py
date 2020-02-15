from tools import path
def readConfig(name):
    filename = path.getConfigPath(name)
    with open(filename, encoding='utf-8') as f:
        content = f.read()
    return content