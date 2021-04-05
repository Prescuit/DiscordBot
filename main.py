import os
import discord
import json
from keep_alive import keep_alive
from discord.ext import commands

#local imports
from scripts.channel_msg import handleMessage
from scripts.direct_msg import handleDMMessage
from classes.reaction_class import ReactionClass
from classes.reddit_class import FetchReddit
from scripts.log import logMessage

bot = commands.Bot(command_prefix="!")

with open('data/response.json') as f:
    data = json.load(f)
class_list = []
for key in data:
    class_list.append(ReactionClass(key, data[key]))

command_list = []
with open('data/commands.json') as f:
    data = json.load(f)
for sub in data['reddit']:
    command_list.append(FetchReddit(sub))

bot.author_id = os.environ.get("DISCORD_ID")

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Kenny G"))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    try:
      if not message.guild:
        await handleDMMessage(message, class_list, command_list, bot)
        return
      else:
        await handleMessage(message, class_list, command_list)
    except Exception as e:
      err = "\nAn exception occured: " + str(e)
      logMessage(err)
      print(err)


keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)  # Starts the bot