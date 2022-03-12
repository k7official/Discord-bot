#01 on messege events

import discord
#import reactions_and_edits
#import on_message
import reaction_roles
from commands import *


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


#bot.run('OTQ4NDE3NTUzMTc5NDg0MzAw.Yh7grQ.Rb9ws-kCmVvoLQQKET97x6uIATc')

#client.run(token)