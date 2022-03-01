from flask import Flask


app = Flask(__name__)

@app.route("/")
def home_page():
    return "<p>Welcome to the home page</p>"
