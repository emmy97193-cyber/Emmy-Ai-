import discord
import os
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} is Online!')
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if bot.user.mentioned_in(message):
        await message.channel.send(f"Hi {message.author.mention}! I'm Emmy Ai 😊 How can I help you?")
    if "hello" in message.content.lower():
        await message.channel.send(f"Hello {message.author.mention}!")
bot.run(os.getenv("DISCORD_TOKEN"))
