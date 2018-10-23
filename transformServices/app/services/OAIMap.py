import importlib
from flask_restful import Resource, abort

from services.maps import maps
from services.MOHUBBaseRecord import baseRecord
from services.DPLARecord import validate
from gleanomatic import Utils

class BadOAIRecord(Exception):
    pass


class OAIMap(Resource):

    resource = None
    mapper = None
    header = None
    metadata = None
    deleted = False
    resultRecord = False

    def __init__(self,**kwargs):
        self.config = kwargs['config']
    
    def getMapper(self,mapperName):
        mapper = importlib.import_module("services." + str(mapperName))
        return mapper
        
    def getBaseRecord(self,baseName):
        baseRecMod = importlib.import_module("services." + str(baseName))
        return baseRecMod.baseRecord

    def initRecord(self,resID):
        resURL = str(self.config.targetURI) + "/resource/" + str(resID)
        resourceJSON = Utils.getContent(resURL)
        self.resource = Utils.jsonToDict(resourceJSON)
        mapConfig = maps[self.resource["sourceNamespace"]][self.resource["setNamespace"]]
        self.mapper = self.getMapper(mapConfig["mapper"])
        self.resultRecord = self.getBaseRecord(mapConfig["baseRecord"])
        url = str(self.config.targetURI) + "/content/" + str(resID)
        content = Utils.getContent(url)
        try:
            data = Utils.getDictFromXML(content)
        except Exception as e:
            raise Exception(str(e))
        try:
            record = data["OAI-PMH"]["GetRecord"]["record"]
            self.header = record["header"]
            self.metadata = record["metadata"]
        except AttributeError as e:
            try:
                self.header = record["header"]
            except AttributeError as e:
                raise BadOAIRecord(str(e))
            try:
                status = self.header["status"]
            except AttributeError as e:
                raise BadOAIRecord(str(e))
            if status == 'deleted':
                self.deleted = True
            else:
                raise BadOAIRecord("No metadata.  Unknown status: " + str(status))
        return record
    
    def validate(item):
        try:
            validate(item)
        except Exception as e:
            pass
            #logger    
    #override in subclass
    def get(self,resID):
        pass

