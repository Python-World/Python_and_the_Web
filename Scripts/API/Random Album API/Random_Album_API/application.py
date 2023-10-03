from flask import Flask, jsonify
from Random_Album_API.shared_resources.exceptions import APIException
from Random_Album_API.views.api_view import RandomAlbumAPI, random_album

app = Flask(__name__)
# Register the blueprint
app.register_blueprint(random_album)
# Add the route to the view class
app.add_url_rule(
    "/v1/random-album/", view_func=RandomAlbumAPI.as_view("random-album")
)


# Exception Handler
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
