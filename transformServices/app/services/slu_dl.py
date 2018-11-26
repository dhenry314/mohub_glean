#SLU_DL

def map(mapObj):
    mapObj.resultRecord['dataProvider'] = 'Saint Louis University'
    return mapObj.resultRecord

def getIdentifier(mapObj):
    recordID = mapObj.header['identifier']
    return "missouri--urn:data.mohistory.org:slu_dl:" + str(recordID)
