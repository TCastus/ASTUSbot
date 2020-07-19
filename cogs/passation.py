import discord
from discord.ext import commands
from myutils import MyUtils
import datetime
import perms


class CogPassation(commands.Cog):
    def __init__(self, bot, prefix):
        self.bot = bot
        self.PREFIX = prefix
        self.passationStatus = 0

    async def cog_check(self, ctx):
        return MyUtils(ctx.guild).getG4Role() in ctx.message.author.roles

    @commands.command()
    async def passation(self, ctx):

        if self.passationStatus > 0:
            await ctx.send("Passation déjà en cours ... ")
            return

        # Creation du role
        oldG4 = await ctx.guild.create_role(
            name=f"G4 {datetime.datetime.now().year - 1}-{datetime.datetime.now().year}",
            permissions=discord.Permissions(1333259863),
            colour=discord.Colour(2123412)
        )

        # attributions des roles au channels

        await MyUtils(ctx.guild).getG4TxtChannel().set_permissions(oldG4, overwrite=perms.g4TxtPerms)
        await MyUtils(ctx.guild).getG4VocalChannel().set_permissions(oldG4, overwrite=perms.g4VocalPerms)

        await ctx.send("Je cherche les anciens membres de l'ASTUS, patiente un moment...")
        for member in ctx.guild.members:
            if MyUtils(ctx.guild).getG4Role() in member.roles:
                await member.remove_roles(MyUtils(ctx.guild).getG4Role())
                await member.add_roles(oldG4)
            if MyUtils(ctx.guild).getASTUSRole() in member.roles:
                await member.remove_roles(MyUtils(ctx.guild).getASTUSRole())
            if MyUtils(ctx.guild).getRespCommRole() in member.roles:
                await member.remove_roles(MyUtils(ctx.guild).getRespCommRole())
            if MyUtils(ctx.guild).getRespSiteRole() in member.roles:
                await member.remove_roles(MyUtils(ctx.guild).getRespSiteRole())
                await member.add_roles(MyUtils(ctx.guild).getAncienRespSiteRole())
            if MyUtils(ctx.guild).getRespTeamEntrepriseRole() in member.roles:
                await member.remove_roles(MyUtils(ctx.guild).getRespTeamEntrepriseRole())
            if MyUtils(ctx.guild).getRespTeamEventRole() in member.roles:
                await member.remove_roles(MyUtils(ctx.guild).getRespTeamEventRole())
            if MyUtils(ctx.guild).getAncienRespSiteRole() in member.roles:
                await member.remove_roles(MyUtils(ctx.guild).getAncienRespSiteRole())
            if MyUtils(ctx.guild).getTeamEventRole() in member.roles:
                await member.remove_roles(MyUtils(ctx.guild).getTeamEventRole())
            if MyUtils(ctx.guild).getTeamEntrepriseRole() in member.roles:
                await member.remove_roles(MyUtils(ctx.guild).getTeamEntrepriseRole())

        self.passationStatus += 1
        await ctx.send("Les anciens membres de l'ASTUS ne font plus partis de l'ASTUS")
        await ctx.send("Qui sont les nouveaux membres du G4 ? ")

        def checkMessage(message):
            return message.author == ctx.message.author and ctx.message.channel == message.channel

        while self.passationStatus > 0:
            try:
                if self.passationStatus == 1:
                    newG4 = await self.bot.wait_for("message", check=checkMessage)
                    members = newG4.content.split(" ")
                    if len(members) != 4:
                        await ctx.send("Le G4 doit être composé de 4 membres")
                    else:
                        await MyUtils(ctx.guild).newAstus(members,
                                                          MyUtils(ctx.guild).getASTUSRole(),
                                                          MyUtils(ctx.guild).getG4Role())
                        await ctx.send("Qui sont les membres de la team Event ?")
                        self.passationStatus += 1

                if self.passationStatus == 2:
                    newTeamEvent = await self.bot.wait_for("message", check=checkMessage)
                    members = newTeamEvent.content.split(" ")
                    if len(members) != 3:
                        await ctx.send("La team event doit être composée de 3 membres \n"
                                       "Le responsable te sera demandé juste aprés")
                    else:
                        await MyUtils(ctx.guild).newAstus(members,
                                                          MyUtils(ctx.guild).getASTUSRole(),
                                                          MyUtils(ctx.guild).getTeamEventRole())
                        await ctx.send("Qui est le resp de la team Event ?")
                        self.passationStatus += 1

                if self.passationStatus == 3:
                    newRespTeamEvent = await self.bot.wait_for("message", check=checkMessage)
                    members = newRespTeamEvent.content.split(" ")
                    if len(members) != 1:
                        await ctx.send("Il n'y a qu'un responsable de la team event")
                    else:
                        await MyUtils(ctx.guild).newAstus(members,
                                                          MyUtils(ctx.guild).getASTUSRole(),
                                                          MyUtils(ctx.guild).getRespTeamEventRole())
                        await ctx.send("Qui sont les membres de la team Entreprise ?")
                        self.passationStatus += 1

                if self.passationStatus == 4:
                    newTeamEntreprise = await self.bot.wait_for("message", check=checkMessage)
                    members = newTeamEntreprise.content.split(" ")
                    if len(members) != 3:
                        await ctx.send("La team Entreprise doit être composée de 3 membres \n"
                                       "Le responsable te sera demandé juste apres")
                    else:
                        await MyUtils(ctx.guild).newAstus(members,
                                                          MyUtils(ctx.guild).getASTUSRole(),
                                                          MyUtils(ctx.guild).getTeamEntrepriseRole())
                        await ctx.send("Qui est le resp de la team Entreprise ?")
                        self.passationStatus += 1

                if self.passationStatus == 5:
                    newRespTeamEntreprise = await self.bot.wait_for("message", check=checkMessage)
                    members = newRespTeamEntreprise.content.split(" ")
                    if len(members) != 1:
                        await ctx.send("Il n'y a qu'un responsable de la team Entreprise")
                    else:
                        await MyUtils(ctx.guild).newAstus(members,
                                                          MyUtils(ctx.guild).getASTUSRole(),
                                                          MyUtils(ctx.guild).getRespTeamEntrepriseRole())
                        await ctx.send("Qui est le resp site international ?")
                        self.passationStatus += 1

                if self.passationStatus == 6:
                    newRespSite = await self.bot.wait_for("message", check=checkMessage)
                    members = newRespSite.content.split(" ")
                    if len(members) != 1:
                        await ctx.send("Il n'y a qu'un responsable du site")
                    else:
                        await MyUtils(ctx.guild).newAstus(members,
                                                          MyUtils(ctx.guild).getASTUSRole(),
                                                          MyUtils(ctx.guild).getRespSiteRole())
                        await ctx.send("Qui est le resp comm ?")
                        self.passationStatus += 1

                if self.passationStatus == 7:
                    newRespComm = await self.bot.wait_for("message", check=checkMessage)
                    members = newRespComm.content.split(" ")
                    if len(members) != 1:
                        await ctx.send("Il n'y a qu'un responsable comm")
                    else:
                        await MyUtils(ctx.guild).newAstus(members,
                                                          MyUtils(ctx.guild).getASTUSRole(),
                                                          MyUtils(ctx.guild).getRespCommRole())
                        await ctx.send("Tape ``end`` pour finir")
                        self.passationStatus += 1

                if self.passationStatus == 8:
                    end = await self.bot.wait_for("message", check=checkMessage)
                    if end.content == "end":
                        self.passationStatus = 0
                        await ctx.send("Passation finie !")
                    else:
                        await ctx.send("Tu dois taper ``end`` pour finir la passation")
            except Exception:
                await ctx.send("Une erreur est survenue...")

        await ctx.send("Content d'avoir été à tes côtés pendant ton mandat :wink:")

    @commands.command()
    async def pasation(self, ctx):
        await ctx.send("Essaie plutot ``" + self.PREFIX + "passation``")

    @passation.error
    async def passationError(self, ctx, error):
        await ctx.send("petit pb...")
        await ctx.send(error)
