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
        await ctx.send("Oups, je n'ai pas les permissions nécéssaires pour faire cette commmande")


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
            await chan.send("Salut, tu as le rôle 3TC sur le serveur de l'astus, ce role te permet de voir la"
                            "catégorie 3TC et de discuter avec tes camarades")

        if new_role.name == "4 TC":
            await chan.send("Salut, tu as le rôle 4TC sur le serveur de l'astus, ce role te permet de voir la"
                            "catégorie 4TC et de discuter avec tes camarades")

        if new_role.name == "5 TC":
            await chan.send("Salut, tu as le rôle 5TC sur le serveur de l'astus, ce role te permet de voir la"
                            "catégorie 5TC et de discuter avec tes camarades")

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

        if new_role.name == "ASTUS":
            await chan.send("He ba bienvenue a l'ASTUS ! \n"
                            "Tout d'abord, felicitation a toi pour avoir integrer l'ASTUS :wink: \n"
                            "Tu as maintenant acces à la categorie ASTUS, tu retrouvera un channel general pour"
                            "parler avec tout tes p'tits potes de l'ASTUS. Et un channel passation pour parler avec"
                            "l'ancien G4 de la gestion de l'ASTUS. En fonction de ton rôle, tu ne vois pas certains"
                            "channel, je t'explique tout ca rapidement :wink:")

        if new_role.name == "G4":
            await chan.send("Un grand pouvoir inplique de grande responsabilitées. C'est grave a toi que l'astus "
                            "peut tourner. Tu as acces a quelque commande de gestion du serveur (plus d'info "
                            "avec ``" + PREFIX + "help`` sur le serveur")

        if new_role.name == "Team Event":
            await chan.send("C'est toi qui va nous régaler avec tous pleins d'Event")

        if new_role.name == "Resp Team Event":
            await chan.send("Resp de la team Event  ! ")

        if new_role.name == "Team Entreprise":
            await chan.send("C'est toi qui va nous regaler avec tous pleins de rencontre avec des ETS")

        if new_role.name == "Resp Team Entreprise":
            await chan.send("Resp de la team Entreprise  ! ")

        if new_role.name == "Resp Site International":
            await chan.send("Resp du site ! \n"
                            "C'est grace a toi que le site peut evoluer, demande a ce qu'on t'ajoute au"
                            "repo GitHub :wink:")

        if new_role.name == "Resp Comm":
            await chan.send("Resp comm ! \n"
                            "L'ASTUS compte sur toi pour un max de communication. Tu geres la page FB de l'astus."
                            "Tu fais les annonces et les affiches pour tous les events ")

if __name__ == '__main__':
    import cogs.newyear
    import cogs.passation
    import cogs.help
    import cogs.videoDiplomes

    # Remove default help command
    bot.remove_command("help")

    # cogs
    bot.add_cog(cogs.passation.CogPassation(bot))
    bot.add_cog(cogs.newyear.CogNewyear(bot))
    bot.add_cog(cogs.help.CogNewyear(bot))
    bot.add_cog(cogs.videoDiplomes.CogVideoDiplomes(bot))

    bot.run(TOKEN)
