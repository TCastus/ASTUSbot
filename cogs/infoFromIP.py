import discord
from discord.ext import commands
import ipinfo
import ipaddress
import os


async def setup(bot):
    print("Ip info load")
    await bot.add_cog(CogIpInfo(bot))


def valid_ip(address):
    try:
        print(ipaddress.ip_address(address))
        return True
    except ValueError:
        return False


class CogIpInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["ipi"])
    async def ipinfo(self, ctx, IpAddr):

        await self.bot.change_presence(activity=discord.Game(name="IpInfo"))

        if not valid_ip(IpAddr):
            await ctx.send("L'adresse IP n'est pas valid")
        else:
            IPINFO_TOKEN = os.getenv("IPINFO_TOKEN")
            handler = ipinfo.getHandler(access_token=IPINFO_TOKEN)
            details = handler.getDetails(IpAddr)

            ipInfoEmbed = discord.Embed(title="Ip info",
                                        color=0x78a5f9,
                                        description=f"Résultat de la commande IpInfo avec `{IpAddr}`")

            ipInfoEmbed.add_field(name="Hostname : ",
                                  value=details.hostname,
                                  inline=False)

            ipInfoEmbed.add_field(name="Compagnie : ",
                                  value=details.org,
                                  inline=False)

            ipInfoEmbed.add_field(name="Localisation : ",
                                  value=f"Pays : {details.country_name} \n"
                                        f"Region : {details.region} \n"
                                        f"Ville : {details.city} \n"
                                        f"Code postal : {details.postal} \n"
                                        f"Coordonées : {details.latitude}, {details.longitude} \n"
                                        f"Timezone : {details.timezone}")

            await ctx.send(embed=ipInfoEmbed)
