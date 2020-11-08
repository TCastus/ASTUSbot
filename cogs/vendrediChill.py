import discord
from discord.ext import commands
from myutils import MyUtils
import random


class CogVendrediChill(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def showChannel(self, ctx):
        if MyUtils(ctx.guild).G4check(ctx):
            category = await ctx.guild.create_category("🎉Vendredi Chill🎉")
            await ctx.guild.create_text_channel(f"General", category=category)
            await ctx.guild.create_voice_channel(f"General", category=category)
            for i in range(15):
                await ctx.guild.create_voice_channel(f"lobby-{i+1}", category=category)

    @commands.command()
    async def hideChannel(self, ctx):
        if MyUtils(ctx.guild).G4check(ctx):
            categoty = MyUtils(ctx.guild).getVendrediChillCategory()
            for channels in categoty.channels:
                await channels.delete()
            await categoty.delete()

    @commands.command()
    async def shufle(self, ctx):
        if MyUtils(ctx.guild).G4check(ctx):
            category = MyUtils(ctx.guild).getVendrediChillCategory()
            generalChan = discord.utils.get(category.voice_channels, name="General")
            lobbyChan = category.voice_channels
            lobbyChan.pop(0)
            print(lobbyChan)
            random.shuffle(lobbyChan)
            conectedMenmbers = generalChan.members
            random.shuffle(conectedMenmbers)
            for member in conectedMenmbers:
                print(member)
                randomLobby = lobbyChan[random.randint(0, len(lobbyChan)-1)]
                print(randomLobby)
                await member.move_to(randomLobby)
                if len(randomLobby.members) == 5:
                    lobbyChan.pop(lobbyChan.index(randomLobby))
