"""A decorator to validate the arguments passed"""
from Random_Album_API.shared_resources.exceptions import APIException

def validate_arguments(func):
    """"""
    def argument_validator(api_key, context):
        """"""
        try :
            assert api_key == 'jUstA!<eY1'
        except AssertionError:
            raise APIException(
                message="Invalid API Key",
                status_code=401
            )
        try :
            assert context in ("random", "all")
        except AssertionError:
            raise APIException(
                message="Invalid Context",
                status_code=406                                   
            )
        return func(api_key, context)
    return argument_validator