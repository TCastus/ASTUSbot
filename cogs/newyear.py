import discord
from discord.ext import commands
from myutils import MyUtils


class CogNewyear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.passationStatus = 0

    async def cog_check(self, ctx):
        return MyUtils(ctx.guild).getG4Role() in ctx.message.author.roles

    @commands.command(aliases=["ny"])
    async def newyear(self, ctx):
        await ctx.send("ok, nouvelle annee")

