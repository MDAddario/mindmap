from flask import Flask, request

from .mindmap import create_map, add_leaf, read_leaf, read_tree


# Define app
app = Flask(__name__)

# SPEC 1: post a new ID
@app.route("/", methods=['POST'])
def post_id():
    
    identity = request.json['id']
    return create_map(identity)


# SPEC 2: post a new leaf to ID
@app.route("/<identity>", methods=['POST'])
def post_leaf(identity):
    
    path = request.json['path']
    text = request.json['text']
    return add_leaf(identity, path, text)


# SPEC 3: get a single leaf from ID
@app.route("/<identity>/<path:path>", methods=['GET'])
def get_leaf(identity, path):
    
    return read_leaf(identity, path)


# SPEC 4: get the whole tree from ID
@app.route("/<identity>", methods=['GET'])
def get_tree(identity):
    
    return read_tree(identity)
