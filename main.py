import os, discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
  command_prefix="!",
  intents=intents
)

@bot.event
async def on_ready():
  print("Emmy-Ai Online")

@bot.command()
async def ping(ctx):
  await ctx.send("Pong! Emmy-Ai Online!")

token = os.getenv("DISCORD_TOKEN")
if token:
  bot.run(token.strip())
