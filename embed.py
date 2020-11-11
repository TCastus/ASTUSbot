import discord
import main

PREFIX = main.PREFIX

###############
# Help        #
###############

helpEmbed = discord.Embed(title="Help",
                          color=0x2e86c1,
                          description="Message d'aide pour l'utilisation du bot de l'ASTUS")

helpEmbed.add_field(name=PREFIX + "help [sujet]",
                    value="Affiche ce message \n "
                          "Les sujets peuvent être divers, en voici une liste : \n"
                          " - SSH \n"
                          " - RDP \n"
                          " - VPN \n"
                          " - terminal \n"
                          " - git ou GitHub \n",
                    inline=False
                    )

helpEmbed.add_field(name=PREFIX + "futur ``alias : metier``",
                    value="Donne un lien vers un playlist youtube de vidéos faites par des diplômés"
                          "expliquant leurs parcours",
                    inline=False)

helpEmbed.add_field(name=PREFIX + "invitation ``alias : lien``",
                    value="Cette commande te permet d'obtenir le lien du serveur",
                    inline=False)

helpEmbed.add_field(name=PREFIX + "ipinfo [IPv4 ou IPv6]``alias : ipi``",
                    value="Permet d'obtenir des infos sur une adress IPv4 ou IPv6",
                    inline=False)

helpEmbed.add_field(name=PREFIX + "dns_lookup [Domain] `alias : nslookup`",
                    value="Donne les champs DNS d'un domain",
                    inline=False)

helpEmbed.add_field(name=PREFIX + "soa_lookup [Domain]",
                    value="Donne les champs SOA d'un domain",
                    inline=False)

###############
# G4 Help     #
###############

g4helpEmbed = discord.Embed(title="Commande du G4",
                            color=0x2e86c1,
                            description="Tu fais parti du G4 et tu as de grandes responsabilités"
                            )

g4helpEmbed.add_field(name=PREFIX + "newyear ``alias : ny``",
                      value="Cette commande est à utiliser quand l'année débute, elle te permet de "
                            "passer les rôles des Futurs TC à 3TC, 3TC -> 4TC, etc.",
                      inline=False)

g4helpEmbed.add_field(name=PREFIX + "passation",
                      value="Ici, tu supprimes tous les rôles des membres de l'ASTUS."
                            "Tu crées un nouveau rôle pour l'ancien G4 afin qu'il soit toujours "
                            "en relation avec l'ASTUS et aider la nouvelle ASTUS au mieux \n"
                            "Tu seras ensuite invité à mentionner les nouveaux membres en fonction de leurs rôles, "
                            "à la fin n'oublie pas de taper ``end`` pour finir la passation",
                      inline=False)

g4helpEmbed.add_field(name=PREFIX + "help nog4help",
                      value="Affiche l'help standard",
                      inline=False)

g4helpEmbed.add_field(name="Vendredi Chill",
                      value="Pour plus d'info utilise la commande : ``" + PREFIX + "help vendredichill``",
                      inline=False)

#########################
# Help {Vendredi chill} #
#########################

helpVendrediChill = discord.Embed(title="Vendredi Chill",
                                  color=0xEE8700,
                                  description="Ce groupe de commande te permet de afficher / cacher une catégorie "
                                              "nomé ``🎉 Vendredi Chill🎉``. Elle contient 15 channels vocaux pour "
                                              "repartir tous le monde en petit groupe.",
                                  )

helpVendrediChill.add_field(name=PREFIX + "showChannel [number of lobby]",
                            value="Cette commande te permet d'afficher la categorie avec les 15 channels vocaux.",
                            inline=False
                            )

helpVendrediChill.add_field(name=PREFIX + "hideChannel",
                            value="Cette commande te permet de cacher la categorie avec les 15 channels vocaux.",
                            inline=False
                            )

helpVendrediChill.add_field(name=PREFIX + "shufle [number per channel]",
                            value="Cette commande te permet de repartir de manière aléatoire les personnes dans le"
                                  " channel vocal `General` dnas les lobby en petit groupe de 5.",
                            inline=False
                            )

##########################
# Help passation command #
##########################

helpPassationEmbed = discord.Embed(title=PREFIX + "passation",
                                   color=0x2874a6,
                                   description="Cette commande te permet d'effectuer la passation de l'astus."
                                               "tu supprimes tous les anciens membres de l'astus et je t'invite"
                                               "à mentionner les nouveaux membres. Tu crées un noueau rôle pour "
                                               "l'ancien G4 \n"
                                               "N'oublie pas de taper `end` à la fin",
                                   )

########################
# Help newyear command #
########################

helpNewyearEmbed = discord.Embed(title=PREFIX + "newyear",
                                 color=0x2874a6,
                                 description="Cette commande te permet de passer à l'année suivante. Tu fais "
                                             "passer les 3TC en 4TC etc.",
                                 )

###########################
# Help invitation command #
###########################

helpInvitationEmbed = discord.Embed(title=PREFIX + "invitation `alias : lien`",
                                    color=0x2874a6,
                                    description="Cette commande te permet d'obtenir le lien d'invitation du serveur",
                                    )

######################
# Help video command #
######################

helpvideoEmbed = discord.Embed(title=PREFIX + "video `alias : metier, futur`",
                               color=0x2874a6,
                               description="Cette commande te permet d'obtenir la playlist des videos faites "
                                           "par des diplômés'",
                               )

#######################
# Help ipinfo Command #
#######################

helpIpInfo = discord.Embed(title=PREFIX + "ipinfo [IPv4 ou IPv6] `alias : ipi`",
                           color=0x78a5f9,
                           description="Donne des infos sur une adresse IPv4 ou IPv6",
                           )

###############################
# Help helpDns_lookup Command #
###############################

