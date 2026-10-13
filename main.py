from flask import Flask
import threading, os
import discord
from discord.ext import commands

web = Flask(__name__)

@web.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta name='viewport' content='width=device-width,initial-scale=1'>
<title>EMMY AI $WALLPAPER</title>
<style>
body{margin:0;font-family:Arial,sans-serif;background:#0a0a0a;color:#fff}
header{background:#2ECC71;padding:20px;text-align:center}
header h1{margin:0;font-size:28px}
header p{margin:5px 0 0 0;opacity:0.9}
.gallery{padding:12px;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.card{background:#1c1c1c;border-radius:18px;overflow:hidden;border:1px solid #2a2a2a}
.card img{width:100%;height:220px;object-fit:cover;display:block}
.card .info{padding:10px}
.btn{background:#2ECC71;color:#000;border:none;padding:12px;width:100%;font-weight:900;border-radius:10px;margin-top:8px}
.badge{background:#111;padding:6px 10px;border-radius:20px;font-size:12px;display:inline-block;margin-top:6px;border:1px solid #2ECC71;color:#2ECC71}
</style>
</head>
<body>
<header>
<h1>EMMY AI 🐸 $WALLPAPER</h1>
<p>Meme Coin Community • AI Wallpaper Bot</p>
<div class='badge'>BOT ONLINE ✅ emmyai0616#1150</div>
</header>

<div style='padding:16px;text-align:center'>
<h2 style='margin:0'>🔥 Trending Wallpapers</h2>
<p style='opacity:0.7'>Download • Set • Share</p>
</div>

<div class='gallery'>
<div class='card'>
<img src='https://images.unsplash.com/photo-1519125323398-675f0ddb6308?w=600'>
<div class='info'>
<button class='btn' onclick="window.open(this.parentElement.previousElementSibling.src)">⬇ Download</button>
</div></div>

<div class='card'>
<img src='https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=600'>
<div class='info'>
<button class='btn' onclick="window.open(this.parentElement.previousElementSibling.src)">⬇ Download</button>
</div></div>

<div class='card'>
<img src='https://images.unsplash.com/photo-1534972195531-b367aadb2cc8?w=600'>
<div class='info'>
<button class='btn' onclick="window.open(this.parentElement.previousElementSibling.src)">⬇ Download</button>
</div></div>

<div class='card'>
<img src='https://images.unsplash.com/photo-1519681393784-d120267933ba?w=600'>
<div class='info'>
<button class='btn' onclick="window.open(this.parentElement.previousElementSibling.src)">⬇ Download</button>
</div></div>

</div>

<div style='text-align:center;padding:30px;opacity:0.5'>
<p>Powered by EMMY AI • $WALLPAPER on Base</p>
<p>Discord: emmyai0616#1150</p>
</div>

</body>
</html>
    """

def run_web():
    web.run(host='0.0.0.0', port=8080)

threading.Thread(target=run_web, daemon=True).start()

# Discord Bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is online - Gallery LIVE')

bot.run(os.getenv('DISCORD_TOKEN'))
