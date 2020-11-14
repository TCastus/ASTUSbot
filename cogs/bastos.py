import discord
from discord.ext import commands


def setup(bot):
    print("Bastian Twitch load")
    bot.add_cog(CogBastosTwitch(bot))


class CogBastosTwitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["bastos", "bastian", "courirvite", "banzai"])
    async def twitch(self, ctx):
        await self.bot.change_presence(activity=discord.Game(name="faire de la pub"))
        await ctx.send(":zap: Pour suivre les lives de Bastian (4TC) c'est par là : https://twitch.tv/Banzai99 :zap:")
