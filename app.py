from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=["POST"])
def recevoir():
    contenu = request.get_json()
    with open("dernier_message.json", "w") as f:
        json.dump(contenu, f)
    return {"status": "ok"}, 200
