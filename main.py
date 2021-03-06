import os
import discord
import datetime
import random
import json
from keep_alive import keep_alive
from discord.ext import commands
from scripts.channel_msg import *

bot_client = commands.Bot(command_prefix="!")
@bot_client.command()
async def load(ctx, extension):
    bot_client.load_extension(f'cogs.{extension}')

bot.author_id = os.environ.get("DISCORD_ID")   # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Kenny G"))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = str(message.content).lower()

    if not message.guild:
      print(message.content)
      f = open("console.log", "a")
      f.write("\n"+"["+str(datetime.datetime.now())+"] - "+str(message.author)+": "+message.content)
      f.close()
      await message.channel.send(message.content + " - " + str(message.author))
      return

    if 'f' in msg:
        aFoo(msg)
        with open('data/data.json') as f:
            data = json.load(f)
        i = random.randint(0, len(data['f'])-1)
        response = data['f'][i]
        await message.channel.send(response)
    #elif message.content =

keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)  # Starts the bot