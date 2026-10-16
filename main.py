from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>EMMY AI technology ⭐</title>
</head>
<body style="margin:0; background:#0a0a12; color:#fff; font-family: sans-serif; text-align:center;">

<div style="width:100%; max-width:480px; margin:0 auto; padding:12px;">
  <video autoplay loop muted playsinline 
    style="width:100%; border-radius:24px; border:2px solid #00e5ff; box-shadow:0 0 25px rgba(0,229,255,0.3);">
    <source src="https://files.catbox.moe/co0epb.mp4" type="video/mp4">
  </video>

  <h2 style="color:#00e5ff; text-shadow:0 0 10px #00e5ff;">EMMY AI technology ⭐</h2>
  <p style="color:#ff6bff;">I am the creator</p>

  <a href="https://wa.me/2349115131319?text=Hi%20Emmy%20AI%20⭐%20I%20saw%20your%20cyborg%20video" target="_blank"
     style="display:block; background:#25D366; color:#fff; padding:14px; border-radius:999px; text-decoration:none; font-weight:800; margin:12px 0;">
     💬 Chat Emmy on WhatsApp
  </a>

  <a href="https://wa.me/2349115131319?text=Hello%20Lady%20T%20I%20want%20to%20buy%20hair" target="_blank"
     style="display:block; background:#ff2d95; color:#fff; padding:14px; border-radius:999px; text-decoration:none; font-weight:700;">
     🛍️ Shop Lady T Hairs
  </a>

  <div style="background:#fff; color:#000; border-radius:16px; padding:12px; margin-top:16px; text-align:left; font-size:13px;">
    <span style="background:#ff2d95; color:#fff; padding:4px 10px; border-radius:999px; font-size:11px;">ACTIVE PROJECT</span>
    <p style="color:#ff2d95; font-weight:800; margin:8px 0 4px;">Emmy-Ai- - Online</p>
    <p>✔️ Production: emmy-ai-production-bc46.up.railway.app</p>
    <p>✔️ Video: co0epb.mp4 Cyborg 98.7% Sync - Catbox</p>
    <p>✔️ Gunicorn 26.2.0 - 0.0.0.0:8080</p>
    <p>✔️ Concept: I-Ai = We Are The Creator</p>
  </div>

  <p style="color:#666; font-size:11px; margin-top:16px;">Built with Meta AI • Powered by EMMY AI technology ⭐ • Abuja, NG</p>
</div>

</body>
</html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
