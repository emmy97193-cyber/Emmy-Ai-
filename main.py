from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width">
<title>Lady T Hairs and Beauty Empire</title>
<style>
body{margin:0;background:#fff0f5;font-family:Arial;padding:20px}
.card{max-width:420px;margin:auto;background:white;border-radius:20px;overflow:hidden;box-shadow:0 10px 30px rgba(0,0,0,.2)}
img{width:100%} .text{padding:20px} h1{color:#d63384;font-size:22px}
ul{color:#444;text-align:left} .btn{background:#d63384;color:white;padding:14px 20px;border-radius:30px;display:block;text-align:center;text-decoration:none;font-weight:bold;margin-top:15px}
</style>
</head>
<body>
<div class="card">
<img src="https://i.ibb.co/placeholder-your-image.jpg" alt="Lady T">
<div class="text">
<h1>LADY T HAIRS AND BEAUTY EMPIRE</h1>
<p>We specialize on all types of hair accessories & cosmetics:</p>
<ul>
<li>Nails, Eyelash, Eyebrows, Lip gloss, Eye pencil, Lipsticks</li>
<li>Hair bonnet, Hair band (kids & adult), Beads, Wool (all colours)</li>
<li>Hair tie, Rubber thread, Bands, Hair net, Shower cap, Attachment</li>
<li>Wig caps, Dummy head, Bed head for styling, Wig stand</li>
<li>Perfumes, Face mask, Face cream, Body cream, Hair cream</li>
<li>Living Mega Growth (sachet & cup), Elan shampoo & conditioner, Edge control, Relaxer, Oil for bone straight</li>
<li>Discover, Cutter and more!</li>
</ul>
<p><b>📍 Sapele, Delta State | 🚚 Nationwide Delivery</b></p>
<a class="btn" href="https://wa.me/2348120287198">Chat on WhatsApp: 08120287198</a>
</div>
</div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
