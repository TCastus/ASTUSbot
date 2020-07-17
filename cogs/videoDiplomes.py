import discord
from discord.ext import commands
import embed


class CogVideoDiplomes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["futur"])
    async def metier(self, ctx):
        await ctx.send(embed=embed.videoDiplomesEmbed)