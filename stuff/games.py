import discord
import random
from discord.ext import commands
import json

with open('trivias.json', 'r') as fp:
    triviaVal = json.load(fp)

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @commands.command(brief="Gives you a trivia question regarding Staples High School")
    async def trivia(self,ctx):
        if("past" not in locals() and "past" not in globals()):
            past = "baloney"
        boi = random.choice(list(triviaVal.keys()))
        while(boi == past):
            boi = random.choice(list(triviaVal.keys()))
        past = boi
        st = ""
        thing = list(triviaVal[boi])
        print(thing)
        ruff = thing[0]
        print(ruff)
        rightIndex = 0
        random.shuffle(thing)
        for i in range(len(thing)):
            if(thing[i]==ruff):
                print(thing[i])
                rightIndex = i+1
            st = st+str(i+1)+". "+thing[i]+"\n"
        await ctx.send(boi+ "\n"+st)

        def check(self):
            # print(ctx.message.author)
            print(ctx.author)
            print(self.author)
            return (ctx.author == self.author)

        msg = await self.bot.wait_for('message',check=check)
        ans = msg.content # Set the title
        print("You entered "+str(ans))
        print("The right answer is " + str(rightIndex))
        if(ans == str(rightIndex)):
            await ctx.send("Right!")
        else:
            await ctx.send("Wrong!")