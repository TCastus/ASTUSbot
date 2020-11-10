import re
import discord
from discord.ext import commands
from .util import formatResponse, getCourseByDate
from datetime import datetime, timedelta
ROOT_CALENDAR = 'cogs/calendar/Assets'


class CogCalendar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["Calendar", "cal", "calendrier"])
    async def calender(self, ctx, arg="4TC2"):
        if re.match(r"(([34])(TC|tc|Tc|tC)([123Aa])|([5])(TC|tc|Tc|tC)([123]))", arg):
            year = arg[0]
            if arg[-1].isnumeric():
                group = arg[-1]
            else:
                group = "A"
            response = ""
            Courses = getCourseByDate(calendarPath=ROOT_CALENDAR + f"/{year}TC{group}.ical")
            if not Courses:
                await ctx.send("t'as pas de cours 😄")
            else:
                for course in Courses:
                    response += formatResponse(course) + "\n"
                await ctx.send(response)
        else:
            await ctx.send("please enter a valid input <year>TC<group>")

    @commands.command(aliases=["Tomorrow", "demain", "dem","tom"])
    async def tomorrow(self, ctx, arg="4TC2"):
        if re.match(r"(([34])(TC|tc|Tc|tC)([123Aa])|([5])(TC|tc|Tc|tC)([123]))", arg):
            year = arg[0]
            if arg[-1].isnumeric():
                group = arg[-1]
            else:
                group = "A"
            tomorrow = datetime.now() + timedelta(days=1)
            response = ""
            Courses = getCourseByDate(tomorrow.date(),calendarPath=ROOT_CALENDAR + f"/{year}TC{group}.ical")
            if not Courses:
                await ctx.send("t'as pas de cours 😄")
            else:
                for course in Courses:
                    response += formatResponse(course) + "\n"
                await ctx.send(response)
        else:
            await ctx.send("please enter a valid input <year>TC<group>")
