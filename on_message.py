import discord

client = discord.Client()

@client.event
async def on_ready():
  print('Bot is now online and ready to roll')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content == 'hello':
    await message.channel.send('Welcome to K7officialServer')
    client.run('OTQ4NDE3NTUzMTc5NDg0MzAw.Yh7grQ.VqCguagFaZkXVEfX5728M1dGmhE')