from services.OAIMap import OAIMap

class MODSMap(OAIMap):

    modsRecord = None

    def get(self,resID):
        record = self.initRecord(resID)
        try:
            self.modsRecord = self.metadata["mods"]
        except AttributeError as e:
            raise BadOAIRecord("No mods element found. ERROR: " + str(e))
        self.resultRecord = self.mapFromMODS()
        self.resultRecord = self.mapper.map(self)
        return self.resultRecord

    def mapFromMODS(self):
        pass
