# Importing some useful libraries
from textblob import TextBlob
from flask import Flask, request, jsonify

# App name
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

# Run as a local host at 5000 port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)