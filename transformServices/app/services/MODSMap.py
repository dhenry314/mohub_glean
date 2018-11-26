from gleanomatic import Utils
from services.OAIBase import OAIBase, BadOAIRecord
from services import MODSRecord as mods
from services import OAIUtils

class BadMODSRecord(BadOAIRecord):
    pass

class MODSMap(OAIBase):

    modsRecord = {}
    resID = None

    def get(self,resID):
        self.resID = resID
        record = self.initRecord()
        metadataKey = 'mods'
        if self.prefix:
            metadataKey = str(self.prefix) + ":mods"
        if not self.deleted:
            try:
                self.modsRecord = self.metadata[metadataKey]
            except KeyError as e:
                 try:
                     self.modsRecord = self.metadata['mods']
                 except KeyError as e:
                     raise BadMODSRecord("No mods element found.",e,self.logger)
            try:
                self.modsRecord = OAIUtils.normalizeRecord(self.modsRecord,self.prefix)
            except Exception as e:
                raise BadMODSRecord("Could not normalize MODS record.",e,self.logger)
        if self.metadata:
            try:
                self.resultRecord = mods.mapFromMODS(self.modsRecord,self.header,self.resultRecord)
            except Exception as e:
                raise BadMODSRecord("Could not create default MODS record.",e,self.logger)
        try:
            self.resultRecord = self.mapper.map(self)
        except Exception as e:
            raise BadMODSRecord("Could not map MODS record.",e,self.logger)
        self.reconcileRecord()
        return self.resultRecord
        
