import discord
from discord.ext import commands
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json


def setup(bot):
    print("TGG load")
    bot.add_cog(CogTGG(bot))


class CogTGG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/spreadsheets',
                 'https://www.googleapis.com/auth/drive'
                 ]

        service_account_info = json.loads(os.getenv('GOOGLE_APPLICATION_CREDENTIALS_JSON', '{}'))
        creds = ServiceAccountCredentials.from_json_keyfile_dict(service_account_info, scope)
        client = gspread.authorize(creds)

        self.sheet = client.open("ASTUSbotTGG_Database").sheet1

    @commands.command(aliases=["tgg", "thomas", "ginny"])
    async def thomasGeorgeGeorge(self, ctx):
        await self.bot.change_presence(activity=discord.Game(name="Cite TGG 💪"))
        randomQuote = random.choice(self.sheet.col_values(1))
        randomPhoto = random.choice(self.sheet.col_values(2))
        Embed = discord.Embed(title="",
                              color=int(hex(random.randint(0, 16777215)), 16),
                              description="",
                              )
        Embed.set_image(url=randomPhoto)
        Embed.set_author(name="Thommas Georges Georges",
                         url="https://www.facebook.com/thomas.georges292",
                         icon_url="https://scontent-cdt1-1.xx.fbcdn.net/v/t1.0-9/118765992_2628383697424846_1304447"
                                  "826277117113_n.jpg?_nc_cat=106&ccb=2&_nc_sid=09cbfe&_nc_ohc=paR3XPGAbkAAX8z428c&_nc"
                                  "_ht=scontent-cdt1-1.xx&oh=65a4ad0a9234daf45247ca7d8139703c&oe=5FD1186B",
                         )
        Embed.set_footer(text=randomQuote)
        await ctx.send(embed=Embed)
