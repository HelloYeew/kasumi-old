# Copyright (c) HelloYeew <me@helloyeew.dev>. Licensed under the MIT Licence.
# See the LICENCE file in the repository root for full licence text.

from kasumiframework.make_bot import *
from kasumiframework.log import *
from kasumiframework.localization import *
from kasumiframework.embed import *

# Bot configuration

bot_token = ""
bot_presence = True
bot_presence_status = "Kasumi"
prefix = '!'
presence = True

bot_log = True
logfile_locate = "logs/main.log"
log_filemode = 'w'
loglevel = 'debug'
GMTTime = True

intents = discord.Intents.default()
intents.members = True

# End configuration

if bot_log:
    set_log(logfile=logfile_locate, filemode=log_filemode, level=loglevel, gmtime=GMTTime)

th = new_language('th')
bot = commands.Bot(command_prefix=prefix)


# TODO: Add licenseheader command

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(bot_presence_status))


@bot.command()
async def test(ctx):
    """I'm genius!"""
    await ctx.send('Test')
    await ctx.send(th('Test'))


@bot.command()
async def embed(ctx):
    """I'm genius!"""
    await ctx.send(embed=new_embed())


bot.run(bot_token)
