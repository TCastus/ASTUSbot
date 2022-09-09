import discord
from discord.ext import commands
import random
import json


async def setup(bot):
    print("Memes load")
    await bot.add_cog(CogMeme(bot))


class CogMeme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = json.load(open("cogs/memes/assets/data.json", "r"))

    @commands.command(aliases=["memes"])
    async def meme(self, ctx):
        await self.bot.change_presence(activity=discord.Activity(name="🤣 Des memes rigolot",
                                                                 type=discord.ActivityType.watching))
        randomPost = random.choice(self.db)
        try:
            msg = randomPost["message"]
        except KeyError:
            msg = ""
        embed = discord.Embed(
            title="Clique ici pour le voir sur facebook",
            url=randomPost["attachments"]["data"][0]["url"],
            color=int(hex(random.randint(0, 16777215)), 16),
            description=msg,
        )
        embed.set_image(url=randomPost["attachments"]["data"][0]["media"]["image"]["src"])
        embed.set_author(name="TC Memes Officiel",
                         url="https://www.facebook.com/mieuxquetcmemes",
                         icon_url="https://scontent-cdg2-1.xx.fbcdn.net/v/t1.0-9"
                                  "/75543605_121438329279422_6240442933963653120_o.jpg?_nc_cat=107&ccb=2&_nc_sid"
                                  "=09cbfe&_nc_ohc=xohKWDoJq90AX9-W5uA&_nc_ht=scontent-cdg2-1.xx&oh"
                                  "=3e18e6ec0ffdc9cdf56965a6a3d11d16&oe=600ECB19")
        await ctx.send(embed=embed)
