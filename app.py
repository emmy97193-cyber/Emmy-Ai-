from flask import Flask
import os

app = Flask(__name__)

CEO_IMAGE_URL = "https://i.imgur.com/8Km9tLL.png"  # Replace with your Imgur link after you upload

@app.route('/')
def home():
    return f"""
    <html>
    <head><meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>EMMY AI ⭐</title>
    <style>
      body{{margin:0;background:radial-gradient(circle at top,#7c3aed,#050612);color:white;text-align:center;font-family:Arial;padding:20px}}
      .logo{{font-size:3rem;font-weight:900;background:linear-gradient(90deg,#f9d76e,#a855f7);-webkit-background-clip:text;-webkit-text-fill-color:transparent}}
      img{{width:90%;max-width:400px;border-radius:24px;border:3px solid #a855f7;box-shadow:0 0 40px #a855f7;margin:20px 0}}
      .btn{{display:block;margin:15px auto;padding:14px 28px;border-radius:50px;text-decoration:none;font-weight:800;width:90%;max-width:320px}}
      .gold{{background:linear-gradient(90deg,#ffcc33,#ffef9a);color:#140b2a}}
      .purple{{background:linear-gradient(90deg,#7c3aed,#a855f7);color:white;border:2px solid #a855f7}}
    </style></head>
    <body>
      <div class="logo">EMMY AI ⭐</div>
      <div style="font-size:4rem">⭐</div>
      <img src="{CEO_IMAGE_URL}" alt="EMMY AI CEO" onerror="this.src='https://via.placeholder.com/400x600/140b2a/f9d76e?text=EMMY+AI+CEO+STAR'" />
      <div style="letter-spacing:3px;color:#f9d76e;font-weight:bold;margin:20px 0;">INTELLIGENCE • INNOVATION • IMPACT</div>
      <a href="{CEO_IMAGE_URL}" download class="btn gold">📥 Download Home Wallpaper</a>
      <a href="{CEO_IMAGE_URL}" download class="btn purple">📱 Download Lock Screen</a>
      <p style="opacity:0.6;margin-top:30px;">CEO MODE: ACTIVE | GLASSES: FUTURE VISION | STAR: ⭐ ACTIVATED</p>
      <p style="opacity:0.4;">emmy-ai-production-bc46.up.railway.app</p>
    </body></html>
    """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT",8080)))
