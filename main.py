import discord
from discord.ext import commands
import os

from myutils import MyUtils

TOKEN = os.getenv("BOT_TOKEN")
PREFIX = "&"

bot = commands.Bot(command_prefix=PREFIX, description="Bot de l'ASTUS")


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.event
async def on_message(message):
    if not message.author.bot:

        if message.content.lower() == "ping":
            await message.channel.send("pong")

        if message.content.lower().replace(" ", "") in ["astusbot", "botastus",]:
            await message.channel.send("Le bot de l'astus pour te servir, tu as besoin de savoir ce que tu peux "
                                       "me demander ? tape ``" + PREFIX + "help `` pour avoir une liste de ce que"
                                       "je sais faire. \n Sinon ``" + PREFIX + "help [sujet]`` te permet"
                                       "d'avoir de l'aide sur un sujet en particulier :wink:")

    await bot.process_commands(message)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Mmmmmmh, j'ai bien l'impression que cette commande n'existe pas :/")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Il manque un argument.")
    if isinstance(error, commands.CheckFailure) or isinstance(error, commands.MissingPermissions):
        await ctx.send("Oups tu ne peux pas utiliser cette commande.")
    if isinstance(error, discord.Forbidden):
        await ctx.send("Oups, je n'ai pas les permissions nécessaires pour faire cette commmande")


@bot.event
async def on_raw_reaction_add(payload):
    messageID = payload.message_id
    if messageID == 726611125252128768:
        guildID = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guildID, bot.guilds)

        if payload.emoji.name == '3️⃣':
            # print("3TC")
            await payload.member.add_roles(MyUtils(guild).get3TCRole(),
                                           MyUtils(guild).getStudentRole())

        elif payload.emoji.name == '4️⃣':
            # print("4TC")
            await payload.member.add_roles(MyUtils(guild).get4TCRole(),
                                           MyUtils(guild).getStudentRole())

        elif payload.emoji.name == '5️⃣':
            # print("5TC")
            await payload.member.add_roles(MyUtils(guild).get5TCRole(),
                                           MyUtils(guild).getStudentRole())
        elif payload.emoji.name == '🇦':
            # print("TCA")
            await payload.member.add_roles(MyUtils(guild).getTCARole())

        elif payload.emoji.name == '👨‍🏫':
            # print("Prof")
            await payload.member.add_roles(MyUtils(guild).getProfRole())

        elif payload.emoji.name == '🎓':
            # print("Diplomes")
            await payload.member.add_roles(MyUtils(guild).getDiplomesRole())

        elif payload.emoji.name == '🆕':
            # print("Futur TC")
            await payload.member.add_roles(MyUtils(guild).getFuturTCRole())