helpDns_lookup = discord.Embed(title=PREFIX + "dns_lookup [Domain] `alias : nslookup`",
                               color=0x78a5f9,
                               description="Donne les champs DNS d'un domain",
                               )

###############################
# Help helpSoa_lookup Command #
###############################

helpSoa_lookup = discord.Embed(title=PREFIX + "soa_lookup [Domain]",
                               color=0x78a5f9,
                               description="Donne les champs SOA d'un domain",
                               )

###############
# Help SSH    #
###############

sshEmbed = discord.Embed(title="SSH",
                         color=0xEE8700,
                         description="",
                         )

sshEmbed.add_field(name="Quèsaco ?",
                   value="SSH = Secure Shell \n"
                         "C'est un protocole de communication sécurisé qui permet d'avoir un shell sur une machine "
                         "distante. Des clés de chiffrement sont échangées en début de connexion. \n"
                         "Le SSH à été créé pour remplacer des protocoles non sécurisé comme "
                         "[telnet](https://fr.wikipedia.org/wiki/Telnet) \n \n"
                         "Pour plus d'info, va sur [wikipedia](https://fr.wikipedia.org/wiki/Secure_Shell)",
                   inline=False
                   )

sshEmbed.add_field(name="Commande",
                   value="Ce n'est pas très compliqué, la commande à taper dans ton "
                         "terminal est la même indépendamment des OS (Unix, OSX, "
                         "Windows) \n "
                         "Tu peux même utiliser le ssh sur "
                         "[Android](https://play.google.com/store/apps/details?id"
                         "=com.server.auditor.ssh.client&hl=fr) "
                         "et [IOS](https://apps.apple.com/us/app/termius-ssh"
                         "-client/id549039908), "
                         "notament avec Terminus \n \n"
                         "``ssh [username]@[machine]``",
                   inline=False
                   )

sshEmbed.add_field(name="Tuto",
                   value="[Lien vers un tuto du repo TChelp]("
                         "https://tcastus.github.io/TChelp/Travailler_a_distance/3-ConnexionDistanteSSH.html)",
                   inline=False
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

###############
# Help VPN    #
###############

vpnEmbed = discord.Embed(title="VPN",
                         color=0x2ecc71,
                         description="",
                         )

vpnEmbed.add_field(name="Quèsaco ?",
                   value="VPN = Virtual Private Network (Réseau virtuel privé) \n"
                         "Un VPN est un lien direct entre deux ou plusieurs ordinateurs / serveurs distants.\n"
                         "Son intérêt est de simuler une connexion locale entre deux machines afin d'accéder "
                         "aux services, ressources distantes. \n \n"
                         "Pour plus d'info, "
                         "[wikipedia](https://fr.wikipedia.org/wiki/R%C3%A9seau_priv%C3%A9_virtuel) "
                         "est ton ami :wink:",
                   inline=False
                   )

vpnEmbed.add_field(name="Commande",
                   value="{description de la commande}",
                   inline=False
                   )

vpnEmbed.add_field(name="Tuto",
                   value="[Lien vers un tuto du repo TChelp]("
                         "https://tcastus.github.io/TChelp/Travailler_a_distance/2-VPN.html) ",
                   inline=False
                   )

###############
# Help RDP #
###############

rdpEmbed = discord.Embed(title="RDP",
                         color=0xe74c3c,
                         description="",
                         )

rdpEmbed.add_field(name="Quèsaco ?",
                   value="RDP = Remote Desktop Protocol \n"
                         "C'est un protocol qui permet de se connecter à un ordinateur / serveur à distance avec "
                         "un environnement graphique. \n \n"
                         "Plus d'info sur [wikipedia](https://fr.wikipedia.org/wiki/Remote_Desktop_Protocol)",
                   inline=False
                   )

rdpEmbed.add_field(name="Commande",
                   value="{description de la commande}",
                   inline=False
                   )

rdpEmbed.add_field(name="Tuto",
                   value="[Lien vers un tuto du repo TChelp]("
                         "https://tcastus.github.io/TChelp/Travailler_a_distance/"
                         "4-ConnexionDistanceBureauVirtuel.html)",
                   inline=False
                   )

#################
# Help Terminal #
#################

terminalEmbed = discord.Embed(title="Terminal",
                              color=0xd68910,
                              description="",
                              )

terminalEmbed.add_field(name="Quèsaco ?",
                        value="C'est une interface sans élément graphique qui permet d'interagir avec la machine."
                              "L'interaction se fait à l'aide de ligne de commande pour éxécuter differents logiciels, "
                              "parcourir des dossiers... \n \n"
                              "Pour plus d'info, un tour sur "
                              "[wikipedia](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande)",
                        inline=False
                        )

terminalEmbed.add_field(name="Commande",
                        value="{description de la commande}",
                        inline=False
                        )

terminalEmbed.add_field(name="Tuto",
                        value="[Lien vers un tuto du repo TChelp]("
                              "https://tcastus.github.io/TChelp/Travailler_a_distance/1-Terminal.html)",
                        inline=False
                        )

# Calendar embed
helpCalendar = discord.Embed(title="Calendar 📅",
                             color=0xd68910,
                             description="",
                             )

helpCalendar.add_field(name="command",
                       value=f"affiche l'emploi du temps de la journée. pour utiliser ecrivez {PREFIX}cal suivi du"
                             f"nom de votre groupe "
                             f"par exemple `{PREFIX}cal 4TC2`",
                       inline=False
                       )

helpCalendar.add_field(name="command",
                       value=f"pour avoir votre emploi du temps de demain, vous pouvez utilise la cmd demain ,"
                             f"dem tomorrow , tom "
                             f"puis suivi de du nom de votre groupe"
                             f"example `{PREFIX}tomorrow 4TC2`",
                       inline=False
                       )
