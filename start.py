import discord
import os

TOKEN = os.getenv("BOT_TOKEN")
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if not message.author.bot:
        if message.content == "ping":
            await message.channel.send("pong")

client.run(TOKEN)
