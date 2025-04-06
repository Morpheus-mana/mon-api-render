from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def recevoir():
    print(request.json)
    return {"status": "ok"}, 200
