from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok", ceo="Emmy-Ai-", mode="24/7 ONLINE"), 200

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>EMMY AI - CEO MODE ONLINE 24/7</title>
<style>
  body{margin:0;background:#0a0614;color:white;font-family:system-ui;text-align:center;overflow-x:hidden}
  .bg{position:fixed;top:0;left:0;width:100%;height:100%;background: radial-gradient(circle at 50% 0%, #3a1a6b 0%, #0a0614 70%);z-index:-1}
  .smoke{position:fixed;top:0;right:0;width:60%;height:100%;background:linear-gradient(90deg, transparent, rgba(168,85,247,0.15));filter:blur(20px);z-index:-1}
  .crown{font-size:48px;margin-top:50px;animation:float 3s infinite}
  @keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
  h1{font-size:42px;background:linear-gradient(90deg,#f5d78e,#d4af37);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900;line-height:1.1;margin:15px}
  .sub{color:#c084fc;letter-spacing:2px;font-size:12px;margin-bottom:30px}
  .card{margin:20px auto;max-width:380px;background:rgba(255,255,255,0.06);border:1px solid rgba(168,85,247,0.4);border-radius:24px;padding:20px;backdrop-filter:blur(20px);box-shadow:0 0 40px rgba(168,85,247,0.3)}
  .bubble{background:rgba(255,255,255,0.1);border-radius:20px;padding:18px;text-align:left;border:1px solid rgba(255,255,255,0.1)}
  .btns{display:flex;gap:12px;margin-top:20px}
  .btn{flex:1;padding:14px;border-radius:30px;border:none;font-weight:700;cursor:pointer}
  .gold{background:linear-gradient(90deg,#d4af37,#f5d78e);color:#1a1033}
  .purple{background:transparent;border:1px solid #c084fc;color:#c084fc}
  .nav{display:flex;justify-content:space-around;margin:30px auto;max-width:380px;background:rgba(0,0,0,0.4);border-radius:20px;padding:12px;border:1px solid rgba(168,85,247,0.3)}
  .nav div{font-size:12px;color:#9ca3af}.nav div.active{color:#c084fc}
  .pulse{display:inline-block;width:8px;height:8px;background:#22c55e;border-radius:50%;box-shadow:0 0 10px #22c55e;animation:pulse 1.5s infinite;margin-right:6px}
  @keyframes pulse{0%{opacity:1}50%{opacity:0.3}100%{opacity:1}}
  .roses{position:fixed;bottom:-20px;left:0;right:0;height:120px;background:radial-gradient(ellipse at bottom, rgba(88,28,135,0.5), transparent);pointer-events:none}
</style>
</head>
<body>
<div class="bg"></div><div class="smoke"></div>
<div class="crown">👑</div>
<h1>EMMY AI - CEO MODE<br>ONLINE 24/7</h1>
<div class="sub"><span class="pulse"></span>Laredo, Texas • 24/7 AI CEO • <span style="color:#22c55e">ONLINE</span></div>

<div class="card">
  <div class="bubble">
    <b>Hello Boss!</b><br>
    I'm Emmy AI 🚀<br><br>
    Your site is now ONLINE 24/7!<br>
    How can I help you today?
  </div>
  <div class="btns">
    <button class="btn gold" onclick="alert('Dashboard coming soon Boss 👑')">✨ Launch Dashboard</button>
    <button class="btn purple" onclick="location.href='/health'">View Analytics</button>
  </div>
</div>

<div class="nav">
  <div class="active">🏠<br>Home</div>
  <div>💬<br>Chat</div>
  <div>📊<br>Insights</div>
  <div>⚙️<br>Settings</div>
</div>

<div class="roses"></div>
</body>
</html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
