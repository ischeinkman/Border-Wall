def _parseFile(name):
    cfg = open(name, 'r')
    paramList = [x.replace(' ','') for x in cfg.read().split('\n') if len(x) > 0]
    prmMap = {}
    for prm in paramList:
        key, value = prm.split('=')
        prmMap[key] = value
    return prmMap

class Config:

    def __init__(self, fileName='CONFIG.txt'):
        self.setUp(fileName)

    def setUp(self, fileName):
        prmMap = _parseFile(fileName)
        self.password = prmMap['password']
        self.key = prmMap['key'].encode('ascii') 
        self.ip = prmMap['ip']
        self.port = int(prmMap['port'])
        
        if 'defaultuser' in prmMap:
            self.defaultuser = prmMap['defaultuser']
        if 'validusers' in prmMap:
            self.validusers = prmMap['validusers'].split(',')
        
