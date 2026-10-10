import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} - Emmy-Ai Online!")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms - Emmy-Ai Online!")

# For EmmyGuard API (your Android app)
from flask import Flask, request, jsonify
from threading import Thread

app = Flask(__name__)

@app.route("/")
def home():
    return "Emmy-Ai is Running!"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text", "")
    # Simple demo - you will add AI later
    return jsonify({"result": "safe", "text": text})

def run_flask():
    app.run(host="0.0.0.0", port=8080)

Thread(target=run_flask, daemon=True).start()

token = os.getenv("DISCORD_TOKEN")
if token:
    token = token.strip().replace("\n", "").replace(" ", "")
    bot.run(token)
