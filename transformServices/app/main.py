from flask import Flask
from flask_restful import Api, Resource, abort

app = Flask('__main__')
api = Api(app)

from gleanomatic.configure import appConfig as config
from services.HelloWorld import HelloWorld as hw
from services.MODSMap import MODSMap as mm

api.add_resource(hw,
                 "/HelloWorld/<string:fullName>",
                 methods=['GET'],
                 resource_class_kwargs={ 'config': config })
                 
api.add_resource(mm,
                 "/MODSMap/<int:resID>",
                 methods=['GET'],
                 resource_class_kwargs={ 'config': config })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
