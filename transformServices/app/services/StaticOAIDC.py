from services.StaticOAI import StaticOAI
from services import DCRecord as dc
from services import OAIUtils

class BadDCRecord(Exception):
    pass


class StaticOAIDC(StaticOAI):

    def get(self,resID,identifier):
        result = super().getStaticRecord(resID,identifier)
        return result
        
    def getMetadata(self):
        try:
            self.dcRecord = self.metadata["oai_dc:dc"]
        except KeyError as e:
            raise BadDCRecord("No oai_dc element found. ERROR: " + str(e))
        self.dcRecord = OAIUtils.normalizeRecord(self.dcRecord)
        try:
            self.resultRecord = dc.mapFromDC(self.dcRecord,self.header,self.resultRecord)
        except Exception as e:
            raise BadDCRecord("Could not create default DC record. ERROR: " + str(e))
        return True
        
    
    
