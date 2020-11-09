import discord
from discord.ext import commands
from .util import formatResponse, getCourseByDate


class CogCalendar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["calendar", "cal", "calendrier"])
    async def calender(self, ctx):
        for course in getCourseByDate():
            await ctx.send(formatResponse(course))
