import discord
from discord.ext import commands
import nslookup


class CogLookup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dns_query = nslookup.Nslookup(dns_servers=["1.1.1.1"])

    @commands.command(aliases=["nslookup"])
    async def dns_lookup(self, ctx, Domain):
        await self.bot.change_presence(activity=discord.Game(name="dns_lookup"))
        nsRecord = self.dns_query.dns_lookup(Domain)
        await self.bot.change_presence(activity=discord.Game(name="dns_lookup"))
        await ctx.send(f"DNS lookup for `{Domain}`\n"
                       f"``{nsRecord.response_full}``")

    @commands.command()
    async def soa_lookup(self, ctx, Domain):
        await self.bot.change_presence(activity=discord.Game(name="soa_lookup"))
        soaRecord = self.dns_query.soa_lookup(Domain)
        await self.bot.change_presence(activity=discord.Game(name="soa_lookup"))
        await ctx.send(f"SOA lookup for `{Domain}` \n"
                       f"`{soaRecord.response_full}`")
