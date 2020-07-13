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
videoDiplomesEmbed.add_field(name="Assia MERMOURI - promo TC2017",
                             value="[Ingénieur réseau et sécurité chez SFR]("
                                   "https://www.youtube.com/watch?v=lQEbnvmJ9uw&list=PL"
                                   "-wHxgCMty1Zn6IOc65cSudv_ZqdteTKx&index=2&t=0s) \n"
                                   "[Profile LinkedIn](https://www.linkedin.com/in/assiamermouri/)",
                             inline=False
                             )

videoDiplomesEmbed.add_field(name="Mamoun DRISSI KACEMI - promo TC2016",
                             value="[Solutions Architect chez Dropbox]("
                                   "https://www.youtube.com/watch?v=GjBI-ldy2hk&list=PL"
                                   "-wHxgCMty1Zn6IOc65cSudv_ZqdteTKx&index=3&t=0s) \n"
                                   "[Profile LinkedIn](https://www.linkedin.com/in/mamoun-drissi-kacemi-6a84a241/)",
                             inline=False
                             )

videoDiplomesEmbed.add_field(name="Hilda EDIMO - promo TC2017",
                             value="[Ingénieure avant-vente chez VMWare]("
                                   "https://www.youtube.com/watch?v=AWnMfzzkm9M&list=PL"
                                   "-wHxgCMty1Zn6IOc65cSudv_ZqdteTKx&index=4&t=0s) \n"
                                   "[Profile LinkedIn](https://www.linkedin.com/in/hilda-edimo-925ab5b0/)",
                             inline=False
                             )

videoDiplomesEmbed.add_field(name="Tianni LI - promo TC2016",
                             value="[Ingénieur qualité chez Dataiku]("
                                   "https://www.youtube.com/watch?v=cQYjcijMrPI&list=PL"
                                   "-wHxgCMty1Zn6IOc65cSudv_ZqdteTKx&index=5&t=0s) \n"
                                   "[Profile LinkedIn](https://www.linkedin.com/in/tianni-li-324504a4/)",
                             inline=False
                             )

videoDiplomesEmbed.add_field(name="Julien BONVALOT - promo TC2005",
                             value="[Manager RF Optimisation chez Network Solutions Factory]("
                                   "https://www.youtube.com/watch?v=D9veUkDoQF4&list=PL"
                                   "-wHxgCMty1Zn6IOc65cSudv_ZqdteTKx&index=6&t=0s) \n"
                                   "[Profile LinkedIn](https://www.linkedin.com/in/julien-bonvalot-b80b26b/)",
                             inline=False
                             )

videoDiplomesEmbed.add_field(name="Samia Bouchareb - Promo TC2015",
                             value="[DevOps Team Manager chez Orange business services]("
                                   "https://www.youtube.com/watch?v=VIzlzUZ6nbM&list=PL"
                                   "-wHxgCMty1Zn6IOc65cSudv_ZqdteTKx&index=7&t=0s) \n"
                                   "[Profile LinkedIn](https://www.linkedin.com/in/samia-bouchareb/)",
                             inline=False
                             )

videoDiplomesEmbed.add_field(name="Guilhem TESSEYRE - Promo TC2008",
                             value="[Head of Customer Engineering for Digital Natives @ Google Cloud]("
                                   "https://www.youtube.com/watch?v=R1Vj_uQhLiE&list=PL"
                                   "-wHxgCMty1Zn6IOc65cSudv_ZqdteTKx&index=8&t=0s) ",
                             inline=False
                             )

videoDiplomesEmbed.add_field(name="Andra DRAGOMIR -promo TC2014",
                             value="[Head of technical development chez NTT]("
                                   "https://www.youtube.com/watch?v=0RSbsSyngJ0&list=PL"
                                   "-wHxgCMty1Zn6IOc65cSudv_ZqdteTKx&index=9&t=0s) \n"
                                   "[Profile LinkedIn](https://www.linkedin.com/in/andraehlert/)",
                             inline=False
                             )

videoDiplomesEmbed.add_field(name="Tommy GAIDDON - promo TC2017",
                             value="[Consultant IT chez Solutec]("
                                   "https://www.youtube.com/watch?v=ZI1JEwSE52s&list=PL"
                                   "-wHxgCMty1Zn6IOc65cSudv_ZqdteTKx&index=10&t=0s) ",
                             inline=False
                             )

videoDiplomesEmbed.add_field(name="Guillaume ZEKIAN - promo TC2006",
                             value="[Head of Network, Security and Datacenters for Switzerland - Société Générale]("
                                   "https://www.youtube.com/watch?v=I7MsXhcsQg8&list=PL"
                                   "-wHxgCMty1Zn6IOc65cSudv_ZqdteTKx&index=11&t=0s) ",
                             inline=False
                             )

videoDiplomesEmbed.add_field(name="Florence MICOL - promo TC2006",
                             value="[CH Salesforce business group lead chez Accenture]("
                                   "https://www.youtube.com/watch?v=4Q8OyWCX5KY&list=PL"
                                   "-wHxgCMty1Zn6IOc65cSudv_ZqdteTKx&index=12&t=0s) ",
                             inline=False
                             )
