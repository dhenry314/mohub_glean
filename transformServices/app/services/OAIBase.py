import importlib
from flask_restful import Resource, abort
import jsonschema
from jsonschema import validate

from services import Utils as serviceUtils
from services.maps import maps
from services.MOHUBBaseRecord import MOHUBBaseRecord
from services.DPLARecord import DPLAschema
from gleanomatic import Utils
import gleanomatic.gleanomaticLogger as gl
from gleanomatic.GleanomaticErrors import GleanomaticError as gError

class BadOAIRecord(gError):
    pass

class OAIBase(Resource):

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
    
    def getMapper(self,mapperName):
        try:
            mapper = importlib.import_module("services." + str(mapperName))
        except Exception as e:
            raise gError("Could not load mapper: " + str(mapperName),e,self.logger)
        return mapper
        
    def getRecord(self,data):
        record = None
        try:
            record = data["OAI-PMH"]["GetRecord"]["record"]
        except KeyError as e:
            raise gError("Could not find OAI in data.",e,self.logger)
        return record
        
    def setIdentifier(self):
        if '@id' not in self.resultRecord:
            self.resultRecord['@id'] = self.mapper.getIdentifier(self)
        elif not self.resultRecord['@id']:
            self.resultRecord['@id'] = self.mapper.getIdentifier(self)
        return True
        
    def initRecord(self):
        resURL = str(self.config.targetURI) + "/resource/" + str(self.resID)
        resourceJSON = Utils.getContent(resURL)
        self.resource = Utils.jsonToDict(resourceJSON)
        self.logger = gl.gleanomaticLogger(self.resource['sourceNamespace'],self.resource['setNamespace'],'OAIMap')
        self.logger.info("Initializing record in OAIBase.")
        if self.resource["sourceNamespace"] not in maps:
            raise BadOAIRecord("No map config found for " + str(self.resource['sourceNamespace'])  + " map: " + str(maps))
        mapConfig = maps[self.resource["sourceNamespace"]][self.resource["setNamespace"]]
        if 'prefix' in mapConfig:
            self.prefix = mapConfig['prefix']
        self.mapper = self.getMapper(mapConfig["mapper"])
        url = str(self.config.targetURI) + "/content/" + str(self.resID)
        content = Utils.getContent(url)
        try:
            data = Utils.getDictFromXML(content)
        except Exception as e:
            raise gError("Could not get dict from xml.",e,self.logger)
        record = self.getRecord(data)
        try:
            self.header = record["header"]
            self.metadata = record["metadata"]
        except KeyError as e:
            try:
                self.header = record["header"]
            except KeyError as e:
                raise BadOAIRecord("Could not find metadata or header in record.",e,self.logger)
            try:
                status = self.header["status"]
            except KeyError as e:
                try:
                    status = self.header["@status"]
                except KeyError as e:
                    raise BadOAIRecord("No status in header.",e,self.logger)
            if status == 'deleted':
                self.deleted = True
            else:
                raise BadOAIRecord("No metadata.  Unknown status: " + str(status),None,self.logger)
        if not self.deleted:
            mbr = MOHUBBaseRecord()
            self.resultRecord = mbr.getBaseRecord()
            self.resultRecord['@id'] = serviceUtils.DPLAID(self.resultRecord['isShownAt'])
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
         
    def reconcileRecord(self):
        self.setIdentifier()
        if self.deleted:
            self.resultRecord['status'] = 'deleted'
        else:
            self.validate()
        if len(self.messages) > 0:
            self.resultRecord['admin'] = {'messages': self.messages}
        return True
        
    def validate(self):
        try:
            validate(self.resultRecord, DPLAschema)
        except jsonschema.exceptions.ValidationError as ve:
            msg = serviceUtils.shortValidationError(str(ve))
            self.logger.warning("Could not validate record. ERRORS: " + str(msg))
            self.messages.append("Could not validate record. ERRORS: " + str(msg))
        return True

      
    #override in subclass
    def get(self,resID):
        pass

