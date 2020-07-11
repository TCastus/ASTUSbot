import discord
import os
import datetime
import embed
import perms

TOKEN = os.getenv("BOT_TOKEN")
client = discord.Client()

PREFIX = "&"

if __name__ == '__main__':

    async def addRole(payload, guild, rolename):
        role = discord.utils.get(guild.roles, name=rolename)
        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
        await member.add_roles(role)


    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
        channel = client.get_channel(726554620377169950)
        msg = await channel.fetch_message(726611125252128768)
        await msg.edit(content="Bonjour à toi, \n \n"
                               "Bienvenue sur le serveur de l'ASTUS, endroit d'échange pour tous les TC. Nous "
                               "comptons sur toi pour le plus grand respect de chacun et la bienveillance de tous \n"
                               "Nous retrouvons des profs, les TC actuels, les diplômés et les nouveaux \n \n"
                               "Des rôles sont mis en place pour identifier tout le monde. Tu peux choisir le tien en "
                               "cliquant sur la bonne réaction. :warning: Petite particularité pour les TCA, il faut "
                               "d'abord choisir TCA puis le niveau qui vous correspond, sinon tu n'auras pas le rôle "
                               "TCA :warning:\n \n"
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

            if message.content.lower() == "ping":
                await message.channel.send("pong")

            if message.content.lower().replace(" ", "") == "astusbot":
                await message.channel.send("Le bot de l'astus pour te servir, tu as besoin de savoir ce que tu peux "
                                           "me demander ? tape ``" + PREFIX + "help `` pour avoir une liste de ce que"
                                           "je sais faire. \n"
                                           "Sinon ``" + PREFIX + "help [SSH|RDP|...]`` te permet"
                                           "d'avoir de l'aide sur un sujet en particulier :wink:")

            if message.content[0] == PREFIX:
                if message.content[1:].lower() == "newyear" and g4 in message.author.roles:

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

                elif message.content[1:].lower() == "passation" and g4 in message.author.roles:

                    # Creation du role
                    newG4 = await message.guild.create_role(
                        name=f"G4 {datetime.datetime.now().year - 1}-{datetime.datetime.now().year}",
                        permissions=discord.Permissions(1333259863),
                        colour=discord.Colour(2123412)
                    )

                    # recherche des channel
                    g4Txt = discord.utils.get(message.guild.channels, id=726554977753104464)
                    g4Vocal = discord.utils.get(message.guild.channels, id=726555448739758151)

                    # attribution des roles aux channels
                    await g4Txt.set_permissions(newG4, overwrite=perms.g4TxtPerms)
                    await g4Vocal.set_permissions(newG4, overwrite=perms.g4VocalPerms)

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

                elif message.content[1:].lower() == "pasation" and g4 in message.author.roles:
                    await message.channel.send("Essaie plutot ``" + PREFIX + "passation``")

                elif message.content[1:].lower() == "new year" and g4 in message.author.roles:
                    await message.channel.send("Essaie plutot ``" + PREFIX + "newyear``")

                elif message.content.split(" ")[0].lower()[1:] == "help":
                    try:
                        subject = message.content.split(" ")[1].lower()
                    except IndexError:
                        subject = None

                    if g4 in message.author.roles and not subject:
                        await message.channel.send(embed=embed.g4helpEmbed)

                    else:
                        if subject == "ssh":
                            await message.channel.send(embed=embed.sshEmbed)

                        elif subject == "rdp":
                            await message.channel.send("Le RDP : \n"
                                                       "Voici de l'aide sur TChelp : \n"
                                                       "https://github.com/TCastus/TChelp/blob/master/guides/4"
                                                       "-ConnexionDistanceBureauVirtuel.md")

                        elif subject == "vpn":
                            await message.channel.send("Le vpn : \n"
                                                       "Voici de l'aide sur TChelp : \n"
                                                       "https://github.com/TCastus/TChelp/blob/master/guides/2-VPN.md")

                        elif subject == "terminal":
                            await message.channel.send("Le terminal : \n"
                                                       "Voici de l'aide sur TChelp : \n"
                                                       "https://github.com/TCastus/TChelp/blob/master/guides/1-Terminal.md")

                        elif subject in ["git", "github"]:
                            await message.channel.send("Git / GitHub : \n"
                                                       "Voici de l'aide sur TChelp : \n"
                                                       "https://github.com/TCastus/TChelp/blob/master/Git_GitHub"
                                                       "/Presentation.md")

                        elif subject == "tsa":
                            await message.channel.send("TSA... :sweat_smile: \n"
                                                       "Je suis vraiment désolé mais je suis dans l'incapacité de te "
                                                       "donner de l'aide sur ce sujet :no_mouth:")

                        elif not subject or g4 in message.author.roles and subject == "nog4help":
                            await message.channel.send(embed=embed.helpEmbed)
                        else:
                            await message.channel.send("Désolé, je ne sais pas te donner de l'aide sur ce sujet... \n "
                                                       "Peut-être que tu trouvera un réponse sur le repo "
                                                       "[TChelp](https://github.com/TCastus/TChelp) :wink: ")

                else:
                    await message.channel.send("Je ne commprend pas cette commande... \n"
                                               "Un `` " + PREFIX + "help `` peut t'aider")


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
                # await addRole(payload, guild, "Student")

    @client.event
    async def on_member_update(before, after):
        if len(before.roles) < len(after.roles):
            new_role = next(role for role in after.roles if role not in before.roles)
            chan = await after.create_dm()
            if new_role.name == "3 TC":
                await chan.send("Salut, tu as le rôle 3TC sur le serveur de l'astus, ce role te permet de voir la"
                                "catégorie 3TC et de discuter avec tes camarades")

            if new_role.name == "4 TC":
                await chan.send("Salut, tu as le rôle 4TC sur le serveur de l'astus, ce role te permet de voir la"
                                "catégorie 4TC et de discuter avec tes camarades")

            if new_role.name == "5 TC":
                await chan.send("Salut, tu as le rôle 5TC sur le serveur de l'astus, ce role te permet de voir la"
                                "catégorie 3TC et de discuter avec tes camarades")

            if new_role.name == "Futur TC":
                await chan.send("Salut, et bienvenue à toi Futur TC. Tu as acces à la categorie Integration du serveur."
                                "Elle te permet de discuter avec tes futurs camarades et avec les TC actuels")

            if new_role.name == "Student":
                await chan.send("Bienvenue sur le serveur de l'ASTUS, tu trouveras plusieurs categorie sur le "
                                "serveur. \n \n"
                                " - General, ici des annonces de l'ASTUS seront faites, vous pouvez voir un channel "
                                "``gestion-music`` qui permet d'utiliser l'enceinte de l'ASTUS \n"
                                " - Un Boulot / Satge, permet de mettre en relation des dipômés avec les TC actuels "
                                "afinde trouver un stage ou un emploi pour les 5TC qui vont avoir leur diplôme \n"
                                " - Garder le contact, permet de discuter avec des diplômés de leur parcour \n"
                                " - L'ASTUS, ici tu peux t'exprimer librement sans prof et faire toute l'humour que "
                                "tu veux \n"
                                " - Integration, soit respectueux avec les nouveaux et aide les a vivre au mieux sa "
                                "nouvelle vie au depart :wink:"
                                )

            if new_role.name in ["Prof", "Diplômés"]:
                await chan.send("Madame, Monsieur, \n"
                                "Bienvenue sur le serveur de l'ASTUS, vous trouverez plusieurs categorie sur le "
                                "serveur. \n \n"
                                " - General, ici des annonces de l'ASTUS seront faites, vous pouvez voir un channel "
                                "``gestion-music`` qui permet d'utiliser l'enceinte de l'ASTUS \n"
                                " - Un Boulot / Satge, permet de mettre en relation des dipômés avec les TC actuels "
                                "afinde trouver un stage ou un emploi pour les 5TC qui vont avoir leur diplôme \n"
                                " - Garder le contact, permet de discuter avec des diplômés de leur parcour"
                                )

            if new_role.name == "Admin Groupe de Travail":
                await chan.send("Tu es un admin des groupes de travail mis en place par l'ASTUS, tu peut creer, "
                                "supprimer des channels dans la categorie groupe de travail afin de les annimer "
                                "au mieux"
                                )


    client.run(TOKEN)
