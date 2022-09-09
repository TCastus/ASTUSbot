import discord
from discord.ext import commands


async def setup(bot):
    print("Invitation load")
    await bot.add_cog(CogInvitation(bot))


class CogInvitation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["lien", "invit", "invite"])
    async def invitation(self, ctx):
        await self.bot.change_presence(activity=discord.Game(name="Give invitation"))
        await ctx.send("Tu veux inviter un TC ? un prof? \n"
                       "Voici le lien du serveur :  https://discord.com/invite/ukwVPsA")
