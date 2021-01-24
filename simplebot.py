import discord
from discord.ext import commands

client = commands.Bot(command_prefix= commands.when_mentioned_or('!'))

@client.event
async def on_ready():
    #you can change the bot status here
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="My Creator suffer becoz the command didn't work "))
    print('We have logged in as {0.user}'.format(client)) 

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hi {0.author.mention}'.format(message)
        await message.send(message.channel, msg)   

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong **ping**: {round(client.latency * 1000)}ms")         

client.run('Nzk1ODY5MTI0OTQ5NTczNjcy.X_Po4Q.bprUGMEuqXtpw-X-wy3xiFkZMPo')