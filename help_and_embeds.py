import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '!')
bot.remove_command('help') # removes the default help command

@bot.command()
async def help(ctx):
  embed = discord.Embed(
    title='Bot Commands',
    description ='Welcome to the help section. Here are all commands for this game',
    color=discord.Colour.green()
  )
  embed.set_thumbnail(url='https://images.unsplash.com/photo-1479936343636-73cdc5aae0c3?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2360&q=80')
  embed.add_field(
    name ='!help',
    value='List all of the commands',
    inline=False
  )
  embed.add_field(
    name ='!punch',
    value='Punch another players',
    inline=False
  )
  embed.add_field(
    name ='!roundhouse_kick',
    value='Roundhouse kick another player',
    inline=False
  )
  await ctx.send(embed=embed)
  

@bot.command()
async def punch(ctx, arg):
  """
  This command punches another player
  """
  await ctx.send(f'Punched {arg}')


@bot.command()
async def roundhouse_kick(ctx, *args):
  
  everyone = ', '.join(args) # takes a list of items and converts them into a string seperated by commas
  await ctx.send(f'Roundhouse kicked  {everyone}')

#bot.run('token')

#the help command is gonna go thru and look at all your commands and pull the docstrings for the description text