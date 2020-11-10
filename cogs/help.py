import discord
from discord.ext import commands
from myutils import MyUtils
import embed


def setup(bot):
    print("Help command load")
    bot.add_cog(CogHelp(bot))


async def HelpCommand(ctx, embedMessage):
    if MyUtils(ctx.guild).G4check(ctx):
        await ctx.send(embed=embedMessage)
    else:
        await ctx.send("Je ne peux pas te donner de l'aide sur cette commande, tu ne peux pas l'utiliser")


class CogHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, subject=""):

        subject = subject.lower()

        await self.bot.change_presence(activity=discord.Game(name="Help"))

        if MyUtils(ctx.guild).G4check(ctx) and subject == "":
            await ctx.send(embed=embed.g4helpEmbed)

        elif (MyUtils(ctx.guild).G4check(ctx) and subject == "nog4help") \
                or (subject == ""):
            await ctx.send(embed=embed.helpEmbed)

        elif subject != "":
            if subject == "ssh":
                await ctx.send(embed=embed.sshEmbed)

            elif subject == "rdp":
                await ctx.send(embed=embed.rdpEmbed)

            elif subject == "vpn":
                await ctx.send(embed=embed.vpnEmbed)

            elif subject in ["terminal", "cli", "ilc"]:
                await ctx.send(embed=embed.terminalEmbed)

            elif subject in ["git", "github"]:
                await ctx.send("Git / GitHub : \n"
                               "Voici de l'aide sur TChelp : \n"
                               "https://github.com/TCastus/TChelp/blob/master/Git_GitHub"
                               "/Presentation.md")

            elif subject == "tsa":
                await ctx.send("TSA... :sweat_smile: \n"
                               "Je suis vraiment désolé mais je suis dans l'incapacité de te "
                               "donner de l'aide sur ce sujet :no_mouth:")

            elif subject == "passation":
                await HelpCommand(ctx, embed.helpPassationEmbed)
            elif subject == "newyear":
                await HelpCommand(ctx, embed.helpNewyearEmbed)
            elif subject == "vendredichill":
                await HelpCommand(ctx, embed.helpVendrediChill)
            elif subject in ["invitation", "lien"]:
                await ctx.send(embed=embed.helpInvitationEmbed)
            elif subject in ["video", "metier", "futur"]:
                await ctx.send(embed=embed.helpvideoEmbed)
            elif subject in ["ipinfo", "ipi"]:
                await ctx.send(embed=embed.helpIpInfo)
            elif subject in ["nslookup", "dns_lookup"]:
                await ctx.send(embed=embed.helpDns_lookup)
            elif subject == "soa_lookup":
                await ctx.send(embed=embed.helpSoa_lookup)

            else:
                await ctx.send("Désolé, je ne sais pas te donner de l'aide sur ce sujet... \n "
                               "Peut-être que tu trouveras une réponse sur le repo "
                               "[TChelp](https://github.com/TCastus/TChelp) :wink: ")
