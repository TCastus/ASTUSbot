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
        for member in ctx.guild.members:
            if MyUtils(ctx.guild).getFuturTCRole() in member.roles:
                await member.remove_roles(MyUtils(ctx.guild).getFuturTCRole())
                await member.add_roles(MyUtils(ctx.guild).get3TCRole())
            elif MyUtils(ctx.guild).get3TCRole() in member.roles:
                await member.remove_roles(MyUtils(ctx.guild).get3TCRole())
                await member.add_roles(MyUtils(ctx.guild).get4TCRole())
            elif MyUtils(ctx.guild).get4TCRole() in member.roles:
                await member.remove_roles(MyUtils(ctx.guild).get4TCRole())
                await member.add_roles(MyUtils(ctx.guild).get5TCRole())
            elif MyUtils(ctx.guild).get5TCRole() in member.roles:
                await member.remove_roles(MyUtils(ctx.guild).get5TCRole(),
                                          MyUtils(ctx.guild).getStudentRole())
                await member.add_roles(MyUtils(ctx.guild).getDiplomesRole())

        await ctx.send("Changement des rôles :) : \n "
                                   " - les Futur sont maintenant des 3TC \n"
                                   " - les 3TC sont maintenant des 4TC \n"
                                   " - les 4TC sont maintenant des 5TC \n"
                                   " - les 5TC sont maintenant des Diplômés \n"
                                   )

