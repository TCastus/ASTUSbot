import discord
from discord.ext import commands


class CogInvitation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["lien"])
    async def invitation(self, ctx):
        await ctx.send("Tu veux inviter un TC ? un prof? \n"
                       "Voici le lien du serveur :  https://discord.com/invite/ukwVPsA")
