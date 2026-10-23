from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

@app.route("/")
def home():
    return (
    "<html><head>"
    '<meta name="viewport" content="width=device-width,initial-scale=1">'
    "<style>"
    "body{margin:0;padding:24px;background:#0a0614;color:#fff;"
    "font-family:sans-serif;text-align:center;min-height:100vh}"
    "h1{background:linear-gradient(90deg,#f5d78e,#d4af37);"
    "-webkit-background-clip:text;-webkit-text-fill-color:transparent;"
    "font-size:28px;font-weight:900}"
    ".card{margin:20px auto;max-width:360px;background:rgba(255,255,255,0.08);"
    "border:1px solid #a855f7;border-radius:20px;padding:20px;"
    "box-shadow:0 0 30px rgba(168,85,247,0.3)}"
    ".bubble{background:rgba(255,255,255,0.12);border-radius:16px;padding:16px;text-align:left}"
    ".gold{width:100%;padding:12px;border-radius:25px;border:0;"
    "background:linear-gradient(90deg,#d4af37,#f5d78e);font-weight:700;margin-top:12px}"
    ".dot{display:inline-block;width:8px;height:8px;background:#22c55e;border-radius:50%}"
    "</style></head><body>"
    '<div style="font-size:40px">👑</div>'
    "<h1>EMMY AI - CEO MODE<br>ONLINE 24/7</h1>"
    '<div style="color:#c084fc;font-size:12px"><span class="dot"></span> Laredo, TX • ONLINE</div>'
    '<div class="card"><div class="bubble">'
    "<b>Hello Boss!</b><br>I'm Emmy AI 🚀<br><br>"
    "Your site is now ONLINE 24/7!<br>How can I help?"
    "</div><button class='gold'>✨ Launch Dashboard</button></div>"
    '<p style="color:#9ca3af;font-size:11px;margin-top:30px">Built on phone • CEO MODE ACTIVE</p>'
    "</body></html>"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
