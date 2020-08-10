import os
import logging
import asyncio
import discord

from discord.ext import commands

client = commands.Bot(description='Disboard Auto Bumper!', command_prefix="o.")

TOKEN = 'TOKENHERE'


@client.command(aliases=['working check'])
async def ping(ctx):
    await ctx.send(f"pong! connection speed is {round(client.latency * 1000)}ms")



@client.command(aliases=['bump'])
async def start(ctx):
#    """Starts the timer to bump every 2 hrs"""
    while 1:
        bumpy = 0
        bumpy = bumpy + 1
        try:
            print("Processing new bump!")
            await ctx.send('!d bump')
            await asyncio.sleep(7200)
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
            print("Processing new bump2!")
            await ctx.send('.bump')
            await asyncio.sleep(7200)
            print(f"Bump {bumpy} succesfully bumped the server using DSC!")
        except:
            print(f"Couldn't Process bump :( {bumpy}.")


@client.event
async def on_connect():
    print('Bumpy Online! | Succesful connection!')


@client.event
async def on_ready():
    print('All Systems ready to go!')


client.run(TOKEN, bot=False)
