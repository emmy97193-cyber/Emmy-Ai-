import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Emmy AI is Online 24/7! 🚀"

@app.route("/health")
def health():
    return {"status": "ok", "message": "Emmy AI Running"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
