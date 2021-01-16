from check import *

# check requirement
check_library()

# import requirement
import discord
from discord.ext import commands
import random
from genius_command import *

# before run please don't forget to put bot token

description = '''All of Kasumi command is here.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.command()
async def genius(ctx):
    await ctx.send('กูฉลาดไอสัส อย่าเถียงกู')
    await ctx.send('https://tenor.com/view/saint-rock-head-shot-to-screen-smile-gif-19946978')

@bot.command()
async def pfp(ctx):
    author = ctx.message.author
    embed = discord.Embed(color=discord.Color.from_rgb(222,137,127))
    embed.title = "This is"
    embed.description = "Your profile image"
    # embed.colour = "#FF5522"
    embed.set_author(name=author.display_name, url="https://youtu.be/dQw4w9WgXcQ",icon_url=author.avatar_url)
    embed.set_thumbnail(url=author.avatar_url)
    await ctx.send(embed = embed)
    # add color!

@bot.command()
async def saint(ctx):
    while True:
        await ctx.send('https://tenor.com/view/saint-rock-head-shot-to-screen-smile-gif-19946978')

@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('ชั่ยๆ, status:{0.subcommand_passed} เอาแบบเบิ้มๆอะ คือลืออะ เหมือนเซ้นอะ'.format(ctx))

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

# genius command zone

@bot.command()
async def roots3(ctx, n1: float,n2: float,n3: float):
    """Root an poly"""
    author = ctx.message.author
    num = [n1,n2,n3]
    answer = numpy.roots(num)
    embed = discord.Embed(color=discord.Color.from_rgb(222,137,127))
    embed.set_author(name=author.display_name, url="https://youtu.be/dQw4w9WgXcQ", icon_url=author.avatar_url)
    embed.title = "🧮 Calculation"
    # embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/762347346993348659/335e22e0f77a6bb717502981f57221e2.png")
    embed.description = "A roots of one-dimension polynomial (three numbers)"
    embed.add_field(name="Input", value = str(numpy.poly1d(num)), inline=False)
    embed.add_field(name="Results", value = str(answer), inline=False)
    await ctx.send(embed=embed)

bot.run('DISCORD-TOKEN')