import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='s.')

@bot.event
async def on_typing(channel, user, when):
    await channel.send("shut up " + str(user), delete_after=0.5)

bot.run(token)