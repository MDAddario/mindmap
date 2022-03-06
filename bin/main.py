from flask import Flask, request

import mindmap as mm


# Define app
app = Flask(__name__)

# SPEC 1: post a new ID
@app.route("/", methods=['POST'])
def post_id():
    
    identity = request.json['id']
    return mm.create_map(identity)


# SPEC 2: post a new leaf to ID
@app.route("/<identity>", methods=['POST'])
def post_leaf(identity):
    
    path = request.json['path']
    text = request.json['text']
    return mm.add_leaf(identity, path, text)


# SPEC 3: get a single leaf from ID
@app.route("/<identity>/<path:path>", methods=['GET'])
def get_leaf(identity, path):
    
    return mm.read_leaf(identity, path)


# SPEC 4: get the whole tree from ID
@app.route("/<identity>", methods=['GET'])
def get_tree(identity):
    
    return mm.read_tree(identity)


# NOT A SPEC: delete entire database (for unit testing)
@app.route("/", methods=['DELETE'])
def delete_all():
    
    return mm.reset_db()
