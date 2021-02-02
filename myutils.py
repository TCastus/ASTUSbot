import discord


class MyUtils:
    def __init__(self, guild):
        self.guild = guild

    def getStudentRole(self):
        return discord.utils.get(self.guild.roles, name="Student")

    def getFuturTCRole(self):
        return discord.utils.get(self.guild.roles, name="Futur TC")

    def get3TCRole(self):
        return discord.utils.get(self.guild.roles, name="3 TC")

    def get4TCRole(self):
        return discord.utils.get(self.guild.roles, name="4 TC")

    def get5TCRole(self):
        return discord.utils.get(self.guild.roles, name="5 TC")

    def getTCARole(self):
        return discord.utils.get(self.guild.roles, name="TCA")

    def getProfRole(self):
        return discord.utils.get(self.guild.roles, name="prof")

    def getDiplomesRole(self):
        return discord.utils.get(self.guild.roles, name="Diplômés")

    def getG4Role(self):
        return discord.utils.get(self.guild.roles, name="G4")

    def getASTUSRole(self):
        return discord.utils.get(self.guild.roles, name="ASTUS")

    def getTeamEventRole(self):
        return discord.utils.get(self.guild.roles, name="Team Event")

    def getRespTeamEventRole(self):
        return discord.utils.get(self.guild.roles, name="Resp Team Event")

    def getTeamEntrepriseRole(self):
        return discord.utils.get(self.guild.roles, name="Team Entreprise")

    def getRespTeamEntrepriseRole(self):
        return discord.utils.get(self.guild.roles, name="Resp Team Entreprise")

    def getRespSiteRole(self):
        return discord.utils.get(self.guild.roles, name="Resp Site International")

    def getAncienRespSiteRole(self):
        return discord.utils.get(self.guild.roles, name="Ancien Resp Site International")

    def getRespCommRole(self):
        return discord.utils.get(self.guild.roles, name="Resp Comm")

    def getEntrepriseRole(self):
        return discord.utils.get(self.guild.roles, name="Entreprise")

    def getAdminRole(self):
        return discord.utils.get(self.guild.roles, name="Admin")

    def getFuturAstusRole(self):
        return discord.utils.get(self.guild.roles, name="Futur ASTUS ?")

    def getOrgaSoireeRole(self):
        return discord.utils.get(self.guild.roles, name="Orga soirée")

    def getG4TxtChannel(self):
        return discord.utils.get(self.guild.channels, id=726554977753104464)

    def getG4VocalChannel(self):
        return discord.utils.get(self.guild.channels, id=726555448739758151)

    def getPassationTxtChannel(self):
        return discord.utils.get(self.guild.channels, id=726555017389277235)

    def getPassationVocalChannel(self):
        return discord.utils.get(self.guild.channels, id=726555473872027729)

    def getVendrediChillCategory(self):
        return discord.utils.get(self.guild.categories, name="🎉Vendredi Chill🎉")

    def getPotTresConfineCategory(self):
        return discord.utils.get(self.guild.categories, name="Pot Très Confiné")

    def getLanOneCategory(self, name):
        return discord.utils.get(self.guild.categories, name=name)

    async def newAstus(self, members, *roles):
        for memberStr in members:
            memberID = memberStr[2:-1] if memberStr[2:-1][0] != "!" else memberStr[2:-1][1:]
            member = self.guild.get_member(user_id=int(memberID))
            for role in roles:
                await member.add_roles(role)

    def G4check(self, ctx):
        return self.getG4Role() in ctx.message.author.roles

    def OrgaSoireeCheck(self, ctx):
        return self.getOrgaSoireeRole() in ctx.message.author.roles
