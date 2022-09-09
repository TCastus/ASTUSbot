import discord
from discord.ext import commands


async def setup(bot):
    print("Stage load")
    await bot.add_cog(CogStage(bot))


class CogStage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["livret"])
    async def stage(self, ctx):
        await self.bot.change_presence(activity=discord.Game(name="Working..."))
        await ctx.send("Tu veux des infos pour ton stage \n"
                       "C'est ici que ca se passe :  https://tinyurl.com/tc-stages")

    @commands.command(aliases=["travail", "work"])
    async def offre(self, ctx):
        await self.bot.change_presence(activity=discord.Game(name="#OPENTOWORK"))
        await ctx.send("Tu cherche un stage \n"
                       "C'est ici que ca se passe :  https://tinyurl.com/tc-offres")
