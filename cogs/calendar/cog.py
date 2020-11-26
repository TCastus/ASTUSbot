import re
import os
from os import path

import discord
from discord.ext import commands, tasks
from .util import formatResponse, getCourseByDate, downloadCalendar, getWeekCalendar, getOffset
from datetime import datetime, timedelta

ROOT_CALENDAR = 'cogs/calendar/Assets'


def setup(bot):
    print("Help command load")
    bot.add_cog(CogCalendar(bot))


class CogCalendar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.updateCalendars.start()

    def cog_unload(self):
        self.updateCalendars.cancel()

    @commands.command(aliases=["Calendar", "cal", "calendrier", "semaine", "week"])
    async def calender(self, ctx, arg="4TC2", offset="+0"):
        if re.match(r"(([34])(TC|tc|Tc|tC)([123Aa])|([5])(TC|tc|Tc|tC)([123]))", arg):
            await self.bot.change_presence(activity=discord.Activity(name=f"Calendrier des {arg}",
                                                                     type=discord.ActivityType.watching))
            year = arg[0]
            if arg[-1].isnumeric():
                group = arg[-1]
            else:
                group = "A"
            CalendarPath = ROOT_CALENDAR + f"/{year}TC{group}.ical"
            Offset = getOffset(offset)
            calendar = getWeekCalendar(calendarPath=CalendarPath, offset=Offset)
            await ctx.send("```\n" + str(calendar) + "```\n")
        else:
            await ctx.send("please enter a valid input <year>TC<group>")

    @commands.command(aliases=["Today", "aujourd'hui", "auj", "tod"])
    async def today(self, ctx, arg="4TC2"):
        print(f"Date from command : {datetime.now()}")
        if re.match(r"(([34])(TC|tc|Tc|tC)([123Aa])|([5])(TC|tc|Tc|tC)([123]))", arg):
            await self.bot.change_presence(activity=discord.Activity(name=f"Calendrier des {arg}",
                                                                     type=discord.ActivityType.watching))
            year = arg[0]
            if arg[-1].isnumeric():
                group = arg[-1]
            else:
                group = "A"
            response = ""
            Courses = getCourseByDate(promptDate=datetime.now().date(), calendarPath=ROOT_CALENDAR + f"/{year}TC{group}.ical")
            if not Courses:
                await ctx.send("t'as pas de cours 😄")
            else:
                for course in Courses:
                    response += formatResponse(course) + "\n"
                await ctx.send(response)
        else:
            await ctx.send("please enter a valid input <year>TC<group>")

    @commands.command(aliases=["Tomorrow", "demain", "dem", "tom"])
    async def tomorrow(self, ctx, arg="4TC2"):
        if re.match(r"(([34])(TC|tc|Tc|tC)([123Aa])|([5])(TC|tc|Tc|tC)([123]))", arg):
            await self.bot.change_presence(activity=discord.Activity(name=f"Calendrier des {arg}",
                                                                     type=discord.ActivityType.watching))
            year = arg[0]
            if arg[-1].isnumeric():
                group = arg[-1]
            else:
                group = "A"
            tomorrow = datetime.now() + timedelta(days=1)
            response = ""
            Courses = getCourseByDate(tomorrow.date(), calendarPath=ROOT_CALENDAR + f"/{year}TC{group}.ical")
            if not Courses:
                await ctx.send("t'as pas de cours 😄")
            else:
                for course in Courses:
                    response += formatResponse(course) + "\n"
                await ctx.send(response)
        else:
            await ctx.send("please enter a valid input <year>TC<group>")

    @tasks.loop(hours=48)
    async def updateCalendars(self):
        print("Deleting calendar assets")
        assetsDir = "cogs/calendar/Assets"
        if not path.exists(assetsDir):
            os.makedirs(assetsDir)
        for file in os.listdir(assetsDir):
            os.remove(os.path.join(assetsDir, file))

        downloadCalendar()
