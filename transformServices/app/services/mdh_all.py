#MDH_ALL

def map(mapObj):
    if 'dc:publisher' in mapObj.dcRecord:
        mapObj.resultRecord['dataProvider'] = str(mapObj.dcRecord['dc:publisher']) + ' through Missouri Digital Heritage'
    else:
        mapObj.resultRecord['dataProvider'] = 'Missouri Digital Heritage'
    return mapObj.resultRecord

def getIdentifier(mapObj):
    recordID = mapObj.header['identifier']
    return "missouri--urn:data.mohistory.org:mdh_all:" + str(recordID)
