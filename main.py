import discord

client = discord.Client()

@client.event
async def on_ready():
  print('Bot is now online and ready to roll')

client.run('OTQ4MjM3NDc1MzQ2Nzg0MzU3.Yh449w.DDojUAu3Dua4cnuPavztEco4Fvo')