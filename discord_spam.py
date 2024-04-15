import discord
from discord.ext import commands
import os
import asyncio

import spam 

from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.all()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await asyncio.sleep(1)
    # to check if the bot is working
    # output in cmd window
    print(message)
    print("------------------------------------")
    print(message.content)
    print("------------------------------------")
    if message.content!="":
        if spam.check_spam(message.content) == 'spam': 
            await message.reply("Your message is considered spam.")

client.run(os.getenv('SECOND_BOT_TOKEN'))