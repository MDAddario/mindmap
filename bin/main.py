from flask import Flask, request


app = Flask(__name__)

@app.route("/<iden>/<path:path>", methods=['POST'])
def home_page(iden, path):
    assert request.method == 'POST'
    return f"{iden} followed by {path} + {request.json['id']}"
