import discord, os
from flask import Flask
import threading
from discord.ext import commands

app = Flask(__name__)
@app.route('/')
def home(): return "Emmy Ai is Online!"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is Online!")

@bot.event
async def on_message(message):
    if message.author == bot.user: return
    if bot.user.mentioned_in(message):
        await message.channel.send(f"Hi {message.author.mention}! I'm Emmy Ai ✨ How can I help?")
    await bot.process_commands(message)

def run_flask():
    app.run(host="0.0.0.0", port=10000)

threading.Thread(target=run_flask).start()
bot.run(os.getenv("BOT_TOKEN"))
