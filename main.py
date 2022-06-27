import os

import discord
GUILD = "redacted"

client = discord.Client()

def kingcheck(message):
    if message.author.nick == "King":
        return True
    else:
        return False


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("HELP!"): ##help command
        await message.channel.send("""
        Welcome to Break-A-Bot. See what you can break. Here are my commands:
        HELP! - this command
        DAD! - do the classic "hi ____ I'm dad"
        ADD! - add two numbers
        SUB! - subtract two numbers
        MUL! - multiply two numbers
        DIV! - divide two numbers

        KING COMMANDS - only for 'King'
        ADDRESS! - verify that you are king
        CALM! - shuts down the bot

        """)

    if message.content.startswith("DAD!"): ## the daddening
        await message.channel.send("Hi " + message.content[4:] + ", I'm DAD. HAHAHAHA.")

    if message.content.startswith("ADD!"): ##addition function
        src = message.content[4:].split(" ")
        fin = 0
        for each in src:
            print(each)
            if each != "":
                fin = fin + int(each)
        await message.channel.send("Your answer: " + str(fin))

    if message.content.startswith("SUB!"): ##subtraction function
        src = message.content[4:].split(" ")
        fin = 0
        for each in src:
            print(each)
            if each != "":
                if fin != 0:
                    fin = fin - int(each)
                else:
                    fin = each

        await message.channel.send("Your answer: " + str(fin))

    if message.content.startswith("MUL!"): ##multiplication function in math
        src = message.content[4:].split(" ")
        print(src)
        fin = 0
        for each in src:
            print(each)
            if each != "":
                if fin != 0:
                    print(fin)
                    fin = fin * int(each)
                    print("tmp fin: " + str(fin))
                elif fin == 0:
                    fin = each ## this line right here
                    print(fin)
        await message.channel.send("Your answer: " + str(fin))

    if message.content.startswith("DIV!"): ##division function
        src = message.content[4:].split(" ")
        fin = 0
        for each in src:
            print(each)
            if each != "":
                if fin != 0:
                    fin = fin / int(each)
                else:
                    fin = each ## also this line
        await message.channel.send("Your answer: " + str(fin))

    if message.content.startswith("ADDRESS!"): ##king doing king things
        if kingcheck(message):
            await message.channel.send("Hello, my king.")
        else:
            await message.channel.send("You are not my king")

    if message.content.startswith("CALM!"): ## goodbye Bot
        if kingcheck(message):
            exit()
        else:
            await message.channel.send("BLASPHEMY")

client.run('redacted')
