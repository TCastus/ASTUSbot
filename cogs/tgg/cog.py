import discord
from discord.ext import commands
import os
import random
import json

ASSETS_DIR = "cogs/tgg/Assets"
IMAGES_DIR = ASSETS_DIR + "/Images"
QUOTES_FILE = ASSETS_DIR + "/Quote.json"


def setup(bot):
    print("TGG load")
    bot.add_cog(CogTGG(bot))


class CogTGG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["tgg", "thomas","ginny"])
    async def thomasGeorgeGeorge(self, ctx, *args):
        if not args:
            image = random.choice(os.listdir(path=IMAGES_DIR))
            with open(QUOTES_FILE, "r") as file:
                Quotes = json.loads(file.read())["quotes"]
            Quote = random.choice(Quotes)
            ImagePath = IMAGES_DIR + "/" + image
            with open(ImagePath, "rb") as file:
                ImageFile = discord.File(file)
            await ctx.send(content="*"+Quote+"*", file=ImageFile)
        if len(args) != 0:
            if args[0] == "add":
                newQuote = ""
                for word in args[1:]:
                    newQuote += word + " "
                newQuote = newQuote[:-1]
                with open(QUOTES_FILE, "r") as file:
                    Quotes = json.loads(file.read())["quotes"]
                Quotes.append(newQuote)
                with open(QUOTES_FILE, "w") as file:
                    file.write(json.dumps({"quotes": Quotes}))
                await ctx.send(f"New Quote '{newQuote}' saved 🎉")
