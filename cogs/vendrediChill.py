import discord
from discord.ext import commands
from myutils import MyUtils
import random
import time


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
                await ctx.guild.create_voice_channel(f"lobby-{i + 1}", category=category)

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
                randomLobby = lobbyChan[random.randint(0, len(lobbyChan) - 1)]
                print(randomLobby)
                await member.move_to(randomLobby)
                if len(randomLobby.members) == 5:
                    lobbyChan.pop(lobbyChan.index(randomLobby))

    @commands.command()
    async def brownie(self, ctx):
        await ctx.send("https://i.pinimg.com/originals/b5/d3/44/b5d3445904e0fa9ffc0452f4a09afc5c.jpg")

    @commands.command(aliases=["biere"])
    async def beer(self, ctx):
        await ctx.send(":beers:")

    @commands.command()
    async def cookie(self, ctx):
        await ctx.send("https://img2.freepng.fr/20180701/yyq/kisspng-chocolate-chip-cookie-cookie-monster-macaron"
                       "-biscu-crazy-cartoon-5b38b0743f46d3.7361440815304418442592.jpg")

    @commands.command(aliases=["gateau"])
    async def cake(self, ctx):
        count = 0

        def checkMessage(message):
            return message.channel == ctx.message.channel

        msg = await ctx.send(":birthday:" * 3)
        try:
            while count < 5:
                soufle = await self.bot.wait_for("message", timeout=15, check=checkMessage)
                if soufle.content == "🌬️":
                    count += 1
            await msg.edit(content=":moon_cake:" * 3)
        except:
            if count == 0:
                await ctx.send("Personne n'a souflé... \n "
                               "Le gateau a pris feu :fire:")
            else:
                await ctx.send("Vous n'avez pas assez souflé... \n "
                               "Le gateau a pris feu :fire:")
            await msg.edit(content=":fire:" * 3)
            return
