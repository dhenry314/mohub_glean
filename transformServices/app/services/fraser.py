#FRASER from FRBSTL

def map(mapObj):
    mapObj.resultRecord['dataProvider'] = 'Federal Reserve Bank of St. Louis'
    return mapObj.resultRecord

def getIdentifier(mapObj):
    recordID = mapObj.header['identifier']
    return "missouri--urn:data.mohistory.org:frbstl_fraser:" + str(recordID)

