import discord
import yaml
from discord.ext import commands

with open("config.yml", "r") as ymlfile:
    config = yaml.load(ymlfile, Loader=yaml.FullLoader)

# with open("bot.yml", "r") as ymlfile:
#     bot = yaml.load(ymlfile, Loader=yaml.FullLoader)


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client
        #self._cd = commands.CooldownMapping.from_cooldown(1.0, 10.0, commands.BucketType.guild)

def setup(client):
    client.add_cog(Events(client))
