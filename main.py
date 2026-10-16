from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Emmy-Ai- | Lady T Beauty Empire</title>
<style>
body{margin:0;background:#0a0a1a;font-family:Arial;color:white;overflow-x:hidden}
#splash{position:fixed;top:0;left:0;width:100%;height:100%;background:#0a0a1a;display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:9999;transition:0.8s}
#splash video{width:280px;border-radius:20px}
#splash h2{color:#ff6bce;margin-top:15px;letter-spacing:2px;text-shadow:0 0 10px #ff6bce}
.card{max-width:420px;margin:20px auto;background:white;color:#333;border-radius:20px;overflow:hidden;box-shadow:0 15px 40px rgba(0,0,0,.5)}
.card img{width:100%} .text{padding:20px}
.btn{display:block;padding:16px;border-radius:35px;text-decoration:none;font-weight:bold;margin:12px 0;text-align:center}
.btn-wa{background:#25D366;color:white}
.btn-call{background:#d63384;color:white}
.badge{background:#d63384;color:white;padding:6px 12px;border-radius:20px;font-size:12px;display:inline-block}
</style>
</head>
<body>

<div id="splash">
  <img src="https://i.imgur.com/Q2a4LwZ.gif" alt="Emmy Ai Avatar" style="width:250px">
  <h2>EMMY AI technology ⭐</h2>
  <p id="creator-text" style="font-size:18px;margin-top:5px;opacity:0;transition:1s">I am the creator</p>
</div>

<div class="card">
<img src="https://i.imgur.com/8Km9tLL.jpg" alt="Lady T">
<div class="text">
<span class="badge">26" SDD BLONDE - AVAILABLE</span>
<h1 style="color:#d63384;font-size:20px">LADY T HAIRS & BEAUTY EMPIRE</h1>
<p>Welcome to Emmy-Ai- project - Luxury hairs & beauty in Sapele!</p>
<a class="btn btn-wa" href="https://wa.me/2348120287198?text=Hello%20Lady%20T%2C%20I%20saw%20your%20Emmy-Ai%20site%20and%20want%20to%20order">💬 Order on WhatsApp</a>
<a class="btn btn-call" href="tel:+2348120287198">📞 08120287198</a>
<p style="font-size:11px;color:#888">emmy-ai-production-bc46.up.railway.app | Built with Emmy-Ai- concept</p>
</div>
</div>

<script>
// Splash logic - shows your avatar intro
setTimeout(()=>{document.getElementById('creator-text').style.opacity='1'},800);
setTimeout(()=>{document.getElementById('splash').style.transform='translateY(-100%)'},3000);
</script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run()
