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
                         description="",
                         )

sshEmbed.add_field(name="Quèsaco ?",
                   value="SSH = Secure Shell \n"
                         "C'est un protocole de communication sécurisé qui permet d'avoir un shell sur une machine "
                         "distante. Des clés de chiffrement sont échanger en début de connexion. \n"
                         "Le SSH à été créé pour remplacer des protocoles non sécurisé comme "
                         "[telnet](https://fr.wikipedia.org/wiki/Telnet) \n \n"
                         "Pour plus d'info, va sur [wikipedia](https://fr.wikipedia.org/wiki/Secure_Shell)",
                   inline=False
                   )

sshEmbed.add_field(name="Commande",
                   value="C'est pas très compliqué, la commande à taper dans ton "
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
                         "Son interet est de simuler une connexion locale entre deux machines afin d'acceder "
                         "aux services, resources distantes. \n \n"
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
                         "https://github.com/TCastus/TChelp/blob/master/guides/2-VPN.md) ",
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
                         "C'est un protocol qui permet de se connecter à un ordinateurs / serveurs à distance avec "
                         "un environement graphique. \n \n"
                         "Plus d'info sur [wikipedia](https://fr.wikipedia.org/wiki/Remote_Desktop_Protocol)",
                   inline=False
                   )

rdpEmbed.add_field(name="Commande",
                   value="{description de la commande}",
                   inline=False
                   )

rdpEmbed.add_field(name="Tuto",
                   value="[Lien vers un tuto du repo TChelp]("
                         "https://github.com/TCastus/TChelp/blob/master/guides/4-ConnexionDistanceBureauVirtuel.md)",
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
                value="C'est une interface sans éléments graphique qui permet d'interagir avec la machine."
                      "L'interaction ce fait à l'aide de ligne de commande pour executer different logiciels, "
                      "parcouris des dossiers... \n \n"
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
                      "https://github.com/TCastus/TChelp/blob/master/guides/1-Terminal.md)",
                inline=False
                )
