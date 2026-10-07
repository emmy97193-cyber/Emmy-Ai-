import discord
import os
from flask import Flask
import threading

app = Flask(__name__)
@app.route('/')
def home(): return "Emmy Ai is Online!"

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is Online!')

@bot.event
async def on_message(message):
    if message.author == bot.user: return
    if bot.user.mentioned_in(message):
        await message.channel.send(f"Hi {message.author.mention}! I'm Emmy Ai 😊 How can I help you?")
    if "hello" in message.content.lower():
        await message.channel.send(f"Hello {message.author.mention}!")

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

threading.Thread(target=run_flask).start()

TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
