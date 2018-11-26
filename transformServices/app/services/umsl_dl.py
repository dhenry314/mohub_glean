#UMSL_DL

def map(mapObj):
    mapObj.resultRecord['dataProvider'] = 'University of Missouri - Saint Louis'
    if 'identifier' in mapObj.modsRecord:
        #redefine link and thumbnail
        if '#text' in mapObj.modsRecord['identifier']:
            link = mapObj.modsRecord['identifier']['#text']
        else:
            link = mapObj.modsRecord['identifier']
        thumbnail = str(link) + "/datastream/TN/view"
        mapObj.resultRecord['isShownAt'] = link
        mapObj.resultRecord['object'] = thumbnail
        mapObj.resultRecord['hasView']['@id'] = link
        sr = mapObj.resultRecord['sourceResource']
        sr['identifier'] = [link]
    return mapObj.resultRecord

def getIdentifier(mapObj):
    recordID = mapObj.header['identifier']
    return "missouri--urn:data.mohistory.org:umkc_dl:" + str(recordID)
