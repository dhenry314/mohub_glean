from gleanomatic import Utils
from services import OAIUtils

class BadMODSRecord(Exception):
    pass


#define default values for the target record
def mapFromMODS(mods,header,resultRecord):
    # define link and thumbnail
    link = None
    thumbnail = None
    if 'location' in mods:
        if 'url' in mods['location']:
            for item in mods['location']['url']:
                if isinstance(item, str):
                    link = item
                if isinstance(item, dict):
                    if '@access' in item:
                        if str(item['@access']).lower() == 'preview':
                            thumbnail = item['#text']
                        if str(item['@access']).lower() == 'object in context':
                            link = item['#text']
                        if str(item['@access']).lower() == 'raw object':
                            link = item['#text']
        elif isinstance(mods['location'],list):
            for item in mods['location']:
                if 'url' in item: 
                    if '@access' in item['url']:
                        if str(item['url']['@access']).lower() == 'preview':
                            thumbnail = item['url']['#text']
                        if str(item['url']['@access']).lower() == 'object in context':
                            link = item['url']['#text']
                        if str(item['url']['@access']).lower() == 'raw object':
                            link = item['url']['#text']
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
    if 'accessCondition' in mods:
        if isinstance(mods['accessCondition'],str):
            rights = mods['accessCondition']
        elif '#text' in mods['accessCondition']:
            rights = mods['accessCondition']['#text']
    sr['rights'] = rights
    #define the title
    title = []
    if 'titleInfo' in mods:
        if isinstance(mods['titleInfo'],list):
            title.append(mods['titleInfo'][0]['title'])
        elif 'title' in mods['titleInfo']:
            title.append(mods['titleInfo']['title'])
        sr['title'] = title
    #define subjects
    subjects = []
    temporal = []
    if 'subject' in mods:
        if 'topic' in mods['subject']:
            if isinstance(mods['subject']['topic'],dict):
                if 'topic' in mods['subject']['topic']:
                    subjects.append({'name':mods['subject']['topic']['topic']})
            elif isinstance(mods['subject']['topic'],str):
                subjects.append({'name':mods['subject']['topic']})
            elif isinstance(mods['subject']['topic'],list):
                for record in mods['subject']['topic']:
                    if isinstance(record,str):
                        subjects.append({"name":record})
                    elif 'topic' in record:
                        if isinstance(record['topic'],str):
                            subjects.append({"name":record['topic']})
                        elif 'name' in record['topic']:
                            subjects.append({"name":record['topic']['name']})
        if 'geographic' in mods['subject']:
            if isinstance(mods['subject']['geographic'],dict):
                if 'geographic' in mods['subject']['geographic']:
                    subjects.append({'name':mods['subject']['geographic']['geographic']})
            elif isinstance(mods['subject']['geographic'],str):
                subjects.append({'name':mods['subject']['geographic']})
        if 'temporal' in mods['subject']:
            if isinstance(mods['subject']['temporal'],str):
                temporal.append({"displayDate":mods['subject']['temporal']})
        elif isinstance(mods['subject'],list):
            for item in mods['subject']:
                if isinstance(item,str):
                    subjects.append({"name":item})
                    continue
                if 'topic' in item:
                    subjects.append({"name":item['topic']})
                    continue
                if 'name' in item:
                    if isinstance(item['name'],str):
                        subjects.append({"name":item['name']})
                        continue
                    if 'displayForm' in item['name']:
                        subjects.append({"name":item['name']['displayForm']})
                    elif 'namePart' in item['name']:
                        subjects.append({"name":item['name']['namePart']})
                if 'geographic' in item:
                    subjects.append({"name":item['geographic']})
                    continue
    sr['subject'] = subjects
    #define description
    description = []
    if 'abstract' in mods:
        description.append(mods['abstract'])
    sr['description'] = description
    #define creator(s)
    creator = []
    if 'name' in mods:
        if isinstance(mods['name'],list):
            for name in mods['name']:
                if 'role' in name:
                    if 'roleTerm' in name['role']:
                        if str(name['role']['roleTerm']).lower() == 'creator':
                            if 'namePart' in name:
                                creator.append(name['namePart'])
        elif 'role' in mods['name']:
            if 'roleTerm' in mods['name']['role']:
                if str(mods['name']['role']['roleTerm']).lower() == 'creator':
                    if 'namePart' in mods['name']:
                        if isinstance(mods['name']['namePart'],list):
                            creator.append(mods['name']['namePart'][0])
                        elif isinstance(mods['name']['namePart'],str):
                            creator.append(mods['name']['namePart'])
    #define temporal (when created)
    if 'originInfo' in mods:
        if 'publisher' in mods['originInfo']:
            creator = mods['originInfo']['publisher']
        if 'dateIssued' in mods['originInfo']:
            start = ''
            end = ''
            displayDate = ''
            for part in mods['originInfo']['dateIssued']:
                if '@point' in part:
                    if str(part['@point']).lower() == 'start':
                        start = part['#text']
                    elif str(part['@point']).lower() == 'end':
                        end = part['#text']
            if len(start + end) >0:
                displayDate = str(start) + "/" + str(end)
                temporal.append({"start":start,"end":end,"displayDate":displayDate})
    sr['temporal'] = temporal            
    sr['creator'] = creator
    #define format
    typeOfResource = sr['format']
    if 'typeOfResource' in mods:
        if isinstance(mods['typeOfResource'],str):
            typeOfResource = OAIUtils.formatWrangler(mods['typeOfResource'])
    if typeOfResource == 'Book':
        if 'genre' in mods:
            if isinstance(mods['genre'],dict):
                if '#text' in mods['genre']:
                    typeOfResource = OAIUtils.formatWrangler(mods['genre']['#text'])
            if isinstance(mods['genre'],str):
                typeOfResource = OAIUtils.formatWrangler(mods['genre'])
            elif isinstance(mods['genre'],list):
                for item in mods['genre']:
                    if isinstance(item,str):
                        typeOfResource = OAIUtils.formatWrangler(item)
                    elif isinstance(item,dict):
                        if '#text' in item:
                            typeOfResource = OAIUtils.formatWrangler(item['#text'])
                    if typeOfResource is not 'Book':
                        break
                
    if typeOfResource:
        sr['format'] = typeOfResource
    sr['specType'] = [sr['format']]    
    resultRecord['sourceResource'] = sr
    return resultRecord
