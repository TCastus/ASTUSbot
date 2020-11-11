import discord
from discord.ext import commands
import embed


def setup(bot):
    print("Video diplomes load")
    bot.add_cog(CogVideoDiplomes(bot))


class CogVideoDiplomes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["futur", "video"])
    async def metier(self, ctx):
        await self.bot.change_presence(activity=discord.Activity(name="Videos des diplômés",
                                                                 type=discord.ActivityType.watching))
        await ctx.send(embed=embed.videoDiplomesEmbed)
