from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok", ceo="Emmy-Ai-", mode="ONLINE 24/7"), 200

@app.route("/")
def home():
    html = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>EMMY AI - CEO MODE ONLINE 24/7</title>
<style>
body{margin:0;background:#0a0614;color:white;font-family:system-ui;text-align:center}
.bg{position:fixed;top:0;left:0;width:100%;height:100%;background:radial-gradient(circle at 50% 0%, #3a1a6b 0%, #0a0614 70%);z-index:-1}
.crown{font-size:48px;margin-top:50px}
h1{font-size:32px;background:linear-gradient(90deg,#f5d78e,#d4af37);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900;margin:15px}
.sub{color:#c084fc;font-size:12px;margin-bottom:30px}
.card{margin:20px auto;max-width:380px;background:rgba(255,255,255,0.06);border:1px solid rgba(168,85,247,0.4);border-radius:24px;padding:20px;backdrop-filter:blur(20px)}
.bubble{background:rgba(255,255,255,0.1);border-radius:20px;padding:18px;text-align:left}
.btns{display:flex;gap:12px;margin-top:20px}
.btn{flex:1;padding:14px;border-radius:30px;border:none;font-weight:700}
.gold{background:linear-gradient(90deg,#d4af37,#f5d78e);color:#1a1033}
.purple{background:transparent;border:1px solid #c084fc;color:#c084fc}
.pulse{display:inline-block;width:8px;height:8px;background:#22c55e;border-radius:50%;margin-right:6px}
</style>
</head>
<body>
<div class="bg"></div>
<div class="crown">👑</div>
<h1>EMMY AI - CEO MODE<br>ONLINE 24/7</h1>
<div class="sub"><span class="pulse"></span>Laredo, Texas • 24/7 AI CEO • ONLINE</div>
<div class="card">
<div class="bubble">
<b>Hello Boss!</b><br>I'm Emmy AI 🚀<br><br>Your site is now ONLINE 24/7!<br>How can I help you today?
</div>
<div class="btns">
<button class="btn gold">✨ Launch Dashboard</button>
<button class="btn purple" onclick="location.href='/health'">View Analytics</button>
</div>
</div>
</body>
</html>"""
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
