import discord
import yaml
import random
from discord.ext import commands

with open("config.yml", "r") as ymlfile:
    config = yaml.load(ymlfile, Loader=yaml.FullLoader)


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        client = self.client
#        try:
        oneInHundred = random.randint(1, 100)
        oneInTen = random.randint(1, 10)

        msg = ['who do you love jelly 3.0', 'who do you love jelly3.0', 'who do you love jelly']

        if message.author.id == 278548721778688010 and oneInHundred == 7:
            await message.reply('DON\'T LISTEN TO THIS HEATHEN, I AM THE REAL JELLY!')
        elif message.content.lower() in msg:
            if oneInTen == 1:
                await message.channel.send('some gay fuck')
            elif oneInTen == 2:
                await message.channel.send('DOGMOORE!')
            elif oneInTen == 3:
                await message.channel.send('some weird chick who says she\'s a cat')
            elif oneInTen == 4:
                await message.channel.send('a ginger hehe')
            elif oneInTen == 5:
                await message.channel.send('APaperbot')
            elif oneInTen == 6:
                await message.channel.send('Jellyfish!...but he never responds to my texts....D:')
            elif oneInTen == 7:
                await message.channel.send('PAPEE')
            elif oneInTen == 8:
                await message.channel.send('FATAL!!!!!!')
            elif oneInTen == 9:
                await message.channel.send('idk, no one?')
            elif oneInTen == 10:
                await message.channel.send('The one and only Queen, Freddie Mercury!')
            else:
                print(f'random failed')


def setup(client):
    client.add_cog(Events(client))
