import discord
import random
from discord.ext import commands
import json

names = ["Krishin", "Dominick"]
lolnames = ["Ayuush", "Ayush"]

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def handbook(self,ctx):
        await ctx.send("**The student handbook is a very prestigious, important book. Do you choose to accept?**")

    @commands.command(brief="Tells you if you are smart")
    async def isSmart(self, ctx, name):
        if(name in names):
            await ctx.send("**"+name + " is totally smart**")
        elif(name==None):
            await ctx.send("Please enter a name")
        elif(name in lolnames):
            await ctx.send("**"+name + " is not smart, but his mum still sort of**")
        else:
            await ctx.send("**"+name + " is sort of smart*")
    @commands.command()
    async def rules(self, ctx, index):
        await ctx.send("There are no rules")
  
