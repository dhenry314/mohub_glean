from flask import Flask
from flask_restful import Api, Resource, abort

app = Flask('__main__')
api = Api(app)

from gleanomatic.configure import appConfig as config
from services.HelloWorld import HelloWorld as hw
from services.MODSMap import MODSMap as mm
from services.DCMap import DCMap as dm
from services.StaticOAIDC import StaticOAIDC as soDC
from services.StaticOAIMODS import StaticOAIMODS as soMODS
from services.MimsyMap import MimsyMap as mimsy

api.add_resource(hw,
                 "/HelloWorld/<string:fullName>",
                 methods=['GET'],
                 resource_class_kwargs={ 'config': config })
                 
api.add_resource(mm,
                 "/MODSMap/<int:resID>",
                 methods=['GET'],
                 resource_class_kwargs={ 'config': config })
                 
api.add_resource(dm,
                 "/DCMap/<int:resID>",
                 methods=['GET'],
                 resource_class_kwargs={ 'config': config })
                 
api.add_resource(soDC,
                 "/StaticOAIDC/<int:resID>/DCMap/<string:identifier>",
                 methods=['GET'],
                 resource_class_kwargs={ 'config': config })
                 
api.add_resource(soMODS,
                 "/StaticOAIMODS/<int:resID>/MODSMap/<string:identifier>",
                 methods=['GET'],
                 resource_class_kwargs={ 'config': config })
                 
api.add_resource(mimsy,
                 "/MimsyMap/<int:resID>",
                 methods=['GET'],
                 resource_class_kwargs={ 'config': config })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
