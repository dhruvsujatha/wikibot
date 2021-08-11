import discord
from discord.ext import commands
import ssis
import os
from dotenv import load_dotenv, find_dotenv
from datetime import datetime, timedelta
import pytz

PREFIX = '!'
EDT = pytz.timezone('US/East-Indiana')

bot = commands.Bot(command_prefix=PREFIX, help_command = None)

@bot.event
async def on_ready():
  activity = discord.Activity(name='!| Learn!', type=discord.ActivityType.watching)
  await bot.change_presence(activity=activity)
  print('We have logged in as {0.user}'.format(bot))

@bot.command()  
async def test(ctx):
  await ctx.send("```Tested Positive! Wait No....```")

@bot.command()
async def search(ctx, keyword):
    result = ssis.wikiSearch(keyword)
    if result["suggest"] == True:
        embed = discord.Embed(title = "Oops!", description = "We couldn't find your term, here is a suggestion", color = 0x02fa5d, timestamp = datetime.now(EDT))
        embed.set_author(name = 'Wikipedia and Dhruv')
        embed.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/220px-Wikipedia-logo-v2.svg.png")
        embed.add_field(name = result["result"][0], value='If this is what you meant, search again with that term.')
        embed.set_footer(text = "Wikipedia (/ˌwɪkɨˈpiːdiə/ or /ˌwɪkiˈpiːdiə/ WIK-i-PEE-dee-ə) is a collaboratively edited, multilingual, free Internet encyclopedia supported by the non-profit Wikimedia Foundation...")
        await ctx.send(embed = embed)
    elif result["search"] == True:
        embed = discord.Embed(title = "Exact Term Finder Running!", description = "A single can have many meanings. To Get you accurate information, choose a topic from the list below", color = 0x02fa5d, timestamp = datetime.now(EDT))
        embed.set_author(name = 'Wikipedia and Dhruv')
        embed.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/220px-Wikipedia-logo-v2.svg.png")
        embed.set_footer(text = "Wikipedia (/ˌwɪkɨˈpiːdiə/ or /ˌwɪkiˈpiːdiə/ WIK-i-PEE-dee-ə) is a collaboratively edited, multilingual, free Internet encyclopedia supported by the non-profit Wikimedia Foundation...")
        for i in result["result"][0]:
            embed.add_field(name = i, value = '?')
        embed.add_field(name = "Pick", value = "a term from the above")
        await ctx.send(embed = embed)
    elif result["summary"] == True:
        embed = discord.Embed(title = keyword, description = "Short Summary", color = 0x02fa5d, timestamp = datetime.now(EDT))
        embed.set_author(name = "Wikipedia and Dhruv")
        embed.add_field(name = keyword, value = result["result"][0])
        if result["image"] == True:
            embed.set_thumbnail(url = result["result"][1] + '.png')
        else:
            embed.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/220px-Wikipedia-logo-v2.svg.png")
        embed.set_footer(text = "Wikipedia (/ˌwɪkɨˈpiːdiə/ or /ˌwɪkiˈpiːdiə/ WIK-i-PEE-dee-ə) is a collaboratively edited, multilingual, free Internet encyclopedia supported by the non-profit Wikimedia Foundation...")
        await ctx.send(embed = embed)
load_dotenv(find_dotenv())
bot.run(os.getenv("TOKEN"))