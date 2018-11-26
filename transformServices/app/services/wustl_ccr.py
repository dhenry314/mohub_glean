#WUSTL_CCR

def map(mapObj):
    link = None
    thumb = None
    for url in mapObj.dcRecord['dc:identifier']:
        if url.startswith('http://repository.wustl.edu/'):
            link = url
        if url.startswith('http://digital.wustl.edu/'):
            thumb = url
    mapObj.resultRecord['isShownAt'] = link
    mapObj.resultRecord['hasView']['@id'] = link
    mapObj.resultRecord['sourceResource']['identifier'] = [link]
    mapObj.resultRecord['object'] = thumb
    mapObj.resultRecord['dataProvider'] = 'Washington University in Saint Louis'
    return mapObj.resultRecord

def getIdentifier(mapObj):
    recordID = mapObj.header['identifier']
    return "missouri--urn:data.mohistory.org:wustl_ccr:" + str(recordID)
