#WUSTL_OMEKA

def map(mapObj):
    mapObj.resultRecord['dataProvider'] = 'Washington University in Saint Louis'
    sr = mapObj.resultRecord['sourceResource']
    thumb = mapObj.resultRecord['isShownAt']
    recordID = mapObj.header['identifier']
    IDParts = recordID.split(':')
    IDNum = IDParts[-1]
    link = "http://omeka.wustl.edu/omeka/items/show/" + str(IDNum)
    mapObj.resultRecord['isShownAt'] = link
    mapObj.resultRecord['hasView']['@id'] = link
    mapObj.resultRecord['object'] = thumb
    return mapObj.resultRecord

def getIdentifier(mapObj):
    recordID = mapObj.header['identifier']
    setSpec = 'wustl_omeka'
    if 'setSpec' in mapObj.header:
        testSet = mapObj.header['setSpec']
        if not testSet.isdigit():
            setSpec = testSet
    identifier = "missouri--urn:data.mohistory.org:" + str(setSpec) + ":" + str(recordID)
    return identifier
