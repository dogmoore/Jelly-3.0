import yaml
import discord
import random
from discord.ext import commands
# from abc import ABCMeta
# from abc_delegation import delegation_metaclass

with open("config.yml", "r") as ymlfile:
    config = yaml.load(ymlfile, Loader=yaml.FullLoader)

# class message:
#     discord.abc.Snowflake

# with open("bot.yml", "r") as ymlfile:
#     bot = yaml.load(ymlfile, Loader=yaml.FullLoader)

class Utils(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(name='ping')
    async def ping(self, context):
        client = self.client
        await context.send('test')



    @commands.command(name='shutdown')
    async def shutdown(self, context):
        client = self.client
        if context.author.id == 376857933067321366 or context.author.id == 278548721778688010:
            await context.send('Ok, time for bed')
            await context.send('Dog and Jelly 1.0 let\'s go sleep')
            await client.close()
        else:
            await context.send('Something went wrong')

def setup(client):
   client.add_cog(Utils(client))
