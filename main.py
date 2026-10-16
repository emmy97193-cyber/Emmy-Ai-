from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    VIDEO_URL = "https://files.catbox.moe/8v55as.mp4"
    return f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>EMMY AI technology - I am the creator</title>
<style>
body{{margin:0;background:#060618;font-family:Arial;color:white;text-align:center}}
.hero{{position:relative;max-width:480px;margin:0 auto;background:black}}
.hero video{{width:100%;max-height:85vh;border-radius:0 0 20px 20px}}
.neon{{color:#00f2ff;text-shadow:0 0 10px #00f2ff;font-size:22px;margin:15px 0 5px}}
.btn{{display:inline-block;padding:14px 26px;border-radius:30px;text-decoration:none;font-weight:bold;margin:8px}}
.btn-wa{{background:#25D366;color:white}} .btn-shop{{background:#ff2e93;color:white}}
.info{{max-width:420px;margin:15px auto;background:white;color:#222;border-radius:18px;padding:16px;text-align:left;font-size:14px}}
.badge{{background:#d63384;color:white;padding:5px 10px;border-radius:12px;font-size:11px}}
</style>
</head>
<body>

<div class="hero">
<video autoplay muted loop playsinline controls>
<source src="{VIDEO_URL}" type="video/mp4">
</video>
</div>

<h2 class="neon">EMMY AI technology ⭐</h2>
<p style="color:#ff6bde;font-size:18px;margin:0 0 15px">I am the creator</p>

<a class="btn btn-wa" href="https://wa.me/2348120287198?text=Hello%20Emmy%20I%20saw%20your%20video%20homepage">💬 Chat Emmy on WhatsApp</a>
<a class="btn btn-shop" href="https://wa.me/2348120287198?text=Shop%20Lady%20T%20Hairs">🛍️ Shop Lady T Hairs</a>

<div class="info">
<span class="badge">ACTIVE PROJECT</span>
<h3 style="margin:8px 0;color:#d63384">Emmy-Ai- - Online</h3>
✔️ Production: emmy-ai-production-bc46.up.railway.app<br>
✔️ Video: EMMY_AI_Creator_Intro.mp4 (5.6MB) hosted on Catbox<br>
✔️ Gunicorn 26.2.0 - Listening 0.0.0.0:8080<br>
✔️ Concept: I-Ai = We Are The Creator
</div>

<p style="color:#666;font-size:11px;margin:20px">Built with Meta AI • Powered by EMMY AI technology ⭐ • Abuja, NG</p>

</body>
</html>
"""

if __name__ == "__main__":
    app.run()
