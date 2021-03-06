import os
import discord
import datetime
from keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(
	command_prefix="!",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = os.environ.get("DISCORD_ID")   # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Kenny G"))


extensions = [
	'cogs.cog_example'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if not message.guild:
      print(message.content)
      f = open("console.log", "a")
      f.write("\n"+"["+str(datetime.datetime.now())+"] - "+str(message.author)+": "+message.content)
      f.close()
      await message.channel.send(message.content + " - " + str(message.author))
      return

    if message.content == '!awakebot':
        response = 'https://tenor.com/3YVH.gif'
        await message.channel.send(response)


keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)  # Starts the bot