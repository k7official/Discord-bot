#01 on messege events

import discord
#import reactions_and_edits
#import on_message
import reaction_roles


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


