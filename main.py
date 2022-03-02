import discord

client = discord.Client()

@client.event
async def on_ready():
  print('Bot is now online and ready to roll')

client.run('OTQ4NDE3NTUzMTc5NDg0MzAw.Yh7grQ.mi5E8UizTDalF1F4NQcktXwjZLg')