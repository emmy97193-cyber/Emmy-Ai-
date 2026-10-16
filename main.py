from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lady T Hairs and Beauty Empire</title>
<style>
body{margin:0;background:#fff0f5;font-family:Arial;text-align:center}
.hero{width:100%;max-width:450px;margin:auto;background:white;border-radius:20px;overflow:hidden;box-shadow:0 10px 30px rgba(0,0,0,.2)}
img{width:100%} .text{padding:20px}
h1{color:#d63384;font-size:22px} ul{text-align:left;color:#444}
.btn{background:#d63384;color:white;padding:15px;display:block;border-radius:30px;text-decoration:none;font-weight:bold;margin-top:15px}
</style>
</head>
<body>
<div class="hero">
<img src="https://i.ibb.co/YOUR-LINK-HERE.jpg" alt="Lady T 26 inch blonde">
<div class="text">
<h1>LADY T HAIRS & BEAUTY EMPIRE</h1>
<p><b>26" SDD BLONDE STRAIGHT - AVAILABLE NOW!</b></p>
<p>We specialize on:</p>
<ul>
<li>Nails, Eyelash, Eyebrows, Lip gloss, Eye pencil, Lipsticks</li>
<li>Hair bonnet, Hair band (kids & adult), Beads, Wool (all colours)</li>
<li>Hair tie, Rubber thread, Bands, Hair net, Shower cap, Attachment</li>
<li>Wig caps, Dummy head, Bed head for styling</li>
<li>Perfumes, Face mask, Face cream, Body cream, Hair cream</li>
<li>Living Mega Growth (sachet & cup), Elan shampoo, Edge control, Relaxer, Oil for bone straight, Discover, Cutter</li>
</ul>
<p><b>Sapele, Delta | Nationwide Delivery</b></p>
<a class="btn" href="https://wa.me/2348120287198">Order on WhatsApp: 08120287198</a>
</div>
</div>
</body>
</html>
    """

if __name__ == "__main__":
    app.run()
