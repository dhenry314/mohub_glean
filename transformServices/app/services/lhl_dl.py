#LHL_DL
from services import Utils

def map(mapObj):
    mapObj.resultRecord['dataProvider'] = 'Linda Hall Library'
    return mapObj.resultRecord

def getIdentifier(mapObj):
    recordID = mapObj.header['identifier']
    setSpec = 'lhl_dl'
    if 'setSpec' in mapObj.header:
        setSpec = mapObj.header['setSpec']
    identifier = "missouri--urn:data.mohistory.org:" + str(setSpec) + ":" + str(recordID)
    return identifier
