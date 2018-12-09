import discord
import asyncio
import random

client = discord.Client()

COR =0x35acf1
msg_id = None
msg_user = None


@client.event
async def on_ready():
    print('Color BOT - nebaaaa!')
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):

    if message.content.lower().startswith(".cor"):
     embed1 =discord.Embed(
        title="Escolha sua cor:",
        color=COR,
        description="- Roxo = 🍇 \n"
                    "- Rosa  =  🍒 \n"
                    "- Vermelho  = 🍓 \n"
                    "- Azul  =  💎 \n"
                    "- Verde  =   🍏\n"
                    "- Amarelo =  🍋 \n"
                    "- Laranja  = 🍊 \n"
                    "- Limpar = 🌽 \n")
    if message.content.lower().startswith(".a")
      await client.send_message(message.channel, "http://prntscr.com/lsreya")
    if message.content.lower().startswith(".cancer"):
        testeMsg = random.randint(1,2)
        if testeMsg == 1:
            await client.send_message(message.channel, "o zeza")

        if testeMsg == 2:
            await client.send_message(message.channel, "neeezambas")


    if message.content.lower().startswith(".keli"):
        await client.send_message(message.channel, "pegalá")

    botmsg = await client.send_message(message.channel, embed=embed1)

    await client.add_reaction(botmsg, "🍇")
    await client.add_reaction(botmsg, "🍒")
    await client.add_reaction(botmsg, "🍓")
    await client.add_reaction(botmsg, "💎")
    await client.add_reaction(botmsg, "🍏")
    await client.add_reaction(botmsg, "🍋")
    await client.add_reaction(botmsg, "🍊")
    await client.add_reaction(botmsg, "🌽")

    global msg_id
    msg_id = botmsg.id

    global msg_user
    msg_user = message.author


@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🍇" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Roxo", msg.server.roles)
     await client.add_roles(user, role)
     print("=============================================")
     print("added to:", user, ", was added:", role)
     print("=============================================")

    if reaction.emoji == "🍒" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Rosa", msg.server.roles)
     await client.add_roles(user, role)
     print("=============================================")
     print("added to:", user, ", was added:", role)
     print("=============================================")

    if reaction.emoji == "🍓" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Vermelho", msg.server.roles)
     await client.add_roles(user, role)
     print("=============================================")
     print("added to:", user, ", was added:", role)
     print("=============================================")

    if reaction.emoji == "💎" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Azul", msg.server.roles)
     await client.add_roles(user, role)
     print("=============================================")
     print("added to:", user, ", was added:", role)
     print("=============================================")

    if reaction.emoji == "🍏" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Verde", msg.server.roles)
     await client.add_roles(user, role)
     print("=============================================")
     print("added to:", user, ", was added:", role)
     print("=============================================")

    if reaction.emoji == "🍋" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Amarelo", msg.server.roles)
     await client.add_roles(user, role)
     print("=============================================")
     print("added to:", user, ", was added:", role)
     print("=============================================")


    if reaction.emoji == "🍊" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Laranja", msg.server.roles)
     await client.add_roles(user, role)
     print("=============================================")
     print("added to:", user, ", was added:", role)
     print("=============================================")

    if reaction.emoji == "🌽" and msg.id == msg_id:  # and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Nada", msg.server.roles)
     await client.add_roles(user, role)
     print("=============================================")
     print("added to:", user, ", was added:", role)
     print("=============================================")


@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == "🍇" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Roxo", msg.server.roles)
     await client.remove_roles(user, role)
     print("=============================================")
     print("removed from:", user, ", was removed:", role)
     print("=============================================")

    if reaction.emoji == "🍒" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Rosa", msg.server.roles)
     await client.remove_roles(user, role)
     print("=============================================")
     print("removed from:", user, ", was removed:", role)
     print("=============================================")

    if reaction.emoji == "🍓" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Vermelho", msg.server.roles)
     await client.remove_roles(user, role)
     print("=============================================")
     print("removed from:", user, ", was removed:", role)
     print("=============================================")

    if reaction.emoji == "💎" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Azul", msg.server.roles)
     await client.remove_roles(user, role)
     print("=============================================")
     print("removed from:", user, ", was removed:", role)
     print("=============================================")

    if reaction.emoji == "🍏" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Verde", msg.server.roles)
     await client.remove_roles(user, role)
     print("=============================================")
     print("removed from:", user, ", was removed:", role)
     print("=============================================")

    if reaction.emoji == "🍋" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Amarelo", msg.server.roles)
     await client.remove_roles(user, role)
     print("=============================================")
     print("removed from:", user, ", was removed:", role)
     print("=============================================")

    if reaction.emoji == "🍊" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Laranja", msg.server.roles)
     await client.remove_roles(user, role)
     print("=============================================")
     print("removed from:", user, ", was removed:", role)
     print("=============================================")

    if reaction.emoji == "🌽" and msg.id == msg_id:  # and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Nada", msg.server.roles)
     await client.remove_roles(user, role)
     print("=============================================")
     print("removed from:", user, ", was removed:", role)
     print("=============================================")



client.run('NTIxMTAxNzgxMDg2ODk2MTUw.Du3n5A.N8uqaukqvnGdXqDFSeUjXPVWKf8')
