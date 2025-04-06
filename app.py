from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def recevoir():
    if request.method == "POST":
        contenu = request.get_json()
        with open("dernier_message.json", "w") as f:
            json.dump(contenu, f)
        return {"status": "ok"}, 200
    else:
        return "<h1>✅ API en ligne</h1><p>Utilise POST avec du JSON pour envoyer des données.</p>", 200
