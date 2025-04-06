@app.route("/", methods=["GET", "POST"])
def recevoir():
    if request.method == "POST":
        contenu = request.get_json()
        with open("dernier_message.json", "w") as f:
            json.dump(contenu, f)
        return {"status": "ok"}, 200
    return "⚠️ Tu dois utiliser POST avec un JSON", 200
