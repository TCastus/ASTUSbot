import discord
from discord.ext import commands
from myutils import MyUtils


async def setup(bot):
    print("Admin load")
    await bot.add_cog(CogAdmin(bot))


class CogAdmin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        return MyUtils(ctx.guild).getAdminRole() in ctx.message.author.roles

    @commands.command()
    async def admin(self, ctx):
        await MyUtils(ctx.guild).setAdminRole(ctx.message.content.split(" ")[1])
