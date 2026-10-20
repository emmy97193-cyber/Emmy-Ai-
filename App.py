from flask import Flask
import os

app = Flask(__name__)

# This uses your own GitHub image - will never crash
IMG = "https://raw.githubusercontent.com/emmy9719/Emmy-Ai-/main/IMG-20261020-WA9640.jpg"

@app.route('/')
def home():
    return f"""
<!DOCTYPE html>
<html><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>EMMY AI ⭐</title>
<style>
 body{{margin:0;background:radial-gradient(circle at top,#7c3aed,#050612);color:#fff;font-family:Arial;text-align:center;padding:20px}}
 .logo{{font-size:3rem;font-weight:900;background:linear-gradient(90deg,#f9d76e,#a855f7);-webkit-background-clip:text;-webkit-text-fill-color:transparent}}
 img{{width:92%;max-width:400px;border-radius:24px;border:3px solid #a855f7;box-shadow:0 0 40px #a855f7;margin:20px auto;display:block}}
 .btn{{display:block;margin:12px auto;padding:14px 28px;border-radius:50px;text-decoration:none;font-weight:800;width:90%;max-width:320px}}
 .gold{{background:linear-gradient(90deg,#ffcc33,#ffef9a);color:#140b2a}}
 .purple{{background:linear-gradient(90deg,#7c3aed,#a855f7);color:#fff;border:2px solid #a855f7}}
</style>
</head><body>
<div class="logo">EMMY AI ⭐</div>
<div style="font-size:3.5rem">⭐</div>
<img src="{IMG}" alt="EMMY AI">
<div style="color:#f9d76e;letter-spacing:3px;font-weight:bold">INTELLIGENCE • INNOVATION • IMPACT</div>
<a class="btn gold" href="{IMG}" target="_blank">📥 Download Wallpaper</a>
<a class="btn purple" href="{IMG}" target="_blank">📱 Lock Screen</a>
<p style="opacity:.6;margin-top:20px">CEO MODE: ACTIVE | STAR: ACTIVATED</p>
</body></html>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
