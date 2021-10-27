from builtins import super
from flask.wrappers import Response
import json


def sell(exc1, exc1_name, exc2, exc2_name):
    exc1 = float(exc1)
    if exc1 < exc2:
        return {
            'exchange_name': exc2_name,
            'price': exc2
        }
    else:
        return {
            'exchange_name': exc1_name,
            'price': exc1
        }


def buy(exc1, exc1_name, exc2, exc2_name):
    exc1 = float(exc1)
    if exc1 < exc2:
        return {
            'exchange_name': exc1_name,
            'price': exc1
        }
    else:
        return {
            'exchange_name': exc2_name,
            'price': exc2
        }


class BaseResponse(Response):
    """
    Base class to format Api response
    """

    def __init__(self, body=None, http_status=None, mime_type='application/json'):
        if body is not None:
            body = json.dumps(body)
        super().__init__(response=body, status=http_status, mimetype=mime_type)


class ErrorResponse(BaseResponse):
    """
        Format error response of API
    """

    def __init__(self, exception, status):

        if isinstance(exception, Exception) and status == 500:
            resp = {"message": "Internal Server Error"}
        elif isinstance(exception, dict):
            resp = exception
        else:
            resp = {"message": str(exception)}

        body = {'data': resp, 'type': 'invalid_request_error', 'code': status}
        code = status
        super().__init__(body=body, http_status=code)
