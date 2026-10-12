from flask import Flask
import threading
import os
import discord
from discord.ext import commands

# --- WEB SERVER FOR RAILWAY + YOUR APP ---
web = Flask(__name__)

@web.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html><head><meta name='viewport' content='width=device-width,initial-scale=1'>
    <style>body{margin:0;font-family:sans-serif;background:#0f0f0f;color:#fff}
    header{background:#4CAF50;padding:14px;display:flex;align-items:center;gap:10px}
    .card{background:#1a1a1a;margin:12px;border-radius:16px;overflow:hidden}
    .card img{width:100%;height:200px;object-fit:cover}
    .btn{background:#4CAF50;color:white;border:none;padding:10px;width:100%;font-weight:bold}
    </style></head><body>
    <header><h1>EMMY AI 🐸 $WALLPAPER</h1></header>
    <div style='padding:16px'><h2>Bot Online ✅</h2><p>Wallpaper Gallery</p></div>
    <div class='card'><img src='https://images.unsplash.com/photo-1534972195531-b367aadb2cc8?w=720'>
    <button class='btn' onclick="window.open(this.previousElementSibling.src)">Download</button></div>
    <div class='card'><img src='https://images.unsplash.com/photo-1519125323398-675f0ddb6308?w=720'>
    <button class='btn' onclick="window.open(this.previousElementSibling.src)">Download</button></div>
    </body></html>
    """

def run_web():
    web.run(host='0.0.0.0', port=8080)

threading.Thread(target=run_web, daemon=True).start()

# --- YOUR DISCORD BOT (keep your token in Railway Variables) ---
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is online')

# Add your bot commands here...

bot.run(os.getenv('DISCORD_TOKEN'))
