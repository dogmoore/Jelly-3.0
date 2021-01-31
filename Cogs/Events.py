import discord
import yaml
import random
from discord.ext import commands

with open("config.yml", "r") as ymlfile:
    config = yaml.load(ymlfile, Loader=yaml.FullLoader)

# with open("bot.yml", "r") as ymlfile:
#     bot = yaml.load(ymlfile, Loader=yaml.FullLoader)


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client
        #self._cd = commands.CooldownMapping.from_cooldown(1.0, 10.0, commands.BucketType.guild)

    @commands.Cog.listener()
    async def on_message(self, message):
        client = self.client
        try:
            oneInHundred = random.randint(1, 100)
            oneInTen = random.randint(1, 10)

            if message.author.id == 278548721778688010 and oneInHundred == 7:
                await message.reply('DON\'T LISTEN TO THIS HEATHEN, I AM THE REAL JELLY!')
            elif 'Who do you love jelly 3.0'.lower() in message.content.lower():
                if oneInTen == 1:
                    await message.send('some gay fuck')
                elif oneInTen == 2:
                    await message.send('DOGMOORE!')
                elif oneInTen == 3:
                    await message.send('some weird chick who says she\'s a cat')
                elif oneInTen == 4:
                    await message.send('a ginger hehe')
                elif oneInTen == 5:
                    await message.send('APaperbot')
                elif oneInTen == 6:
                    await message.send('Jellyfish!...but he never responds to my texts....D:')
                elif oneInTen == 7:
                    await message.send('PAPEE')
                elif oneInTen == 8:
                    message.send('FATAL!!!!!!')
                elif oneInTen == 9:
                    await message.send('idk, no one?')
                elif oneInTen == 10:
                    await message.send('The one and only Queen, Freddie Mercury!')
                else:
                    await print(f'random failed')
        except:
            pass

def setup(client):
    client.add_cog(Events(client))
