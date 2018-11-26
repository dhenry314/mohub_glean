#MSU_ALL

def map(mapObj):
    mapObj.resultRecord['dataProvider'] = 'Missouri State University'
    return mapObj.resultRecord

def getIdentifier(mapObj):
    recordID = mapObj.header['identifier']
    return "missouri--urn:data.mohistory.org:msu_all:" + str(recordID)
