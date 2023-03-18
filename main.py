import os
import discord
from discord.ext import commands
import asyncio
import keep_alive
import datetime
from bs4 import BeautifulSoup
import urllib3
import re
import random
import requests

client = discord.Client()
token = os.getenv('DISCORD_BOT_SECRET')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
  if message.author == client.user:
      return
  if message.content.startswith('$hello'):
      await message.channel.send('Hello!')





async def my_background_task():
    await client.wait_until_ready()
    channel = client.get_channel(950867986120577026)
    while not client.is_closed():
        now = datetime.datetime.now()
        if now.hour == 21 and now.minute == 00:
          await channel.send('Good night <@487010330304577565>!')
        if now.hour == 7 and now.minute == 00:
          await channel.send('Good morning <@487010330304577565>!')
        if now.weekday() == 2 and now.hour == 14 and now.minute == 45:
          allowed_mentions = discord.AllowedMentions(everyone = True)
          await channel.send(content = "@everyone" + " Math Contest Club is right now!", allowed_mentions = allowed_mentions)
        if now.weekday() == 4 and now.hour == 14 and now.minute == 45:
          allowed_mentions = discord.AllowedMentions(everyone = True)
          await channel.send(content = "@everyone" + " Computer Science Club is right now!", allowed_mentions = allowed_mentions)
        await asyncio.sleep(59) # task runs every 59 seconds

client.loop.create_task(my_background_task())
#client.run(os.environ['DISCORD_TOKEN'])
keep_alive.keep_alive()
client.run(token)
