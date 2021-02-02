import discord
from discord.ext import commands
from myutils import MyUtils


def setup(bot):
    print("LAN TC load")
    bot.add_cog(Lan(bot))


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
            # LoL
            lol = await ctx.guild.create_category("League of Legends")
            await ctx.guild.create_text_channel(f"General", category=lol)
            await ctx.guild.create_voice_channel(f"General", category=lol)
            for i in range(6):
                await ctx.guild.create_voice_channel(f"Equipe-{i + 1}", category=lol)

            # Rocket League
            rl = await ctx.guild.create_category("Rocket League")
            await ctx.guild.create_text_channel(f"General", category=rl)
            await ctx.guild.create_voice_channel(f"General", category=rl)
            for i in range(6):
                await ctx.guild.create_voice_channel(f"Equipe-{i + 1}", category=rl)

            # CSGO
            csgo = await ctx.guild.create_category("CS:GO")
            await ctx.guild.create_text_channel(f"General", category=csgo)
            await ctx.guild.create_voice_channel(f"General", category=csgo)
            for i in range(6):
                await ctx.guild.create_voice_channel(f"Equipe-{i + 1}", category=csgo)

            # Minecraft
            minecraft = await ctx.guild.create_category("Minecraft")
            await ctx.guild.create_text_channel(f"General", category=minecraft)
            await ctx.guild.create_voice_channel(f"General", category=minecraft)

            # AoE2
            aoe2 = await ctx.guild.create_category("AOE2")
            await ctx.guild.create_text_channel(f"General", category=aoe2)
            await ctx.guild.create_voice_channel(f"General", category=aoe2)

        else:
            raise discord.ext.commands.CheckFailure

    @commands.command()
    async def stopLan(self, ctx):
        utils = MyUtils(ctx.guild)
        if MyUtils(ctx.guild).G4check(ctx):
            await self.bot.change_presence(activity=discord.Game(name="Désinstalle la LAN"))
            categories = [
                          utils.getLanOrgaCategory(),
                          utils.getViewersCategory(),
                          utils.getLOLCategory(),
                          utils.getRlCategory(),
                          utils.getCsgoCategory(),
                          utils.getMinecraftCategory(),
                          utils.getAoE2Category()
                          ]
            for category in categories:
                for channels in category.channels:
                    await channels.delete()
                await category.delete()
        else:
            raise discord.ext.commands.CheckFailure