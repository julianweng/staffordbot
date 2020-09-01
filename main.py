import discord
import random
from discord.ext import commands
import json
from stuff.info import *
from stuff.games import *

bot = commands.Bot(command_prefix='s.',description='StaffordBot - The only bot that helps you become a better Staples citizen!')

bot.add_cog(Info(bot))
bot.add_cog(Games(bot))

bot.run('banana') #placeholder token