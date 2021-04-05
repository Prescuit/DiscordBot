import datetime
import os
from discord import DMChannel
from scripts.log import logMessage
from classes.reddit_class import FetchReddit
from data.constants import GlobalConstants

subreddit = []

async def getResponse(msg):
  default_subs = ["Aww", "Cats"]
  sub = []
  return_posts = []

  if len(msg) == 0:
    for s in default_subs:
      sub.append(FetchReddit(s))
      subreddit.append(s)
  elif msg[0] == "g":
    sub.append(FetchReddit(msg[2:]))
    subreddit.append(msg[2:])
  elif msg.isnumeric:
    sub.append(FetchReddit(default_subs[int(msg)]))
    subreddit.append(default_subs[int(msg)])

  for x in sub:
    y = await x.getTopPost(True)
    return_posts.append(y)

  return return_posts

async def sendLogs(msg):
  textfile = open("data/logs.txt")
  lines = textfile.readlines()
  if GlobalConstants.LINE_BREAK in lines[len(lines)-1]:
    await msg.channel.send('No new logs')
  else:
    for line in reversed(lines):
      if GlobalConstants.LINE_BREAK in line:
        break
      await msg.channel.send(line)
    logMessage("\n"+GlobalConstants.LINE_BREAK)

async def adminDM(message, bot):
  if message.content[:2] == GlobalConstants.SEND_IT:
    #get Josh's user id
    user = await bot.fetch_user(str(os.environ.get("JOSH_ID")))
    #get posts
    posts = await getResponse(message.content[3:])
    
    i = 0
    for x in posts:
      await DMChannel.send(user, x)
      await DMChannel.send(user, "post from r/"+subreddit[i])
      i+=1
      #await message.channel.send(x)
    await message.channel.send("Message has been sent")
    
  elif message.content[:2] == GlobalConstants.PREVIEW:
    posts = await getResponse(message.content[3:])

    await message.channel.send("Would you like to send this?")
    i = 0
    for x in posts:
      await message.channel.send(x)
      await message.channel.send("post from r/"+subreddit[i])
      i+=1

  elif message.content.lower() == "logs":
    await sendLogs(message)
  else:
    await message.channel.send("Ping!")
  #cleanup
  subreddit.clear()

async def handleDMMessage(message, class_list, command_list, bot):
  logs = ""
  if len(message.content) == 0:
    return

  if message.author.id == int(os.environ.get("R_USER_ID")):
    await adminDM(message, bot)
  else:
    logs = "\n"+"["+str(datetime.datetime.now())+"] - "+str(message.author).split('#')[0]+": "+message.content
    for x in class_list:
      if "dm" == x.name:
        reply = x.execute()
        logs = logs + "\nBOT-Response: " + reply
        await message.channel.send(reply)
        break

  logMessage(logs)