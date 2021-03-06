import importlib
from flask_restful import Resource, abort

from services.maps import maps
from services.MOHUBBaseRecord import MOHUBBaseRecord
from services.DPLARecord import validate
from gleanomatic import Utils
import gleanomatic.gleanomaticLogger as gl

class BadOAIRecord(Exception):
    pass


class OAIMap(Resource):

    resource = None
    mapper = None
    prefix = None
    header = None
    metadata = None
    deleted = False
    resultRecord = {}

    def __init__(self,**kwargs):
        self.config = kwargs['config']
        self.resultRecord = {}
    
    def getMapper(self,mapperName):
        try:
            mapper = importlib.import_module("services." + str(mapperName))
        except Exception as e:
            self.logger.critical("Could not load mapper: " + str(mapperName))
        return mapper
        
    def initRecord(self,resID):
        resURL = str(self.config.targetURI) + "/resource/" + str(resID)
        resourceJSON = Utils.getContent(resURL)
        self.resource = Utils.jsonToDict(resourceJSON)
        self.logger = gl.gleanomaticLogger(self.resource['sourceNamespace'],self.resource['setNamespace'],'OAIMap')
        self.logger.info("Initializing record in OAIMap.")
        mapConfig = maps[self.resource["sourceNamespace"]][self.resource["setNamespace"]]
        if 'prefix' in mapConfig:
            self.prefix = mapConfig['prefix']
        self.mapper = self.getMapper(mapConfig["mapper"])
        url = str(self.config.targetURI) + "/content/" + str(resID)
        content = Utils.getContent(url)
        try:
            data = Utils.getDictFromXML(content)
        except Exception as e:
            self.logger.critical("Could not get dict from xml. ERROR: " + str(e))
            raise Exception(str(e))
        try:
            record = data["OAI-PMH"]["GetRecord"]["record"]
            self.header = record["header"]
            self.metadata = record["metadata"]
        except KeyError as e:
            try:
                self.header = record["header"]
            except KeyError as e:
                self.logger.critical("Could not find metadata or header in record.")
                raise BadOAIRecord(str(e))
            try:
                status = self.header["status"]
            except KeyError as e:
                try:
                    status = self.header["@status"]
                except KeyError as e:
                    self.logger.critical("No status in header.")
                    raise BadOAIRecord(str(e))
            if status == 'deleted':
                self.deleted = True
            else:
                self.logger.critical("Unknown status type: " + str(status))
                raise BadOAIRecord("No metadata.  Unknown status: " + str(status))
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
    
    def validate(item):
        try:
            validate(item)
        except Exception as e:
            pass
            #logger    
    
    #override in subclass
    def get(self,resID):
        pass

