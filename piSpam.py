# Import Discord Package
import discord
import json
import os
from discord.ext import commands

# Setup important data

with open(os.path.abspath(os.path.join(os.path.dirname("piSpam.py"), "PiSpamDiscordBot\\secret.json"))) as f:
    data = json.load(f)


#Client (our bot)

client = discord.Client()

@client.event
async def on_ready():
    general_channel = client.get_channel(769024871719501838)
    await general_channel.send("Sup.")

print(data['saver'] + data['saver2'] + data['saver3'])

client.run(data['saver'] + data['saver2'] + data['saver3'])