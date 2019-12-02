import discord
import random
from discord.ext import commands

prefix = "~"
client = commands.Bot(command_prefix = prefix)
errors = discord.ext.commands.errors
client.remove_command("help")
lol = [False]

#starting making commands and events

#commmands
@client.command(aliases = ["set welcome channel", "set channel for welcome", "set welcome"])
async def set(cont):
    await cont.channel.send("Done")
    lol[0] = True

@client.command()
async def check(cont):
    await cont.channel.send("lets see")
    if lol[0]:
        await cont.channel.send ("yea boi worked")
    else :
        await cont.channel.send("NOPE")

#events
@client.event
async def on_member_join(member):
    guild = member.guild
    channel = discord.utils.get(guild.text_channel , name = welcome_channel)

@client.event
async def on_ready():
    print("yea boi i am ready for your service")

client.run("NjUxMTEwMDc5ODI2NzU1NjA0.XeVHlQ._TgKzuYGsDk8CBy4r104ozrGVfc")
