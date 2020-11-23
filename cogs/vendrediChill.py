import discord
from discord.ext import commands
from myutils import MyUtils
import random
import asyncio


def setup(bot):
    print("Vendredi Chill load")
    bot.add_cog(CogVendrediChill(bot))


class CogVendrediChill(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cookies = [
            "https://tenor.com/view/cookie-monster-om-nom-omnomnom-sesame-gif-10644609",
            "https://img2.freepng.fr/20180701/yyq/kisspng-chocolate-chip-cookie-cookie-monster-macaron-biscu"
            "-crazy-cartoon-5b38b0743f46d3.7361440815304418442592.jpg",
            "https://media.tenor.com/images/12fbaab498da0df08b4b7086954d5016/tenor.gif",
            "https://media.tenor.com/images/626d54f8905f7fc267bb365f2aca4254/tenor.gif",
            "https://media.tenor.com/images/53f9792c40f8c93e26b85c15bd28d175/tenor.gif",
        ]
        self.brownies = [
            "https://i.pinimg.com/originals/b5/d3/44/b5d3445904e0fa9ffc0452f4a09afc5c.jpg",
            "https://media.tenor.com/images/d99b1a30fc5e1fff78109930cab58ba9/tenor.gif",
            "https://media.tenor.com/images/5910b399aad3a16a71faf11a1b1239a2/tenor.gif",
            "https://media.tenor.com/images/bd022b60e0c69c4068eb47d7dfdc4edc/tenor.gif",
        ]
        self.beers = [
            ":beers:",
            ":beer:",
            "https://media.tenor.com/images/218d4f5fd06af8ca4b2f9d7c524f1a59/tenor.gif",
            "https://media.tenor.com/images/d44815a7735a0b7adc72c6bdba072fbc/tenor.gif",
            "https://media.tenor.com/images/42b7583994f574f0a6521197d0454c33/tenor.gif",
            "https://media.tenor.com/images/da89e4634ed028230dc5fb0a5a112174/tenor.gif",
            "https://media.tenor.com/images/3b07b01b63abbdd75f3c54bce3841212/tenor.gif",
        ]

    @commands.command()
    async def showChannel(self, ctx, number=15):
        if MyUtils(ctx.guild).G4check(ctx):
            await self.bot.change_presence(activity=discord.Game(name="Prepare le vendredi chill"))
            category = await ctx.guild.create_category("🎉Vendredi Chill🎉")
            await ctx.guild.create_text_channel(f"General", category=category)
            await ctx.guild.create_voice_channel(f"General", category=category)
            for i in range(number):
                await ctx.guild.create_voice_channel(f"lobby-{i + 1}", category=category)
        else:
            raise discord.ext.commands.CheckFailure

    @commands.command()
    async def hideChannel(self, ctx):
        if MyUtils(ctx.guild).G4check(ctx):
            await self.bot.change_presence(activity=discord.Game(name="Désinstalle le vendredi chill"))
            categoty = MyUtils(ctx.guild).getVendrediChillCategory()
            for channels in categoty.channels:
                await channels.delete()
            await categoty.delete()
        else:
            raise discord.ext.commands.CheckFailure

    @commands.command()
    async def shufle(self, ctx, number=6):
        if MyUtils(ctx.guild).G4check(ctx):
            await self.bot.change_presence(activity=discord.Game(name="Attribu des lobby"))
            category = MyUtils(ctx.guild).getVendrediChillCategory()
            lobbyChan = category.voice_channels
            lobbyChan.pop(0)
            print(lobbyChan)
            random.shuffle(lobbyChan)
            generalChanID = discord.utils.get(category.voice_channels, name="General").id
            for memberID in [i for i in self.bot.get_channel(generalChanID).voice_states.keys()]:
                member = await ctx.guild.fetch_member(memberID)
                try:
                    while True:
                        randomLobby = lobbyChan[random.randint(0, len(lobbyChan) - 1)]
                        print(randomLobby)
                        if len(randomLobby.members) == number:
                            print("pop")
                            lobbyChan.pop(lobbyChan.index(randomLobby))
                        else:
                            break
                    await member.move_to(randomLobby)
                except ValueError:
                    await ctx.send("Woups... Quelque chose c'est mal passé")
        else:
            raise discord.ext.commands.CheckFailure

    @commands.command()
    async def brownie(self, ctx):
        await self.bot.change_presence(activity=discord.Game(name="mange une part de brownie"))
        await ctx.send(random.choice(self.brownies))

    @commands.command(aliases=["biere"])
    async def beer(self, ctx):
        await self.bot.change_presence(activity=discord.Game(name="Boit une bonne biere"))
        await ctx.send(random.choice(self.beers))

    @commands.command()
    async def cookie(self, ctx):
        await self.bot.change_presence(activity=discord.Game(name="Mange un cookie"))
        await ctx.send(random.choice(self.cookies))

    @commands.command(aliases=["beerscookiebrownies", "cookiebeerbrownies"])
    async def browniesbeercookie(self, ctx):
        await self.bot.change_presence(activity=discord.Game(name="Se fait un bon goûter"))
        await ctx.send(random.choice(self.beers))
        await ctx.send(random.choice(self.brownies))
        await ctx.send(random.choice(self.cookies))

    @commands.command(aliases=["gateau"])
    async def cake(self, ctx, number=3):
        await self.bot.change_presence(activity=discord.Game(name="Fête ses 22 ans"))
        count = 0

        def checkMessage(message):
            return message.channel == ctx.message.channel

        msg = await ctx.send(":birthday:" * number)
        try:
            print(number*1.5)
            while count < number*1.5:
                soufle = await self.bot.wait_for("message", timeout=15, check=checkMessage)
                if soufle.content == "🌬️":
                    count += 1
            await msg.edit(content=":moon_cake:" * number)
        except:
            if count == 0:
                await ctx.send("Personne n'a souflé... \n "
                               "Le gateau a pris feu :fire:")
            else:
                await ctx.send("Vous n'avez pas assez souflé... \n "
                               "Le gateau a pris feu :fire:")
            await msg.edit(content=":fire:" * number)
            return
