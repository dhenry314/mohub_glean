#SHSMO_ALL

def map(mapObj):
    mapObj.resultRecord['dataProvider'] = 'State Historical Society of Missouri'
    return mapObj.resultRecord

def getIdentifier(mapObj):
    recordID = mapObj.header['identifier']
    setSpec = 'shsmo_all'
    if 'setSpec' in mapObj.header:
        setSpec = mapObj.header['setSpec']
    identifier = "missouri--urn:data.mohistory.org:" + str(setSpec) + ":" + str(recordID)
    return identifier
