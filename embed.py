import discord
import start

PREFIX = start.PREFIX

###############
# G4 Help     #
###############

g4helpEmbed = discord.Embed(title="Commande du G4",
                            color=0x2e86c1,
                            description="Tu fait parti du G4 et tu as de grande responsabilitées"
                            )

g4helpEmbed.add_field(name=PREFIX + "newyear",
                      value="Cette commande est à utiliser quand l'année debute, elle te permet de "
                            "passer les rôles des FuturTC à 3TC, 3TC -> 4TC, etc.",
                      inline=False)

g4helpEmbed.add_field(name=PREFIX + "passation",
                      value="Ici, tu supprimer tous les rôles des membres de l'ASTUS."
                            "Tu créé un nouveau rôle pour l'ancien G4 afin qu'il soit toujours "
                            "en relation avec l'ASTUS et aider la nouvelle ASTUS au mieux",
                      inline=False)

g4helpEmbed.add_field(name=PREFIX + "help nog4help",
                      value="Affiche l'help standard",
                      inline=False)


###############
# Help SSH    #
###############

sshEmbed = discord.Embed(title="SSH",
                         color=0xEE8700,
                         description="C'est pas très compliqué, la commande à taper dans ton "
                                     "terminal est la même indépendamment des OS (Unix, OSX, "
                                     "Windows) \n "
                                     "Tu peux même utiliser le ssh sur "
                                     "[Android](https://play.google.com/store/apps/details?id"
                                     "=com.server.auditor.ssh.client&hl=fr) "
                                     "et [IOS](https://apps.apple.com/us/app/termius-ssh"
                                     "-client/id549039908), "
                                     "notament avec Terminus",
                         )

sshEmbed.add_field(name="Command",
                   value="``ssh [username]@[machine]``",
                   inline=False
                   )

sshEmbed.add_field(name="Tuto",
                   value="[Lien vers un tuto du repo TChelp]("
                         "https://github.com/TCastus/TChelp/blob/master/guides/3"
                         "-ConnexionDistanteSSH.md) ",
                   inline=False
                   )

###############
# Help        #
###############

helpEmbed = discord.Embed(title="Help",
                          color=0x2e86c1,
                          description="Message d'aide pour l'utilisation du bot de l'ASTUS")

helpEmbed.add_field(name=PREFIX + "help [sujet]",
                    value="Affiche ce message \n "
                          "Les sujets peuvent être diverse, en voici une liste : \n"
                          " - SSH \n"
                          " - RDP \n"
                          " - VPN \n"
                          " - terminal \n"
                          " - git ou GitHub \n"
                    )

###########################
# playlist video diplomes #
###########################

videoDiplomesEmbed = discord.Embed(title="Playlist des vidéos faites pas les dipômés",
                                   color=0x5e3dc8,
                                   description="Tu trouveras sur cette playlist des vidéos faites pas les diplômes"
                                               "de TC afin d'expliquer leur parcours et leurs métiers",
                                   url="https://www.youtube.com/playlist?list=PL-wHxgCMty1Zn6IOc65cSudv_ZqdteTKx",
                                   )

videoDiplomesEmbed.set_thumbnail(url="https://img.icons8.com/fluent/48/000000/youtube-play.png")
