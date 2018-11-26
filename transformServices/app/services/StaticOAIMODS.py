from services.StaticOAI import StaticOAI
from services import MODSRecord as mods
from services import OAIUtils

class BadMODSRecord(Exception):
    pass


class StaticOAIMODS(StaticOAI):

    modsRecord = {}

    def get(self,resID,identifier):
        result = super().getStaticRecord(resID,identifier)
        return result
        
    def getMetadata(self):
        try:
            self.modsRecord = self.metadata["mods"]
        except KeyError as e:
            raise BadMODSRecord("No mods element found. ERROR: " + str(e))
        self.modsRecord = OAIUtils.normalizeRecord(self.modsRecord)
        try:
            self.resultRecord = mods.mapFromDC(self.modsRecord,self.header,self.resultRecord)
        except Exception as e:
            raise BadMODSRecord("Could not create default MODS record. ERROR: " + str(e))
        return True
        
    
    
