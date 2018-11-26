#SLPL_DL
from services import DCRecord

def map(mapObj):
    mapObj.resultRecord['dataProvider'] = 'Saint Louis Public Library'
    if mapObj.deleted:
        return mapObj.resultRecord
    # define link and thumbnail
    dc = mapObj.dcRecord
    link = None
    thumbnail = None
    if 'dc:identifier' in dc:
        if isinstance(dc['dc:identifier'],list):
            for item in dc['dc:identifier']:
                if 'http://collections.slpl.org/cdm/' in item:
                    link = item
        elif 'http://collections.slpl.org/cdm/' in dc['dc:identifier']:
            link = dc['dc:identifier']
    if link:
        if '/cdm/' in link:
            thumbnail = DCRecord.getCDMThumb(link)
    mapObj.resultRecord['isShownAt'] = link
    mapObj.resultRecord['object'] = thumbnail
    mapObj.resultRecord['hasView'] = {'@id': link}
    return mapObj.resultRecord

def getIdentifier(mapObj):
    recordID = mapObj.header['identifier']
    return "missouri--urn:data.mohistory.org:slpl_dl:" + str(recordID)
