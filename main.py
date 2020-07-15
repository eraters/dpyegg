import discord
from discord.ext import commands, tasks

@client.event
async def on_ready():
    print('Bot ready.')

client.run('TOKEN HERE')
