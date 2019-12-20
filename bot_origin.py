from discord import client
import discord
import random
import re


tokendice = ""
client = discord.Client()


def dice_throw(dicecount, dicetype):
    dice_res = []
    for i in range(dicecount):
        dicedrop = random.randrange(1, int(dicetype)+1)
        dice_res.append(dicedrop)
    return f'{dice_res}'


def parse_command(command):
    matches = re.findall(r'\d+', command)
    return matches


@client.event
async def on_message(message):
    print(f'{message.author} send message {message.content}')
    if f"{message.content}".startswith(f"throw"):
        try:
            dices = f'{message.content}'.split(" ")[1]
        except IndexError:
            return
        if f"{message.content}".startswith(f"throw {dices}"):
            patern = parse_command(message.content)
            dicecount = int(patern[0])
            dicetype = patern[1]
            result = dice_throw(dicecount,dicetype)
            response = f"{result}"
            await message.channel.send(response)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(tokendice)