@bot.event
async def on_member_update(before, after):
    if len(before.roles) < len(after.roles):
        new_role = next(role for role in after.roles if role not in before.roles)
        chan = await after.create_dm()
        if new_role.name == "3 TC":
            await chan.send("Salut, tu as le rôle 3TC sur le serveur de l'astus, ce rôle te permet de voir la"
                            "catégorie 3TC et de discuter avec tes camarades")

        if new_role.name == "4 TC":
            await chan.send("Salut, tu as le rôle 4TC sur le serveur de l'astus, ce rôle te permet de voir la"
                            "catégorie 4TC et de discuter avec tes camarades")

        if new_role.name == "5 TC":
            await chan.send("Salut, tu as le rôle 5TC sur le serveur de l'astus, ce rôle te permet de voir la"
                            "catégorie 5TC et de discuter avec tes camarades")

        if new_role.name == "Futur TC":
            await chan.send("Salut, et bienvenue à toi Futur TC. Tu as accès à la categorie Integration du serveur :wave: \n\n "
                            "Le bureau de l'Astus est prêt à t'accueillir et à te faire passer une intégration que tu n'oublieras pas , crois nous ! ( tout dans le respect des gestes barrières :man_pouting:  :left_right_arrow: :deaf_person:  , le gel hydroalcoolique sera notre meilleur ami ). \n"
                            " :arrow_forward: Point intégration : La rentrée est initialement prévue le 14 septembre 2020, mais une rumeur de Covid complique les choses. Donc pour le moment on se base dessus, et on prévoie de vous organiser une inté à partir du  jeudi 10 au soir. \n"
                            " :arrow_forward: Si ce n'est pas déjà le cas, on t'invite à rejoindre le groupe Facebook de la promo, où des informations tourneront aussi par rapport aux activités en journée www.facebook.com/groups/tc2023/ \n "
                            " :arrow_forward: Questions réponses : Ce chanel est dédié à répondre à toutes vos questions sur l'intégration, que ce soit d'un point de vue logistique ou même sur l'organisation globale de celle- ci. N'hésite pas, nous serons nombreux à pouvoir te répondre ! \n")

        if new_role.name == "Student":
            await chan.send(" :wave: Bienvenue sur le serveur de l'ASTUS, tu trouveras plusieurs categories sur le "
                            "serveur. \n \n"
                            " `` Général``  ici des annonces de l'ASTUS seront faites. Vous pouvez voir un channel \n"
                            " ``gestion-music`` qui permet d'utiliser l'enceinte de l'ASTUS \n"
                            " `` Que deviens- tu ? `` Tu as envie de parler de ton expérience à l'issu de ton parcours TC? Des conseils à donner aux futurs diplômés?  Cet espace est fait pour toi !  :man_technologist: \n"
                            "Au contraire, tu es un étudiant concerné par ce que deviennent les anciens diplômés, c'est aussi ici que tu peux t'exprimer ! \n"
                            " `` Section Astus `` ( Accès attribués aux étudiants ): "
                            "Alors là, vous faites ce que vous voulez, quand vous voulez. Le chanel modélise le local de l'asso, donc on modère uniquement en cas de propos haineux, racistes, ou toute la liste qui suit. C'est votre espace détente donc lâchez vous, ça compte aussi pour les futurs 3TC ! \n"
                            " `` Section intégration `` Informations : Salut à toi futur TC ! :wave: \n"
                            " Le bureau de l'Astus est prêt à t'accueillir et à te faire passer une intégration que tu n'oublieras pas , crois nous ! ( tout dans le respect des gestes barrières :man_pouting:  :left_right_arrow: :deaf_person:  , le gel hydroalcoolique sera notre meilleur ami ). \n "
                            " :arrow_forward:  Point intégration : La rentrée est initialement prévue le 14 septembre 2020, mais une rumeur de Covid complique les choses. Donc pour le moment on se base dessus, et on prévoie de vous organiser une inté à partir du  jeudi 10 au soir. \n"
                            " :arrow_forward:  Si ce n'est pas déjà le cas, on t'invite à rejoindre le groupe Facebook de la promo, où des informations tourneront aussi par rapport aux activités en journée www.facebook.com/groups/tc2023/  \n "
                            " :arrow_forward:  Questions réponses : Bienvenue ! Ce chanel est dédié à répondre à toutes vos questions sur l'intégration, que ce soit d'un point de vue logistique ou même sur l'organisation globale de celle- ci. N'hésite pas, nous serons nombreux à pouvoir te répondre ! \n"
"
                            )

        if new_role.name in ["Prof", "Diplômés"]:
            await chan.send("Madame, Monsieur, \n"
                            "Bienvenue sur le serveur de l'ASTUS, vous trouverez plusieurs categories sur le "
                            "serveur. :speaking_head: \n \n"
                            " :arrow_forward: ``Général`` ici des annonces de l'ASTUS seront faites. "
                            " :arrow_forward: ``gestion-music`` qui permet d'utiliser l'enceinte de l'ASTUS \n"
                            " :arrow_forward: ``Un Boulot / Stage`` , permet de mettre en relation des dipômés avec les TC actuels "
                            "afin de trouver un stage ou un emploi pour les 5TC qui vont avoir leur diplôme \n"
                            " :arrow_forward: Garder le contact, permet de discuter avec des diplômés de leur parcours\n "
                            )

        if new_role.name == "Admin Groupe de Travail":
            await chan.send("Tu es un admin des groupes de travail mis en place par l'ASTUS, tu peux créer, "
                            "supprimer des channels dans la categorie groupe de travail afin de les animer "
                            "au mieux. May the force be with you ! :man_technologist:  "
                            )

        if new_role.name == "ASTUS":
            await chan.send("Bienvenue à l'ASTUS ! \n"
                            "Tout d'abord, félicitation à toi pour avoir intégré l'ASTUS :wink: \n"
                            "Tu as maintenant accés à la categorie ASTUS, tu retrouveras un channel général pour"
                            "parler avec tous tes p'tits potes de l'ASTUS. Il y a aussi channel passation pour parler avec"
                            "l'ancien G4 de la gestion de l'ASTUS quand la fameuse heure viendra. En fonction de ton rôle, tu ne vois pas certains"
                            "channel, je t'explique tout cela rapidement :wink:")

        if new_role.name == "G4":
            await chan.send("Un grand pouvoir inplique de grandes responsabilités. C'est grâce à toi que l'astus "
                            "peut tourner. Tu as accès à quelques commandes de gestion du serveur (plus d'info "
                            "avec ``" + PREFIX + "help`` sur le serveur")

        if new_role.name == "Team Event":
            await chan.send("C'est toi qui va nous régaler avec tout pleins d'Event. Un channel dans la catégorie "
                            "ASTUS t'es réservé")

        if new_role.name == "Resp Team Event":
            await chan.send("Tu gères la Team Event, pour cela tu as accès à un channel dédié avec ta team")

        if new_role.name == "Team Entreprise":
            await chan.send("C'est toi qui va nous régaler avec tout pleins de rencontre avec des entreprises."
                            "Un channel dans la catégorie ASTUS t'es réservé")

        if new_role.name == "Resp Team Entreprise":
            await chan.send("Tu gères la Team Entreprise, pour cela tu as accès à un channel dédié avec ta team")

        if new_role.name == "Resp Site International":
            await chan.send("Resp du site ! \n"
                            "C'est grâce à toi que le site peut évoluer, demande à ce qu'on t'ajoute au"
                            "repo GitHub :wink:")

        if new_role.name == "Resp Comm":
            await chan.send("Resp comm ! \n"
                            "L'ASTUS compte sur toi pour un max de communication. Tu géres la page FB de l'astus."
                            "Tu fais les annonces et les affiches pour tous les events ")

if __name__ == '__main__':
    import cogs.newyear
    import cogs.passation
    import cogs.help
    import cogs.videoDiplomes
    import cogs.invitation

    # Remove default help command
    bot.remove_command("help")

    # cogs
    bot.add_cog(cogs.passation.CogPassation(bot, PREFIX))
    bot.add_cog(cogs.newyear.CogNewyear(bot))
    bot.add_cog(cogs.help.CogHelp(bot))
    bot.add_cog(cogs.videoDiplomes.CogVideoDiplomes(bot))
    bot.add_cog(cogs.invitation.CogInvitation(bot))

    bot.run(TOKEN)