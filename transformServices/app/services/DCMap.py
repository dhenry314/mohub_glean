from gleanomatic import Utils
from services.OAIBase import OAIBase, BadOAIRecord
from services import DCRecord as dc
from services import OAIUtils

class BadDCRecord(BadOAIRecord):
    pass

class DCMap(OAIBase):

    dcRecord = {}
    resID = None

    def get(self,resID):
        self.resID = resID
        record = self.initRecord()
        if not self.deleted:
            try:
                self.dcRecord = self.metadata["oai_dc:dc"]
            except KeyError as e:
                raise BadDCRecord("No oai_dc:dc element found.",e,self.logger)
            try:
                self.dcRecord = OAIUtils.normalizeRecord(self.dcRecord)
            except Exception as e:
                raise BadDCRecord("Could not normalize record.",e,self.logger)
        if self.metadata:
            try:
                self.resultRecord = dc.mapFromDC(self.dcRecord,self.header,self.resultRecord)
            except Exception as e:
                raise BadDCRecord("Could not create default DC record.",e,self.logger)
        try:
            self.resultRecord = self.mapper.map(self)
        except Exception as e:
            raise BadDCRecord("Could not map DC record.",e,self.logger)
        self.reconcileRecord()
        return self.resultRecord
        
