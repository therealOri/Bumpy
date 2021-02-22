import asyncio
import discord

from discord.ext import commands

client = commands.Bot(description='Disboard Auto Bumper!', command_prefix="p.")

TOKEN = 'TOKENHERE'


@client.command(aliases=['working check'])
async def ping(ctx):
    await ctx.send(f"pong! connection speed is {round(client.latency * 1000)}ms")



@client.command(aliases=['bump'])
async def start(ctx):
#    """Starts the timer to bump every 2 hrs and 1 minute"""
    while 1:
        bumpy = 0
        bumpy = bumpy + 1
        try:
            print("Bumping your server with Disboard!")
            await ctx.send('!d bump')
            await asyncio.sleep(7260)
            print(f"Bump {bumpy} succesfully bumped the server with disboard!")
        except:
            print(f"Couldn't Process bump :( {bumpy}.")


@client.command(aliases=['bump2'])
async def start2(ctx):
#    """Starts the timer to bump every 2 hrs"""
    while 1:
        bumpy = 0
        bumpy = bumpy + 1
        try:
            print("Bumping your server with DSC!")
            await ctx.send('.bump')
            await asyncio.sleep(7200)
            print(f"Bump {bumpy} succesfully bumped the server using DSC!")
        except:
            print(f"Couldn't Process bump :( {bumpy}.")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"Doing teh bumps"), status=discord.Status.online)
    print("User Online!")
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN, bot=False)
