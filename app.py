from flasgger import Swagger
from flask import Flask, jsonify, Blueprint
from flask_cors import CORS
from flask_restful import Api
from werkzeug.exceptions import HTTPException, default_exceptions
from views.recomendations import Recomendations

UNKNOWN_ERROR = 'Oops something went wrong!'

CRYPTO_V1 = '/crypto/v1/%s'

def json_app(flask_app):
    def error_handling(error):
        if isinstance(error, HTTPException):
            result = {
                'code': error.code,
                'message': error.description
            }
        else:
            result = {
                'code': 500,
                'message': UNKNOWN_ERROR
            }
        resp = jsonify(result)
        resp.status_code = result['code']
        return resp

    for code in default_exceptions.keys():
        flask_app.register_error_handler(code, error_handling)

    return flask_app


application = json_app(Flask(__name__))

application.config['SWAGGER'] = {
    'title': 'Crypto', 'specs_route': CRYPTO_V1 % 'apidocs'}

Swagger(application)

# Create Blueprint Object
crypto_blueprint = Blueprint('crypto-v1', __name__)

api = Api(crypto_blueprint)
CORS(crypto_blueprint)

application.register_blueprint(crypto_blueprint, url_prefix='/crypto/v1')

api.add_resource(Recomendations, '/recommendations', strict_slashes=False)


if __name__ == '__main__':
    application.run(debug=True)