import discord
import asyncio
import requests
import random


client = discord.Client()

COR = 0x35acf1
msg_id = None
msg_user = None
url = "https://i.imgur.com/6pzAWfP.jpg"


@client.event
async def on_ready():
    print('Color BOT - nebaaaa!')
    print(client.user.name)
    print(client.user.id)


@client.event
async def on_message(message):
    if message.content.lower().startswith(".planetas"):
        embed1 = discord.Embed(
            title="Escolha sua cor:",
            color=COR,
            description="- Urano =  💎 \n"
                        "- Netuno  =  ☄ \n"
                        "- Mercúrio  =  🍊 \n"
                        "- Saturno  =  🍋 \n"
                        "- Terra  =  🥒 \n"
                        "- Vênus =  🍎 \n"
                        "- Júpiter =  🍑 \n"
                        "- Marte =  🍒 \n")


    if message.content.lower().startswith("#adr"):
        await client.send_message(message.channel, "http://prntscr.com/lw9g9p")
    if message.content.lower().startswith(".f"):
        await client.send_message(message.channel, url)
    if message.content.lower().startswith(".cancer"):
        testeMsg = random.randint(1, 6)
        if testeMsg == 1:
            await client.send_message(message.channel, "neeeeeeeeeeeeee")

        if testeMsg == 2:
            await client.send_message(message.channel, "neeeebaaaaaaaaa")

        if testeMsg == 3:
            await client.send_message(message.channel, "neeeeezambas")

        if testeMsg == 4:
            await client.send_message(message.channel, "nem")

        if testeMsg == 5:
            await client.send_message(message.channel, "pior que nem em")

        if testeMsg == 6:
            await client.send_message(message.channel, "se pá nem em")

    if message.content.lower().startswith(".keli"):
        await client.send_message(message.channel, "pegalá a poeira cósmica keli")

        botmsg = await client.send_message(message.channel, embed=embed1)

        await client.add_reaction(botmsg, "💎")
        await client.add_reaction(botmsg, "☄")
        await client.add_reaction(botmsg, "🍊")
        await client.add_reaction(botmsg, "🍋")
        await client.add_reaction(botmsg, "🥒")
        await client.add_reaction(botmsg, "🍎")
        await client.add_reaction(botmsg, "🍑")
        await client.add_reaction(botmsg, "🍒")

    global msg_id
    msg_id = botmsg.id

    global msg_user
    msg_user = message.author

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "💎" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Urano", msg.server.roles)
        await client.add_roles(user, role)
        print("=============================================")
        print("added to:", user, ", was added:", role)
        print("=============================================")

    if reaction.emoji == "☄" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Netuno", msg.server.roles)
        await client.add_roles(user, role)
        print("=============================================")
        print("added to:", user, ", was added:", role)
        print("=============================================")

    if reaction.emoji == "🍊" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Mercúrio", msg.server.roles)
        await client.add_roles(user, role)
        print("=============================================")
        print("added to:", user, ", was added:", role)
        print("=============================================")

    if reaction.emoji == "🍋" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Saturno", msg.server.roles)
        await client.add_roles(user, role)
        print("=============================================")
        print("added to:", user, ", was added:", role)
        print("=============================================")

    if reaction.emoji == "🥒" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Terra", msg.server.roles)
        await client.add_roles(user, role)
        print("=============================================")
        print("added to:", user, ", was added:", role)
        print("=============================================")

    if reaction.emoji == "🍎" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Vênus", msg.server.roles)
        await client.add_roles(user, role)
        print("=============================================")
        print("added to:", user, ", was added:", role)
        print("=============================================")

    if reaction.emoji == "🍑" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Júpiter", msg.server.roles)
        await client.add_roles(user, role)
        print("=============================================")
        print("added to:", user, ", was added:", role)
        print("=============================================")

    if reaction.emoji == "🍒" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Marte", msg.server.roles)
        await client.add_roles(user, role)
        print("=============================================")
        print("added to:", user, ", was added:", role)
        print("=============================================")


@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == "💎" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Urano", msg.server.roles)
        await client.remove_roles(user, role)
        print("=============================================")
        print("removed from:", user, ", was removed:", role)
        print("=============================================")

    if reaction.emoji == "☄" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Netuno", msg.server.roles)
        await client.remove_roles(user, role)
        print("=============================================")
        print("removed from:", user, ", was removed:", role)
        print("=============================================")

    if reaction.emoji == "🍊" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Mercúrio", msg.server.roles)
        await client.remove_roles(user, role)
        print("=============================================")
        print("removed from:", user, ", was removed:", role)
        print("=============================================")

    if reaction.emoji == "🍋" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Saturno", msg.server.roles)
        await client.remove_roles(user, role)
        print("=============================================")
        print("removed from:", user, ", was removed:", role)
        print("=============================================")

    if reaction.emoji == "🥒" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Terra", msg.server.roles)
        await client.remove_roles(user, role)
        print("=============================================")
        print("removed from:", user, ", was removed:", role)
        print("=============================================")

    if reaction.emoji == "🍎" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Vênus", msg.server.roles)
        await client.remove_roles(user, role)
        print("=============================================")
        print("removed from:", user, ", was removed:", role)
        print("=============================================")

    if reaction.emoji == "🍑" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Júpiter", msg.server.roles)
        await client.remove_roles(user, role)
        print("=============================================")
        print("removed from:", user, ", was removed:", role)
        print("=============================================")

    if reaction.emoji == "🍒" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Marte", msg.server.roles)
        await client.remove_roles(user, role)
        print("=============================================")
        print("removed from:", user, ", was removed:", role)
        print("=============================================")


client.run('NTIxMTAxNzgxMDg2ODk2MTUw.DvsY6g.e6ZB_jbpuPkVA03m6l1WUjG24CY')
