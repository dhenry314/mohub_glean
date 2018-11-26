from services import Utils
from services import OAIUtils


class BadDCRecord(Exception):
    pass


#define default values for the target record
def mapFromDC(dc,header,resultRecord):
    # define link and thumbnail
    link = None
    thumbnail = None
    if 'dc:identifier' in dc:
        if isinstance(dc['dc:identifier'],list):
            for item in dc['dc:identifier']:
                if item.startswith('http'):
                    link = item
        elif dc['dc:identifier'].startswith('http'):
            link = dc['dc:identifier']
    if link:
        if '/cdm/' in link:
            thumbnail = getCDMThumb(link)
    resultRecord['isShownAt'] = link
    resultRecord['object'] = thumbnail
    resultRecord['hasView']['@id'] = link
    # grab the current sourceResource
    sr = resultRecord['sourceResource']
    sr['identifier'] = [link]
    if 'identifier' in header:
        sr['@id'] = header['identifier']
    #define rights statement
    rights = ''
    if 'dc:rights' in dc:
        if isinstance(dc['dc:rights'],dict):
            if 'a' in dc['dc:rights']:
                rights = dc['dc:rights']['a']['#text']
        else:
            rights = dc['dc:rights']
    sr['rights'] = rights
    #define the title
    if 'dc:title' in dc:
        if isinstance(dc['dc:title'],list):
            sr['title'] = dc['dc:title']
        else:
            sr['title'] = [dc['dc:title']]
    #define description
    if 'dc:description' in dc:
        sr['description'] = [dc['dc:description']]
    #define subjects
    subject = []
    if 'dc:subject' in dc:
        if isinstance(dc['dc:subject'],str):
            parts = dc['dc:subject'].split(";")
            for part in parts:
                subject.append({"name":part})
    sr['subject'] = subject
    #define language
    language = []
    if 'dc:language' in dc:
        if isinstance(dc['dc:language'],str):
            terms = dc['dc:language'].split(";")
        else:
            terms = dc['dc:language']
        for term in terms:
            langResult = Utils.getISO639(term)
            if langResult:
                parts = langResult.split('|')
                language.append({"iso639_3": parts[0], "name": parts[1]})
    if len(language) > 0:
        sr['language'] = language
    #define temporal
    temporal = []
    if 'dc:date' in dc:
        if isinstance(dc['dc:date'],list):
            for item in dc['dc:date']:
                temporal.append({"displayDate": item})
        else:
            temporal.append({"displayDate": dc['dc:date']})
    sr['temporal'] = temporal                
    resultRecord['sourceResource'] = sr
    return resultRecord

def getCDMThumb(url):
    thumbURL = None
    protocol = None
    if url.startswith('http://'):
        url = url[7:]
        protocol = 'http://'
    if url.startswith('https://'):
        url = url[8:]
        protocol = 'https://'
    parts =  url.split('/')
    domain = parts[0]
    dParts = url.split('/collection/')
    suffix = '/collection/' + str(dParts[1])
    thumbURL = str(protocol) + str(domain) + '/utils/getthumbnail' + str(suffix)
    return thumbURL
            
        
