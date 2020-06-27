import discord
import re

TOKEN = "NzI2NTM0MDUxNjkwOTcxMjE3.XvertQ.LbwYba7ekYRedD0A2nChGGkrH3Y"
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if re.match("test", message.content) and not message.author.bot:
        await message.channel.send("Bonsoir")

client.run(TOKEN)
