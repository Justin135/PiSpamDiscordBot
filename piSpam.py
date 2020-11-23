# Import Discord Package
import discord

from discord.ext import commands

# Setup important data
TOKEN = "NzgwMjQ2MTY1Njg5NTk3OTgy.X7sS3g.MC9CBi70UKLMO20F3i4DGyManuY"

#Client (our bot)
client = discord.Client()

@client.event
async def on_ready():
    general_channel = client.get_channel(769024871719501838)
    await general_channel.send("Sup.")

client.run(TOKEN)