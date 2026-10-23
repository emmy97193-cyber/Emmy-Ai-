@app.route("/")
def home():
    return "👑 EMMY AI IS AWAKE - CEO MODE ACTIVE"

@app.route("/health")
def health():
    return {"status": "ok", "ceo": "Emmy-Ai-", "location": "Laredo, TX"}, 200
