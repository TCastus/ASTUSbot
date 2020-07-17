import discord


class Roles:
    def __init__(self, guild):
        self.student = discord.utils.get(guild.roles, name="Student")
        self.new3TC = discord.utils.get(guild.roles, name="Futur TC")
        self.troisTC = discord.utils.get(guild.roles, name="3 TC")
        self.quatreTC = discord.utils.get(guild.roles, name="4 TC")
        self.cinqTC = discord.utils.get(guild.roles, name="5 TC")
        self.TCA = discord.utils.get(guild.roles, name="TCA")
        self.prof = discord.utils.get(guild.roles, name="prof")
        self.diplomes = discord.utils.get(guild.roles, name="Diplômés")
        self.g4 = discord.utils.get(guild.roles, name="G4")
        self.astus = discord.utils.get(guild.roles, name="ASTUS")
        self.teamEvent = discord.utils.get(guild.roles, name="Team Event")
        self.respTeamEvent = discord.utils.get(guild.roles, name="Resp Team Event")
        self.teamEts = discord.utils.get(guild.roles, name="Team Entreprise")
        self.respTeamEts = discord.utils.get(guild.roles, name="Resp Team Entreprise")
        self.respSite = discord.utils.get(guild.roles, name="Resp Site International")
        self.ancienRespSite = discord.utils.get(guild.roles, name="Ancien Resp Site International")
        self.respComm = discord.utils.get(guild.roles, name="Resp Comm")
