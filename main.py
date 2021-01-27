from check import *

# check requirement
check_library()

# import requirement
from genius_command import *
from tenor import *

# before run please don't forget to put bot token

description = "All Kasumi command is here"

# put all API key and bot token here

bot_token = 'bot_token'
tenor_token = "tenor_token"

# You can change your prefix here

prefix = "!"

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=prefix, description=description, intents=intents, help_command=None)


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
    """I'm genius!"""
    await ctx.send("I'm online and I'm genius!")


@bot.command()
async def pfp(ctx):
    author = ctx.message.author
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.title = "This is"
    embed.description = "Your profile image"
    # embed.colour = "#FF5522"
    embed.set_author(name=author.display_name, url="https://youtu.be/dQw4w9WgXcQ", icon_url=author.avatar_url)
    embed.set_thumbnail(url=author.avatar_url)
    await ctx.send(embed=embed)


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


@bot.command()
async def repeat(ctx, text: str, time: int):
    """Repeat a message x times"""
    for i in range(time):
        await ctx.send(text)


# help command

@bot.command()
async def help(ctx):
    help = '''
    **General Command**
    - !pfp : Sender's profile picture
    - !genius : I'm genius! (Test Command)
    - !repeat (text_or_sth) (x) : Spam a text x time(s)
    
    **Genius Command**
    - !roots2 (float_x^1) (float_x^0) : Calculate a roots of one-dimension polynomial (two numbers)
    - !roots3 (float_x^2) (float_x^1) (float_x^0) : Calculate a roots of one-dimension polynomial (three numbers)
    '''
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.title = "❓ Help"
    embed.description = help
    await ctx.send(embed=embed)


# genius command zone

@bot.command()
async def roots2(ctx, n1: float, n2: float):
    """Root an poly"""
    author = ctx.message.author
    num = [n1, n2]
    answer = numpy.roots(num)
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.set_author(name=author.display_name, url="https://youtu.be/dQw4w9WgXcQ", icon_url=author.avatar_url)
    embed.title = "🧮 Calculation"
    # embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/762347346993348659/335e22e0f77a6bb717502981f57221e2.png")
    embed.description = "A roots of one-dimension polynomial (two numbers)"
    embed.add_field(name="Input", value=str(numpy.poly1d(num)), inline=False)
    embed.add_field(name="Results", value=str(answer), inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def roots3(ctx, n1: float, n2: float, n3: float):
    """Root an poly"""
    author = ctx.message.author
    num = [n1, n2, n3]
    answer = numpy.roots(num)
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.set_author(name=author.display_name, url="https://youtu.be/dQw4w9WgXcQ", icon_url=author.avatar_url)
    embed.title = "🧮 Calculation"
    # embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/762347346993348659/335e22e0f77a6bb717502981f57221e2.png")
    embed.description = "A roots of one-dimension polynomial (three numbers)"
    embed.add_field(name="Input", value=str(numpy.poly1d(num)), inline=False)
    embed.add_field(name="Results", value=str(answer), inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def roots4(ctx, n1: float, n2: float, n3: float, n4: float):
    """Root an poly"""
    author = ctx.message.author
    num = [n1, n2, n3, n4]
    answer = numpy.roots(num)
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.set_author(name=author.display_name, url="https://youtu.be/dQw4w9WgXcQ", icon_url=author.avatar_url)
    embed.title = "🧮 Calculation"
    # embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/762347346993348659/335e22e0f77a6bb717502981f57221e2.png")
    embed.description = "A roots of one-dimension polynomial (four numbers)"
    embed.add_field(name="Input", value=str(numpy.poly1d(num)), inline=False)
    embed.add_field(name="Results", value=str(answer), inline=False)
    await ctx.send(embed=embed)


# tenor command zone

@bot.command()
async def gif(ctx, word: str):
    """Return first GIF search result"""
    try:
        result = tenor(tenor_token, word, 1)
        if result is not None:
            embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
            embed.title = f"🔎 Result of GIF search '{word}'"
            embed.description = f"First GIF search result of *{word}*"
            embed.set_image(url=result)

        else:
            embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
            embed.title = f"🥲 No result of GIF search '{word}'"
            embed.description = "Sad"
        await ctx.send(embed=embed)
    except:
        await ctx.send("🔎 No search result!")


bot.run(bot_token)
