#KCPL_PDR

def map(mapObj):
    link = None
    thumb = None
    for url in mapObj.dcRecord['dc:relation']:
        if url.startswith('https://pendergastkc.org/'):
            link = url
        if url.startswith('<a href='):
            sParts = url.split(' src="')
            parts2 = sParts[1].split('" ')
            thumb = parts2[0]
    mapObj.resultRecord['isShownAt'] = link
    mapObj.resultRecord['hasView']['@id'] = link
    mapObj.resultRecord['sourceResource']['identifier'] = [link]
    mapObj.resultRecord['object'] = thumb
    mapObj.resultRecord['dataProvider'] = 'Kansas City Public Library'
    return mapObj.resultRecord

def getIdentifier(mapObj):
    recordID = mapObj.header['identifier']
    return "missouri--urn:data.mohistory.org:kcpl_pdr:" + str(recordID)
