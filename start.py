import discord
import os
import time

TOKEN = os.getenv("BOT_TOKEN")
client = discord.Client()

PREFIX = "@"


async def addRole(payload, guild, rolename):
    role = discord.utils.get(guild.roles, name=rolename)
    member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
    await member.add_roles(role)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channel = client.get_channel(726554620377169950)
    msg = await channel.fetch_message(726611125252128768)
    await msg.edit(content="hello, les regles, blabla \n"
                           "Voici les rôles : \n"
                           ":man_teacher: : Prof \n"
                           ":mortar_board: : Diplômés \n"
                           ":three: : 3TC \n"
                           ":four: : 4TC \n"
                           ":five: : 5TC \n"
                           ":regional_indicator_a: : TCA \n"
                           ":new: : Futur TC"
                   )  # mettre le message des regles


@client.event
async def on_message(message):
    if not message.author.bot:

        student = discord.utils.get(message.guild.roles, name="Student")
        new3TC = discord.utils.get(message.guild.roles, name="Futur TC")
        troisTC = discord.utils.get(message.guild.roles, name="3 TC")
        quatreTC = discord.utils.get(message.guild.roles, name="4 TC")
        cinqTC = discord.utils.get(message.guild.roles, name="5 TC")
        diplomes = discord.utils.get(message.guild.roles, name="Diplômés")
        g4 = discord.utils.get(message.guild.roles, name="G4")

        if message.content == "ping":
            await message.channel.send("pong")

        if message.content == PREFIX + "newyear" and g4 in message.author.roles:

            for member in message.guild.members:
                if new3TC in member.roles:
                    await member.remove_roles(new3TC)
                    await member.add_roles(troisTC)
                elif troisTC in member.roles:
                    await member.remove_roles(troisTC)
                    await member.add_roles(quatreTC)
                elif quatreTC in member.roles:
                    await member.remove_roles(quatreTC)
                    await member.add_roles(cinqTC)
                elif cinqTC in member.roles:
                    await member.remove_roles(cinqTC, student)
                    await member.add_roles(diplomes)

            await message.channel.send("Changement des rôles :) : \n "
                                       " - les Futur sont maintenant des 3TC \n"
                                       " - les 3TC sont maintenant des 4TC \n"
                                       " - les 4TC sont maintenant des 5TC \n"
                                       " - les 5TC sont maintenant des Diplômés \n"
                                       )

        else:
            await message.channel.send("Tu n'as pas le droit d'exécuter cette commande")



@client.event
async def on_raw_reaction_add(payload):
    messageID = payload.message_id
    if messageID == 726611125252128768:
        guildID = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guildID, client.guilds)

        if payload.emoji.name == '3️⃣':
            # print("3TC")
            await addRole(payload, guild, "3 TC")
            await addRole(payload, guild, "Student")
        elif payload.emoji.name == '4️⃣':
            # print("4TC")
            await addRole(payload, guild, "4 TC")
            await addRole(payload, guild, "Student")
        elif payload.emoji.name == '5️⃣':
            # print("5TC")
            await addRole(payload, guild, "5 TC")
            await addRole(payload, guild, "Student")
        elif payload.emoji.name == '🇦':
            # print("TCA")
            await addRole(payload, guild, "TCA")
        elif payload.emoji.name == '👨‍🏫':
            # print("Prof")
            await addRole(payload, guild, "Prof")
        elif payload.emoji.name == '🎓':
            # print("Diplomes")
            await addRole(payload, guild, "Diplômés")
        elif payload.emoji.name == '🆕':
            # print("Futur TC")
            await addRole(payload, guild, "Futur TC")
            await addRole(payload, guild, "Student")


client.run(TOKEN)
