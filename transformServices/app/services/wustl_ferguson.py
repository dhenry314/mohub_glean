#WUSTL_FERGUSON

def map(mapObj):
    mapObj.resultRecord['dataProvider'] = 'Washington University in Saint Louis'
    sr = mapObj.resultRecord['sourceResource']
    thumb = mapObj.resultRecord['isShownAt']
    recordID = mapObj.header['identifier']
    IDParts = recordID.split(':')
    IDNum = IDParts[-1]
    link = "http://documentingferguson.wustl.edu/omeka/items/show/" + str(IDNum)
    mapObj.resultRecord['isShownAt'] = link
    mapObj.resultRecord['hasView']['@id'] = link
    mapObj.resultRecord['object'] = thumb
    return mapObj.resultRecord
    
def getIdentifier(mapObj):
    recordID = mapObj.header['identifier']
    return "missouri--urn:data.mohistory.org:wustl_ferguson:" + str(recordID)
