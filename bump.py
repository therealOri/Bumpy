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
      await ctx.send("I don't listen to you.")


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
      await ctx.send("I don't listen to you.")

      
      
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
      await ctx.send("I don't listen to you.")


      

#You will need to run this command again in the verification channel after restarting the bot/account so it can start the event function and wait for reactions.
#If you can fix it so it doesn't need to be re ran again after restrt then be my guest.
@client.command(pass_context=True)
async def verify(ctx):
  if ctx.author.id == your_main_account_id_here:
    Embed = discord.Embed(title="Verification", description="React to this message to gain access to the server!", color=discord.Color.green())
    msg = await ctx.send(embed=Embed)
    await msg.add_reaction("✅")
  else:
      await ctx.send("I don't listen to you.")

        
@client.event
async def on_reaction_add(reaction, member):
    Channel = client.get_channel('id_of_channel_for_verification_here')
    if reaction.message.channel.id != same_id_here_as_above:
        return
    if reaction.emoji == "✅":
        role = discord.utils.get(member.guild.roles, name='ROLE_NAME_HERE_TO_GIVE_USERS_AFTER_VERIFICATION')
        await member.add_roles(role)
      
      
      
  
#Counts the message/command you send as part of how many to want to delete. Example: p.purge 8 to purge 7 messages from the channel, because it counts your command as 1.
@client.command(pass_context=True)
async def purge(ctx, amount=7):
    if ctx.author.id == your_main_account_id_here:
      await ctx.channel.purge(limit=amount)
    else:
      await ctx.send("I don't listen to you.")



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"Doing teh bumps"), status=discord.Status.online)
    print("User Online!")
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN, bot=False)
