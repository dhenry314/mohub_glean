
from gleanomatic import Utils


"""
   Format type should be one of:
   Book, Film/Video, Manuscript, Maps, Music, Musical Score, Newspapers, Nonmusic, Photograph/Pictorial Works, Serial
"""
def formatWrangler(term):
     types = {
            'book': 'Book', 
            'film': 'Film/Video', 
            'document': 'Manuscript', 
            'map': 'Maps', 
            'music': 'Music', 
            'score': 'Musical Score', 
            'newspaper': 'Newspapers', 
            'nonmusic': 'Nonmusic', 
            'image':'Photograph/Pictorial Works', 
            'serial': 'Serial'
     }
     #redefine format
     typeWords = term.split(' ')
     for typeWord in typeWords:
         typeWord = str(typeWord).lower()
         if typeWord in types:
             return types[typeWord]
         if typeWord == 'manuscript':
             return types['document']
         if (typeWord == 'photo') or (typeWord == 'photograph'):
             return types['image']
         if typeWord == 'video':
             return types['film']
     #default to book if no match
     return 'Book'
     
def normalizeRecord(record,prefix=None):
    if isinstance(record,list):
        result = []
        for item in record:
            newItem = normalizeRecord(item)
            result.append(newItem)
        return result
    if not isinstance(record,dict):
        return record
    result = dict(record)
    for field in record:
        if not record[field]:
            del result[field]
            continue
        if prefix:
            prefixTest = str(prefix) + ":"
            if prefixTest in field:
                newField = field.replace(prefixTest,'')
                result[newField] = normalizeRecord(record[field])
                del result[field]
    return result
    
def validate(item):
    try:
        validate(item)
    except Exception as e:
        pass

