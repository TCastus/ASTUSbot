import discord
from discord.ext import commands
from myutils import MyUtils
import embed


class CogNewyear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, subject=""):

        subject = subject.lower()

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
            else:
                await ctx.send("Désolé, je ne sais pas te donner de l'aide sur ce sujet... \n "
                                           "Peut-être que tu trouvera un réponse sur le repo "
                                           "[TChelp](https://github.com/TCastus/TChelp) :wink: ")

