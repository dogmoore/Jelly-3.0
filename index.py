# bot.py
import os
import yaml
import discord
from discord.ext import commands


from dotenv import load_dotenv

with open("config.yml", "r") as ymlfile:
    bot = yaml.load(ymlfile, Loader=yaml.FullLoader)
    TOKEN = bot['token']
    PREFIX = bot['prefix']

# TOKEN = os.getenv('ODAyMDE0MjcyNDE0NDE2OTA3.YApD_w.CuTo6dxfyrJa8ivmmWQA-nStQhE')

intents = discord.Intents.default()
client = Bot(command_prefix=PREFIX, help_command=None, activity=activity, intents=intents)
client = discord.Client()

for x in os.listdr('commands'):
    try:
        client.load_extension(f'commands.{x[:-3]}')
        print(f'\033[92m{i[:-3]}] loaded.\033[0m]')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run('ODAyMDE0MjcyNDE0NDE2OTA3.YApD_w.CuTo6dxfyrJa8ivmmWQA-nStQhE')
