import re
import discord
from discord.ext import commands
from .util import formatResponse, getCourseByDate

ROOT_CALENDAR = 'cogs/calendar/Assets'


class CogCalendar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["calendar", "cal", "calendrier"])
    async def calender(self, ctx, arg="4TC2"):
        if re.match(r"(([34])(TC|tc|Tc|tC)([123Aa])|([5])(TC|tc|Tc|tC)([123]))", arg):
            year = arg[0]
            if arg[-1].isnumeric():
                group = arg[-1]
            else:
                group = "A"
            for course in getCourseByDate(calendarPath=ROOT_CALENDAR + f"/{year}TC{group}.ical"):
                await ctx.send(formatResponse(course))
        else:
            await ctx.send("please enter a valid input <year>TC<group>")
