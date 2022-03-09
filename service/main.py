"""
Endpoints for mindmap web service
Defines all valid POST and GET requests
"""

from flask import Flask, request

from .mindmap import create_map, add_leaf, read_leaf, read_tree


# Define app
app = Flask(__name__)


@app.route("/", methods=["POST"])
def post_id():
    """
    Specification 1:

    Create a new mind map via an ID

    Request should provide a json object with an "id" field
    """

    identity = request.json["id"]
    return create_map(identity)


@app.route("/<identity>", methods=["POST"])
def post_leaf(identity):
    """
    Specification 2:

    Add a leaf to an existing mind map

    Request should provide a json object with "path" and "text" fields
    Request URI should specify the ID of the mind map
    """

    path = request.json["path"]
    text = request.json["text"]
    return add_leaf(identity, path, text)


@app.route("/<identity>/<path:path>", methods=["GET"])
def get_leaf(identity, path):
    """
    Specification 3:

    Read a leaf from an existing mind map

    Request URI should specify the ID of the mind map and the path to the leaf
    """

    return read_leaf(identity, path)


@app.route("/<identity>", methods=["GET"])
def get_tree(identity):
    """
    Specification 4:

    Read an entire existing mind map

    Request URI should specify the ID of the mind map
    """

    return read_tree(identity)
