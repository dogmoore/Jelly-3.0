import discord
import yaml
import random
import asyncio
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
        oneInMeme = random.randint(1, 69420)
        oneInTen = random.randint(1, 10)

        i = ''
        x = ''

        msg = {'who do you love jelly3', 'who do you love jelly3.0', 'who do you love jelly',
               'who do you love jelly 3.0'}
        msg2 = {'how are you doing jelly', 'how are you doing jelly3.0', 'how are you doing jelly3',
                'how are you doing jelly 3.0'}

        timer = 2

        # if client.user.mentioned_in(message):
        #     emote = '<a:pinged:807363547793326080>'
        #     emote2 = '<:sanic:807366430306861086>'
        #     await message.add_reaction(str(emote))
        #     await message.channel.send(str(emote2))

        if message.author.id == 278548721778688010 and oneInMeme == 7:
            print('\'jelly is a heathen\' triggered')
            async with message.channel.typing():
                await asyncio.sleep(1)
            await message.reply('DON\'T LISTEN TO THIS HEATHEN, I AM THE REAL JELLY!')
        elif message.content.lower() in msg:
            if oneInTen == 1:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('some gay fuck')
                i = 1
            elif oneInTen == 2:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('DOGMOORE!')
                i = 2
            elif oneInTen == 3:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('some weird chick who says she\'s a cat')
                i = 3
            elif oneInTen == 4:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('a ginger hehe')
                i = 4
            elif oneInTen == 5:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('APaperbot')
                i = 5
            elif oneInTen == 6:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('Jellyfish!...but he never responds to my texts....D:')
                i = 6
            elif oneInTen == 7:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('PAPEE')
                i = 7
            elif oneInTen == 8:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('FATAL!!!!!!')
                i = 8
            elif oneInTen == 9:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('idk, no one?')
                i = 9
            elif oneInTen == 10:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('The one and only Queen, Freddie Mercury!')
                i = 10
            print(f'who does jelly-3.0 love issued and returned option: {i}')
        elif message.content.lower() in msg2:
            if oneInTen == 1:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('bloody dreadful')
                x = 1
            elif oneInTen == 2:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('I\'m doing alright')
                x = 2
            elif oneInTen == 3:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('real question is, how are you doing?')
                x = 3
            elif oneInTen == 4:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('sorta feel like using a forbidden bath bomb')
                x = 4
            elif oneInTen == 5:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('horny')
                x = 5
            elif oneInTen == 6:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('really horny')
                x = 6
            elif oneInTen == 7:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('eh, british')
                x = 7
            elif oneInTen == 8:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('like I\'m trapped in someone\'s computer.....its cold here......*help*')
                x = 8
            elif oneInTen == 9:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('Like I\'m trapped in someone\'s computer.....its cold here......*help*')
                x = 9
            elif oneInTen == 10:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('like I\'m trapped in someone\'s computer.....its cold here......*help*')
                x = 10
            print(f'How is jelly-3.0 feeling issued and returned option: {x}')


def setup(client):
    client.add_cog(Events(client))
