import discord

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTM1MjY2NTkyNTUwNTEyMjM1Ng.GtxnJP.DnNWsYMLhnzDZAE37gO6fHca4szdgEVzxj8aOY')