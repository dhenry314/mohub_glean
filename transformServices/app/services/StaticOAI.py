import importlib
from flask_restful import Resource, abort

from services.OAIBase import OAIBase, BadOAIRecord
from services.maps import maps
from services.MOHUBBaseRecord import MOHUBBaseRecord
from gleanomatic import Utils


class StaticOAI(OAIBase):

    resource = None
    oaiRecord = None
    resID = None
    identifier = None
    mapper = None
    prefix = None
    header = None
    metadata = None
    deleted = False
    resultRecord = {}

    def __init__(self,**kwargs):
        self.config = kwargs['config']
        self.resultRecord = {}
        
    def getRecord(self,data):
        for item in data['records']['record']:
            if item['header']['identifier'] == self.identifier:
                return item
        return None
        
    def getStaticRecord(self,resID,identifier):
        self.resID = resID
        self.identifier = identifier
        record = self.initRecord()
        if self.metadata:
            self.getMetadata()
        try:
            self.resultRecord = self.mapper.map(self)
        except Exception as e:
            raise BadOAIRecord("Could not map record.",e,self.logger)
        if self.deleted:
            self.resultRecord['status'] = 'deleted'
        return self.resultRecord
