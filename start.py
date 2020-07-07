import discord
import os
import datetime

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
        astus = discord.utils.get(message.guild.roles, name="ASTUS")
        teamEvent = discord.utils.get(message.guild.roles, name="Team Event")
        respTeamEvent = discord.utils.get(message.guild.roles, name="Resp Team Event")
        teamEts = discord.utils.get(message.guild.roles, name="Team Entreprise")
        respTeamEts = discord.utils.get(message.guild.roles, name="Resp Team Entreprise")
        respSite = discord.utils.get(message.guild.roles, name="Resp Site International")
        ancienRespSite = discord.utils.get(message.guild.roles, name="Ancien Resp Site International")
        respComm = discord.utils.get(message.guild.roles, name="Resp Comm")

        if message.content == "ping":
            await message.channel.send("pong")

        if message.content[0] == PREFIX and g4 in message.author.roles:
            if message.content[1:] == "newyear":

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

            elif message.content[1:] == "passation" and g4 in message.author.roles:

                # Creation du role
                newG4 = await message.guild.create_role(
                    name=f"G4 {datetime.datetime.now().year - 1}-{datetime.datetime.now().year}",
                    permissions=discord.Permissions(1333259863),
                    colour=discord.Colour(2123412)
                )

                # recherche des channel
                g4Txt = discord.utils.get(message.guild.channels, id=726554977753104464)
                g4Vocal = discord.utils.get(message.guild.channels, id=726555448739758151)

                # permissions
                g4TxtPerms = discord.PermissionOverwrite(
                    create_instant_invite=False,
                    read_messages=True,
                    send_messages=True,
                    manage_channels=True,
                    add_reactions=True,
                    send_tts_messages=False,
                    manage_messages=True,
                    embed_links=True,
                    attach_files=True,
                    read_message_history=True,
                    mention_everyone=True,
                    external_emojis=True,
                    manage_roles=False,
                    manage_webhooks=False
                )

                g4VocalPerms = discord.PermissionOverwrite(
                    create_instant_invite=False,
                    manage_roles=False,
                    manage_webhooks=False,
                    manage_channels=True,
                    priority_speaker=False,
                    stream=True,
                    view_channel=True,
                    connect=True,
                    speak=True,
                    mute_members=True,
                    use_voice_activation=True
                )
                g4VocalPerms.stream = True

                # attribution des roles aux channels
                await g4Txt.set_permissions(newG4, overwrite=g4TxtPerms)
                await g4Vocal.set_permissions(newG4, overwrite=g4VocalPerms)

                for member in message.guild.members:
                    if g4 in member.roles:
                        await member.remove_roles(g4)
                        await member.add_roles(newG4)
                    if astus in member.roles:
                        await member.remove_roles(astus)
                    if respComm in member.roles:
                        await member.remove_roles(respComm)
                    if respSite in member.roles:
                        await member.remove_roles(respSite)
                    if respTeamEts in member.roles:
                        await member.remove_roles(respTeamEts)
                    if respTeamEvent in member.roles:
                        await member.remove_roles(respTeamEvent)
                    if ancienRespSite in member.roles:
                        await member.remove_roles(ancienRespSite)
                    if teamEvent in member.roles:
                        await member.remove_roles(teamEvent)
                    if teamEts in member.roles:
                        await member.remove_roles(teamEts)

                await message.channel.send("Passation faite")

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
