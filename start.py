import discord
import os

TOKEN = os.getenv("BOT_TOKEN")
client = discord.Client()


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
        if message.content == "ping":
            await message.channel.send("pong")


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
