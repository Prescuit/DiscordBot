import os
import discord
import json
from data.constants import GlobalConstants
from classes.reddit_class import FetchReddit
from scripts.api.apex_status_api import getStatus
from scripts.build_embed import buildApexStatus

async def handleMessage(message, class_list, command_list):
  msg = str(message.content).lower()
  if len(msg) == 0:
    return

  if msg[:5] == "!apex":
    status = getStatus()
    #with open('data/test.json') as f:
      #status = json.load(f)
    embedVar = buildApexStatus(status)
    await message.channel.send(embed=embedVar)

  elif msg[:2] == "!r":
    nsfw_post = True
    post = FetchReddit(msg[3:])
    if message.author.id == int(os.environ.get("JOSH_ID")):
      nsfw_post = False
    response = await post.getTopPost(nsfw_post)
    await message.channel.send(response)

  elif msg[0] == GlobalConstants.COMMAND_PREFIX:
    is_command = False
    for x in command_list:
      if msg[1:] == x.name:
        is_command = True
        bot_msg = await x.execute()
        await message.channel.send(bot_msg)
        break
    if not is_command:
      if message.author.id == int(os.environ.get("JOSH_ID")):
        await message.channel.send("That's not a command, Josh")
        for x in class_list:
          if "dm" == x.name:
            reply = x.execute()
            await message.channel.send(reply)
            break
      else:
        await message.channel.send("Sorry, that's not a command")
  else:
    for x in class_list:
      if msg == x.name:
        await message.channel.send(x.execute())
        break

  #e = discord.Embed(color=discord.Color.blurple(), description='')
 # for page in command_list:
    #  e.description += page.name