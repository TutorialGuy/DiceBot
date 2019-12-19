import random
import json
import discord
import requests

dicetype = None
dicedrop = random.randrange(1,dicetype)
message = None
webhook = ""

def dice_throw():
    return "Dice threw {}".format(dicedrop)

message = dice_throw()
print(message)

discord_data = {'content': "{}".format(dice_throw())}
responce = requests.post(url=webhook,
                         data=discord_data
                         )


