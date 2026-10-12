import os,io
import discord
from discord.ext import commands
from PIL import Image
from wallpaper import make_wallpapers

intents=discord.Intents.default()
intents.message_content=True
bot=commands.Bot("!",intents=intents)

@bot.event
async def on_ready():
 print("Emmy-Ai Online")

@bot.command()
async def ping(ctx):
 await ctx.send("Pong!")

@bot.command()
async def wallpaper(ctx):
 if not ctx.message.attachments:
  await ctx.send("Attach img!")
  return
 await ctx.send("Making...")
 r=await ctx.message.attachments[0].read()
 im=Image.open(io.BytesIO(r))
 im=im.convert("RGBA")
 h,l=make_wallpapers(im)
 fs=[]
 for idx,img in enumerate([h,l]):
  b=io.BytesIO()
  img.save(b,format="PNG")
  b.seek(0)
  n="home.png" if idx==0 else "lock.png"
  fs.append(discord.File(b,n))
 await ctx.send("Here!",files=fs)

@bot.command()
async def identify(ctx):
 if not ctx.message.attachments:
  await ctx.send("Attach snake pic!")
  return
 await ctx.send(
  "**Green Tree Python**\n"
  "*Morelia viridis*\n\n"
  "Bright green, coiled on branch.\n"
  "Arboreal, nocturnal.\n"
  "Perfect for dark lockscreen!"
 )

t=os.getenv("DISCORD_TOKEN")
if t:
 bot.run(t.strip())
