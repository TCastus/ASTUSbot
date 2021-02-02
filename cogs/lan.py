import discord
from discord.ext import commands
from myutils import MyUtils
import asyncio


def setup(bot):
    print("LAN TC load")
    bot.add_cog(Lan(bot))


async def Category(ctx, name, teams=False):
    gameCategory = await ctx.guild.create_category(name)
    await ctx.guild.create_text_channel(f"General", category=gameCategory)
    await ctx.guild.create_voice_channel(f"General", category=gameCategory)
    if teams:
        for i in range(6):
            await ctx.guild.create_voice_channel(f"Equipe-{i + 1}", category=gameCategory)


class Lan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def startLan(self, ctx, number=15):
        if MyUtils(ctx.guild).G4check(ctx):
            await self.bot.change_presence(activity=discord.Game(name="Prepare la LAN"))
            # Categorie orga
            orga = await ctx.guild.create_category("Orga LAN")
            await ctx.guild.create_text_channel(f"General", category=orga)
            await ctx.guild.create_voice_channel(f"General", category=orga)
            await ctx.guild.create_voice_channel(f"Commentateurs / Streamer", category=orga)

            # Categorie pour le Viewers
            viewers = await ctx.guild.create_category("Viewers")
            await ctx.guild.create_text_channel(f"Annonce", category=viewers)
            for i in range(5):
                await ctx.guild.create_voice_channel(f"lobby-{i + 1}", category=viewers)

            # Cetegorie pour les joueurs
            group = await asyncio.gather(
                    # LoL
                    Category(ctx, "League of Legends", teams=True),

                    # Rocket League
                    Category(ctx, "Rocket League", teams=True),

                    # CSGO
                    Category(ctx, "CS:GO", teams=True),

                    # Minecraft
                    Category(ctx, "Minecraft"),

                    # AoE2
                    Category(ctx, "AOE2")
                )

            loop = asyncio.get_event_loop()
            loop.run_until_complete(group)
            loop.close()

        else:
            raise discord.ext.commands.CheckFailure

    @commands.command()
    async def stopLan(self, ctx):
        utils = MyUtils(ctx.guild)

        async def deleteCategory(cat):
            for channels in cat.channels:
                await channels.delete()
            await cat.delete()

        if MyUtils(ctx.guild).G4check(ctx):
            await self.bot.change_presence(activity=discord.Game(name="Désinstalle la LAN"))
            games = ["Orga LAN", "Viewers", "League of Legends", "Rocket League", "CS:GO", "Minecraft", "AOE2"]
            categories = [utils.getLanOneCategory(name) for name in games]
            group = asyncio.gather(*[deleteCategory(category)for category in categories])
            loop = asyncio.get_event_loop()
            loop.run_until_complete(group)
            loop.close()

        else:
            raise discord.ext.commands.CheckFailure
