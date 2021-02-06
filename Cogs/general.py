import yaml
import discord
import time
import asyncio
from discord.ext import commands

with open("config.yml", "r") as ymlfile:
    config = yaml.load(ymlfile, Loader=yaml.FullLoader)

botAdmin = {'278548721778688010', '376857933067321366'}


class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='ping')
    async def ping(self, context):
        client = self.client

        start = time.monotonic()
        message = await context.send('Pinging...')
        pingValue = (time.monotonic() - start) * 1000
        pingMsg = f'Latency: {int(pingValue)}ms'
        await message.edit(content=pingMsg)
        print(f'Ping command issued, Latency is {int(pingValue)}ms')

    @commands.command(name='shutdown')
    async def shutdown(self, context):
        client = self.client
        if context.author.id == 278548721778688010 or context.author.id == 376857933067321366:
            async with context.typing():
                await asyncio.sleep(2)
            await context.send('Ok, time for bed')
            print(f'{client.user} is shutting down...')
            await client.close()
        else:
            await context.send('Permission error')

    @commands.command(name='say')
    async def say(self, context, *, args):
        if context.author.id == 278548721778688010 or context.author.id == 376857933067321366:
            argsLength = len(args)
            async with await asyncio.sleep(0.05):
                await context.message.delete()
            if 0 < argsLength < 10:
                timer = 1
                async with context.typing():
                    await asyncio.sleep(timer)
                await context.send(args)
                print(f'say command issued, jelly-3.0 said: "{args}" with a typing timer of: {timer}')
            elif 10 < argsLength < 20:
                timer = 3
                async with context.typing():
                    await asyncio.sleep(timer)
                await context.send(args)
                print(f'say command issued, jelly-3.0 said: "{args}" with a typing timer of: {timer}')
            elif 20 < argsLength < 40:
                timer = 5
                async with context.typing():
                    await asyncio.sleep(timer)
                await context.send(args)
                print(f'say command issued, jelly-3.0 said: "{args}" with a typing timer of: {timer}')
            elif 40 < argsLength:
                timer = 8
                async with context.typing():
                    await asyncio.sleep(timer)
                await context.send(args)
                print(f'say command issued, jelly-3.0 said: "{args}" with a typing timer of: {timer}')
        else:
            await context.message.delete()
            await context.send('Permission Error')


def setup(client):
    client.add_cog(Utils(client))
