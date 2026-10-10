import os,discord
from discord.ext import commands
intents=discord.Intents.default()
intents.message_content=True
bot=commands.Bot(command_prefix="!",intents=intents)
@bot.event
async def on_ready():print(f"ONLINE {bot.user}")
@bot.command()
async def ping(ctx):await ctx.send(f"Pong! Emmy-Ai Online {round(bot.latency*1000)}ms!")
bot.run(os.getenv("DISCORD_TOKEN")
