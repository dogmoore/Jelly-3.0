import yaml
import discord
from discord.ext import commands

with open("config.yml", "r") as ymlfile:
    config = yaml.load(ymlfile, Loader=yaml.FullLoader)

# with open("bot.yml", "r") as ymlfile:
#     bot = yaml.load(ymlfile, Loader=yaml.FullLoader)

class Utils(commands.Cog):
    def __init__(self,client):
        self.client = client

@commands.command(name='ping')
async def ping(self, context):
    client = self.client
    await message.send('test')

def setup(client):
   client.add_cog(Utils(client))
