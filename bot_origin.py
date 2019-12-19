from discord import client
import discord
import random


tokendice = ""
client = discord.Client()


def dice_throw(dicetype):
    dicedrop = random.randrange(1,int(dicetype))
    return f'{dicedrop}'


@client.event
async def on_message(message):
    print(f'{message.author} send message {message.content}')
    if f"{message.content}".startswith("!d"):
        dicetype = f"{message.content}".split(sep="d")[1]
        result = dice_throw(dicetype)
        response = f"{result}"
        await message.channel.send(response)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(tokendice)