from flask import Blueprint, current_app, jsonify, request, abort
from flask.views import MethodView

from Random_Album_API.shared_resources.argument_check import validate_arguments
from Random_Album_API.logics.app_logic import GetRandomAlbum

random_album = Blueprint('random_album', __name__)

@validate_arguments
def logic_caller(api_key, context):
    """"""
    obj = GetRandomAlbum(context=context)
    return obj.driver_method()

class RandomAlbumAPI(MethodView):
    """
    """
    def get(self):
        api_key = request.args.get('api_key',None)
        context = request.args.get('context',None)
        return jsonify(logic_caller(api_key, context))
