from services.OAIMap import OAIMap

class DCMap(OAIMap):

    dcRecord = None

    def get(self,resID):
        record = self.pullRecord(resID)
        try:
            self.dcRecord = self.metadata["dc"]
        except AttributeError as e:
            raise BadOAIRecord("No dc element found. ERROR: " + str(e))
        return self.dcRecord
