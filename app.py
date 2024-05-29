from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World This is my first website and I am very happy for it!"
