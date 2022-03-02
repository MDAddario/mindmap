from flask import Flask, request


# Define app
app = Flask(__name__)

# SPEC 1: post a new ID
@app.route("/", methods=['POST'])
def post_id():
    
    identity = request.json['id']
    return f"Created {identity}"


# SPEC 2: post a new leaf to ID
@app.route("/<identity>", methods=['POST'])
def post_leaf(identity):
    
    path = request.json['path']
    text = request.json['text']
    return f"Added {path} with {text} for {identity}"


# SPEC 4: get the whole tree from ID
@app.route("/<identity>", methods=['GET'])
def get_tree(identity):
    
    return f"Requested {identity}"


# SPEC 3: get a single leaf from ID
@app.route("/<identity>/<path:path>", methods=['GET'])
def get_leaf(identity, path):
    
    return f"Requested {path} from {identity}"
