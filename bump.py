import asyncio
import discord

from discord.ext import commands

client = commands.Bot(description='Discord Auto Bumper!', command_prefix="p.")#prefix is changeable. Make it so no one will ever guess it. (unless they see you use it then it's kinda meh.

TOKEN = 'YOUR_TOKEN_HERE'



@client.command(pass_context=True)
async def ping(ctx):
  if ctx.author.id == your_main_account_id_here:
    await ctx.send(f"pong! connection speed is {round(client.latency * 1000)}ms")
  else:
      pass


#    """Starts the timer to bump every 2 hrs and 1 min because sometimes the disboard bot gives an error and tells you to wait 1 more min."""
@client.command(pass_context=True)
async def bump(ctx):
  if ctx.author.id == your_main_account_id_here:
    while 1:
      bumpy = 0
      bumpy = bumpy + 1
      try:
        print("Processing new bump!")
        await ctx.send('!d bump')
        await asyncio.sleep(7260)
        print(f"Bump {bumpy} succesfully bumped the server with disboard!")
      except:
        print(f"Couldn't Process bump :( {bumpy}.")
  else:
      pass

      
      
#   """Starts the timer to bump every 40 mins"""
#It's set to 40 min because I have a channel for DSC to post other servers in, which in return allows you to bump faster. Otherwise it's 2hrs. 7200s = 2hrs.
@client.command(pass_context=True)
async def dsc(ctx):
  if ctx.author.id == your_main_account_id_here:
    while 1:
      dscB = 0
      dscB = dscB + 1
      try:
        print("Processing DSC bump!")
        await ctx.send('d=bump')
        await asyncio.sleep(2400)
        print(f"Bump {dscB} succesfully bumped the server using DSC!")
      except:
        print(f"Couldn't Process bump :( {dscB}.")
  else:
      pass
            
      
  
#Counts the message/command you send as part of how many to want to delete. Example: p.purge 8 to purge 7 messages from the channel, because it counts your command as 1.
@client.command(pass_context=True)
async def purge(ctx, amount=7):
    if ctx.author.id == your_main_account_id_here:
      await ctx.channel.purge(limit=amount+1)
    else:
      pass



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"Doing teh bumps"), status=discord.Status.online)
    print("User Online!")
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN, bot=False)
