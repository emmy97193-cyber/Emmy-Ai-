from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lady T Hairs & Beauty Empire</title>
<style>
body{margin:0;background:#fff0f5;font-family:Arial}
.card{max-width:420px;margin:20px auto;background:white;border-radius:20px;overflow:hidden;box-shadow:0 15px 40px rgba(0,0,0,.25)}
img{width:100%} .text{padding:20px}
h1{color:#d63384;font-size:20px;margin:0 0 10px}
h2{color:#333;font-size:16px;margin:15px 0 5px}
ul{text-align:left;color:#444;font-size:14px;line-height:1.6}
.btn{display:block;padding:16px;border-radius:35px;text-decoration:none;font-weight:bold;margin:12px 0;text-align:center}
.btn-wa{background:#25D366;color:white}
.btn-call{background:#d63384;color:white}
.badge{background:#d63384;color:white;padding:6px 12px;border-radius:20px;font-size:12px;display:inline-block;margin-bottom:10px}
</style>
</head>
<body>
<div class="card">
<img src="https://i.imgur.com/8Km9tLL.jpg" alt="Lady T Blonde">
<div class="text">
<span class="badge">NEW ARRIVAL - 26" SDD BLONDE STRAIGHT</span>
<h1>LADY T HAIRS & BEAUTY EMPIRE</h1>
<p>Your one-stop shop for luxury hair & cosmetics in Sapele!</p>

<h2>🔥 Hot Product: 26" SDD Blonde Straight</h2>
<p>Luxury bone straight, silky, full length - CEO look!</p>

<h2>We Sell:</h2>
<ul>
<li>Hair: Attachment, Wool (all colours), Wig caps, Bone straight oil, Elan shampoo/conditioner</li>
<li>Beauty: Nails, Eyelash, Eyebrows, Lip gloss, Lipsticks, Eye pencil</li>
<li>Accessories: Hair bonnet, Hair band (kids & adult), Beads, Hair tie, Rubber thread, Bands, Hair net, Shower cap, Edge control, Dummy head, Wig caps, Relaxer, Bed head</li>
<li>Cosmetics: Perfumes, Face mask, Face cream, Body cream, Hair cream, Living Mega Growth, Discover, Cutter</li>
</ul>

<a class="btn btn-wa" href="https://wa.me/2348120287198?text=Hello%20Lady%20T%2C%20I%20want%20to%20order%20your%2026%20inch%20SDD%20Blonde%20Straight%20and%20other%20products">💬 Order on WhatsApp</a>
<a class="btn btn-call" href="tel:+2348120287198">📞 Call: 08120287198</a>

<p style="font-size:12px;color:#888;margin-top:15px">📍 Sapele, Delta State | 🚚 Nationwide Delivery | Active since 2026-10-16</p>
</div>
</div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run()
