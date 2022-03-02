import discord

class MyClient(discord.Client):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.target_message_id = 948586007647891488

  async def on_ready(self):
    print('Ready')

  async def on_raw_reaction_add(self, payload):
    '''
    Give a role based on reaction emoji
    '''
    if payload.message_id != self.target_message_id:
      return

    guild = client.get_guild(payload.guild_id)

    if payload.emoji.name == '💯':
      role = discord.utils.get(guild.roles, name =         'Top class')
      await payload.member.add_roles(role)
    elif payload.emoji.name == '🔥':
      role = discord.utils.get(guild.roles, name = 'Fire cracker')
      await payload.member.add_roles(role)
    elif payload.emoji.name == '🚀':
      role = discord.utils.get(guild.roles, name = 'Rocket launcher')
      await payload.member.add_roles(role)
      
  async def on_raw_reaction_remove(self, payload):
    '''
    Remove a role based on reaction emoji
    '''
    if payload.message_id != self.target_message_id:
      return

    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)

    if payload.emoji.name == '💯':
      role = discord.utils.get(guild.roles, name =         'Top class')
      await member.remove_roles(role)
    elif payload.emoji.name == '🔥':
      role = discord.utils.get(guild.roles, name = 'Fire cracker')
      await member.remove_roles(role)
    elif payload.emoji.name == '🚀':
      role = discord.utils.get(guild.roles, name = 'Rocket launcher')
      await member.remove_roles(role)

intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
#client.run('token')