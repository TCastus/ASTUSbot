import discord
from discord.ext import commands


class CogInternational(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def international(self, ctx):
        await self.bot.change_presence(activity=discord.Game(name="Travel"))
        await ctx.send("Tu veux des infos pour l'international \n"
                       "C'est ici que ca se passe :  https://discord.gg/j4EWH3Y")
