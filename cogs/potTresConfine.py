import discord
from discord.ext import commands
from myutils import MyUtils
import random
import os
import asyncio


def setup(bot):
    print("Pot très confiné load")
    bot.add_cog(CogPotTresConfine(bot))


class CogPotTresConfine(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.microOnde = [
            "https://tenor.com/view/microwave-gif-18041779",
        ]


    @commands.command()
    async def CreatePot(self, ctx):
        if MyUtils(ctx.guild).G4check(ctx):
            await self.bot.change_presence(activity=discord.Game(name="Prepare le Pot TC"))
            category = await ctx.guild.create_category("Pot Très Confiné")
            await ctx.guild.create_text_channel(f"General", category=category)
            await ctx.guild.create_voice_channel(f"General", category=category)
        else:
            raise discord.ext.commands.CheckFailure

    @commands.command()
    async def DestroyPot(self, ctx):
        if MyUtils(ctx.guild).G4check(ctx):
            await self.bot.change_presence(activity=discord.Game(name="Toutes les bonnes choses ont une fin"))
            categoty = MyUtils(ctx.guild).getPotTresConfineCategory()
            for channels in categoty.channels:
                await channels.delete()
            await categoty.delete()
        else:
            raise discord.ext.commands.CheckFailure

    @commands.command()
    async def Repartition(self, ctx, number=8):
        if MyUtils(ctx.guild).G4check(ctx):
            await self.bot.change_presence(activity=discord.Game(name="Réparti les joueurs"))
            category = MyUtils(ctx.guild).getPotTresConfineCategory()
            generalChanID = discord.utils.get(category.voice_channels, name="General").id

            # il faut implémenter un créateur de catégorie en fonction de gens qui sont présents
            nbUsers = 0
            for memberID in [i for i in self.bot.get_channel(generalChanID).voice_states.keys()]:
                nbUsers += 1
            for i in range(int((nbUsers/8))+1):
                await ctx.guild.create_voice_channel(f"lobby-{i + 1}", category=category)

            voiceChannel = category.voice_channels
            voiceChannel.pop(0)
            print(voiceChannel)
            random.shuffle(voiceChannel)

            for memberID in [i for i in self.bot.get_channel(generalChanID).voice_states.keys()]:
                member = await ctx.guild.fetch_member(memberID)
                try:
                    while True:
                        randomLobby = voiceChannel[random.randint(0, len(voiceChannel) - 1)]
                        print(randomLobby)
                        if len(randomLobby.members) == number:
                            print("pop")
                            voiceChannel.pop(voiceChannel.index(randomLobby))
                        else:
                            break
                    await member.move_to(randomLobby)
                except ValueError:
                    await ctx.send("Woups... Quelque chose c'est mal passé")
        else:
            raise discord.ext.commands.CheckFailure

    @commands.command()
    async def Rassemblement(self, ctx):
        if MyUtils(ctx.guild).G4check(ctx):
            await self.bot.change_presence(activity=discord.Game(name="Rassemble les joueurs"))
            category = MyUtils(ctx.guild).getPotTresConfineCategory()
            generalChanID = discord.utils.get(category.voice_channels, name="General").id
            voiceChannel = category.voice_channels
            voiceChannel.pop(0)

            # Loop qui parcours les lobby et move les members vers voice général, puis détruit tous les autres voice channels que général
            print(len(voiceChannel))
            print(voiceChannel[0])
            print(voiceChannel[1])
            for chan in voiceChannel.id:
                print(chan)
                for mem in chan.members:
                    print(mem)
                    await mem.move_to(generalChanID)
                chan.delete()
        else:
            raise discord.ext.commands.CheckFailure