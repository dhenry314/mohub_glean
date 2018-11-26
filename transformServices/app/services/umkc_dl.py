#UMKC_DL

def map(mapObj):
    mapObj.resultRecord['dataProvider'] = 'University of Missouri - Kansas City'
    if 'mods:identifier' in mapObj.modsRecord:
        #redefine link and thumbnail
        link = mapObj.modsRecord['mods:identifier']['#text']
        thumbnail = str(link) + "/datastream/TN/view"
        mapObj.resultRecord['isShownAt'] = link
        mapObj.resultRecord['object'] = thumbnail
        mapObj.resultRecord['hasView']['@id'] = link
        sr = mapObj.resultRecord['sourceResource']
        sr['identifier'] = [link]
    mapObj.resultRecord['@id'] = getIdentifier(mapObj.header['identifier'])
    return mapObj.resultRecord

def getIdentifier(recordID):
    #parse out IDNum
    parts = recordID.split(":")
    IDNum = parts[-1]
    return "missouri--urn:data.mohistory.org:umkc_dl:oai:dl.mospace.umsystem.edu/umkc/:" + str(IDNum)
