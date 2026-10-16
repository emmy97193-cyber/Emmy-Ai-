from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    # REPLACE THIS WITH YOUR IMGUR LINK AFTER UPLOAD
    HERO_IMAGE = "https://i.imgur.com/YOUR_NEW_IMAGE_LINK.jpg"
    
    return f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>EMMY AI Technology - I am the creator</title>
<style>
body{{margin:0;background:#060616;font-family:Arial;color:white;text-align:center}}
.hero{{position:relative;width:100%;max-width:480px;margin:0 auto}}
.hero img{{width:100%;border-radius:0 0 25px 25px;box-shadow:0 10px 40px #00f2ff66}}
.overlay{{position:absolute;bottom:20px;left:0;right:0}}
.btn{{display:inline-block;padding:14px 28px;border-radius:30px;text-decoration:none;font-weight:bold;margin:8px}}
.btn-wa{{background:#25D366;color:white}} .btn-shop{{background:#ff2e93;color:white}}
.info{{max-width:420px;margin:20px auto;background:white;color:#222;border-radius:20px;padding:18px;text-align:left}}
.badge{{background:#d63384;color:white;padding:5px 10px;border-radius:15px;font-size:12px}}
</style>
</head>
<body>
<div class="hero">
<img src="{HERO_IMAGE}" alt="EMMY AI Technology I am the creator">
</div>

<div style="padding:15px">
<h2 style="color:#00f2ff">Welcome to Emmy-Ai- Empire</h2>
<p>Your AI-powered tech & beauty platform</p>
<a class="btn btn-wa" href="https://wa.me/2348120287198?text=Hello%20Emmy%20I%20saw%20your%20new%20homepage">💬 Chat Emmy on WhatsApp</a>
<a class="btn btn-shop" href="https://wa.me/2348120287198?text=I%20want%20to%20shop%20Lady%20T%20products">🛍️ Shop Lady T Hairs</a>

<div class="info">
<span class="badge">ACTIVE PROJECT</span>
<h3 style="margin:10px 0 5px;color:#d63384">Emmy-Ai- - Online</h3>
<p style="font-size:14px;line-height:1.5">
✔️ Production: emmy-ai-production-bc46.up.railway.app<br>
✔️ Gunicorn 26.2.0 - Listening 0.0.0.0:8080<br>
✔️ Deployment successful - 2026-10-16 18:09<br>
✔️ Concept: I-Ai = We Are The Creator
</p>
</div>

<p style="color:#888;font-size:11px;margin-top:20px">Built with Meta AI • Powered by EMMY AI technology ⭐ • Abuja, NG</p>
</div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run()
