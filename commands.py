from discord.ext import commands

bot = commands.Bot(command_prefix = '!')

@bot.command()
async def punch(ctx, arg):
  """
  !punch Xavi
  """
  await ctx.send(f'Punched {arg}')

@bot.command()
async def double_punch(ctx, arg1, arg2):
  """
  !double_punch Xavi and Andre
  """
  await ctx.send(f'Double punched {arg1} and {arg2}')

@bot.command()
async def roundhouse_kick(ctx, *args):
  """
  !roundhouse_kick Xavi Hope Ana     Sue
  """
  everyone = ', '.join(args) # takes a list of items and converts them into a string seperated by commas
  await ctx.send(f'Roundhouse kicked  {everyone}')

@bot.command()
async def info(ctx):
  '''
  ctx - context (information about how the command  executed)
  !info
  '''

  await ctx.send(ctx.guild)
  await ctx.send(ctx.author)
  await ctx.send(ctx.message.id)


#bot.run(token)

