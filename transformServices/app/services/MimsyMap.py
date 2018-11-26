import importlib
from flask_restful import Resource, abort
import jsonschema
from jsonschema import validate

from services import Utils as serviceUtils
from services.MOHUBBaseRecord import MOHUBBaseRecord
from services.DPLARecord import DPLAschema
from gleanomatic import Utils
import gleanomatic.gleanomaticLogger as gl
from gleanomatic.GleanomaticErrors import GleanomaticError as gError

class BadOAIRecord(gError):
    pass

class MimsyMap(Resource):

    resource = None
    logger = None
    mapper = None
    prefix = None
    header = None
    metadata = None
    deleted = False
    resultRecord = {}
    messages = []

    def __init__(self,**kwargs):
        self.config = kwargs['config']
        self.resultRecord = {}
        self.messages = []
    
    def initRecord(self):
        resURL = str(self.config.targetURI) + "/resource/" + str(self.resID)
        resourceJSON = Utils.getContent(resURL)
        self.resource = Utils.jsonToDict(resourceJSON)
        self.logger = gl.gleanomaticLogger(self.resource['sourceNamespace'],self.resource['setNamespace'],'MimsyMap')
        self.logger.info("Initializing record in MimsyMap.")
        url = str(self.config.targetURI) + "/content/" + str(self.resID)
        try:
            response = Utils.getResponse(url)
            record = Utils.getJSONFromResponse(response)
        except Exception as e:
            raise gError("Could not get data from url",e,self.logger)
        if not self.deleted:
            mbr = MOHUBBaseRecord()
            self.resultRecord = mbr.getBaseRecord()
        return record

    
    """
      Format type should be one of:
      Book, Film/Video, Manuscript, Maps, Music, Musical Score, Newspapers, Nonmusic, Photograph/Pictorial Works, Serial
    """
    def formatWrangler(self,term):
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
         
            
    def validate(self):
        try:
            validate(self.resultRecord, DPLAschema)
        except jsonschema.exceptions.ValidationError as ve:
            msg = serviceUtils.shortValidationError(str(ve))
            self.logger.warning("Could not validate record. ERRORS: " + str(msg))
            self.messages.append("Could not validate record. ERRORS: " + str(msg))
        return True

    def getRights(self,mimsyRecord):
        term = 'NKC'
        if 'rights' in mimsyRecord['_source']:
            testTerm = mimsyRecord['_source']['rights']
            if isinstance(testTerm,str):
                if len(testTerm) > 2:
                    term = testTerm
        rights = 'http://rightsstatements.org/vocab/' + str(term) + '/1.0/'
        return rights
        
    def getFormat(self,mimsyRecord):
        recordType = mimsyRecord['_source']['mimsyRecordType']
        formatType = None
        if recordType == "P":
            formatType = 'Photograph/Pictorial Works'
        if recordType == "A":
            formatType = 'Manuscript'
        if recordType == "M":
            formatType = "Film/Video"
        if recordType == "L":
            formatType = "Book"
        return formatType
             
    #override in subclass
    def get(self,resID):
        self.resID = resID
        mimsyRecord = self.initRecord()
        if not self.deleted:
            mbr = MOHUBBaseRecord()
            self.resultRecord = mbr.getBaseRecord()
        link = mimsyRecord['_source']['itemID']
        thumb = mimsyRecord['_source']['thumbnail']
        self.resultRecord['isShownAt'] = link
        self.resultRecord['object'] = thumb
        self.resultRecord['hasView']['@id'] = link
        self.resultRecord['dataProvider'] = 'Missouri Historical Society'
        sr = self.resultRecord['sourceResource']
        sr['rights'] = self.getRights(mimsyRecord)
        sr['title'] = [mimsyRecord['_source']['label']]
        sr['description'] = [mimsyRecord['_source']['description']]
        #subject
        subjects = []
        for subject in mimsyRecord['_source']['subjects']:
            subjects.append({'name':subject['label']})
        sr['subject'] = subjects
        #temporal
        sr['temporal'] = [{
                           "start": mimsyRecord['_source']['date1'], 
                           "end": mimsyRecord['_source']['date1'],
                           "displayDate": mimsyRecord['_source']['date_str']
                         }]
        sr['@id'] = mimsyRecord['_source']['itemID']
        sr['format'] = self.getFormat(mimsyRecord)
        sr['specType'] = [sr['format']]
        sr['identifier'] = mimsyRecord['_source']['ids']
        sr['creator'] = mimsyRecord['_source']['makers']
        self.resultRecord['sourceResource'] = sr
        itemID = mimsyRecord['_source']['itemID']
        resourceID = itemID.replace('http://collections.mohistory.org/resource/','')
        self.resultRecord['@id'] = 'missouri--urn:data.mohistory.org:MHM_all:oai:collections.mohistory.org:' + str(resourceID)
        return self.resultRecord
