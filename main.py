import os
import discord
from discord.ext import commands
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn
import threading

class AppInfo(BaseModel):
    name: str
    permissions: List[str]

class DeviceData(BaseModel):
    battery: int
    storage_free_percent: int
    apps: List[AppInfo] = []

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Emmy-Ai ONLINE as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! Emmy-Ai is back! {round(bot.latency*1000)}ms")

@bot.event
async def on_message(message):
    if message.author == bot.user: return
    if "hello" in message.content.lower():
        await message.channel.send(f"Hi {message.author.mention}! I'm back 🤖")
    await bot.process_commands(message)

def run_discord():
    token = os.getenv("DISCORD_TOKEN")
    if token: bot.run(token)

app = FastAPI()
@app.get("/")
def home():
    return {"status": "Emmy-Ai + EmmyGuard Online", "owner": "emmy97193-cyber"}

@app.post("/analyze")
def analyze(data: DeviceData):
    fitness = int(data.battery * 0.5 + data.storage_free_percent * 0.5)
    risky = []
    for a in data.apps:
        p = " ".join(a.permissions)
        score = 0
        reason = ""
        if "READ_SMS" in p and "SEND_SMS" in p:
            score = 95; reason = "SMS fraud risk"
        elif "ACCESS_FINE_LOCATION" in p and len(a.permissions)>10:
            score = 75; reason = f"Over-privileged {len(a.permissions)} perms"
        if score>0: risky.append({"app": a.name, "score": score, "reason": reason})
    return {"fitness": fitness, "risky_count": len(risky), "risky": risky[:10]}

if __name__ == "__main__":
    threading.Thread(target=run_discord, daemon=True).start()
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
