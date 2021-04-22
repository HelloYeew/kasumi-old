# Copyright (c) HelloYeew <me@helloyeew.dev>. Licensed under the MIT Licence.
# See the LICENCE file in the repository root for full licence text.

import discord
from discord.ext import commands
from kasumiframework.log import *
import inspect

bot_token = ...
bot_presence = False
bot_presence_status = "Kasumi"

logfile_locate = "logs/main.log"
log_filemode = 'w'
loglevel = 'notset'
GMTTime = True

bot = commands.Bot(command_prefix="!")


def start_bot(token,prefix='!',log=True, presence=True):
    global bot_presence, bot
    try:
        bot_presence = presence
        bot = commands.Bot(command_prefix=prefix)
        if log:
            prepare_log(logfile=logfile_locate,filemode=log_filemode,level=loglevel,gmtime=GMTTime)
        streaming = discord.Streaming(platform="Twitch", name="Dota 2",
                                      detail="Premieres March 25, only on Netflix.",
                                      url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                                      game="Dota 2")
        bot.change_presence(activity=streaming)
        bot.run(token)
    except:
        logging.exception('Run bot failed!')
        raise


def set_presence(status):
    global bot_presence_status
    bot_presence_status = status


def set_log(logfile="logs/main.log", filemode='a', level='notset', gmtime=True):
    global logfile_locate, log_filemode, loglevel, GMTTime
    logfile_locate = logfile
    log_filemode = filemode
    loglevel = level
    GMTTime = gmtime


@bot.command()
async def genius(ctx):
    """I'm genius!"""
    await ctx.send("I'm online and I'm genius!")


@bot.event
async def on_ready():
    streaming = discord.Streaming(platform="Twitch", name="Dota 2",
                                  detail="Premieres March 25, only on Netflix.",
                                  url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                                  game="Dota 2")
    await bot.change_presence(activity=streaming)


@bot.event
async def change_presence(ctx,text="Kasumi"):
    await bot.change_presence(activity=discord.Game(text))
    await ctx.send("Complete!")