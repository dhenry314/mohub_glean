
class ServiceResolver():

    serviceName = None
    resPath = None 

    def __init__(self,serviceName,resPath):
        self.serviceName = serviceName
        self.resPath = resPath

    def resolve(self):
        service = None
        if str(self.serviceName) == 'HelloWorld':
            from . import HelloWorld as hw
            service = hw.HelloWorld()
            return service
