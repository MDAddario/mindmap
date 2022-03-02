from flask import Flask, request

# Define app
app = Flask(__name__)

# SPEC 1: post a new ID
@app.route("/", methods=['POST'])
def post_id():
    
    identity = request.json['id']
    return f"Created {identity}"

# SPEC 2: post a new leaf to ID

# SPEC 4: get the whole tree from ID

# SPEC 3: get a single leaf from ID

@app.route("/<iden>/<path:path>", methods=['POST'])
def home_page(iden, path):
    assert request.method == 'POST'
    return f"{iden} followed by {path} + {request.json['id']}"
