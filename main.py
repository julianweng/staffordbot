import discord
import random
from discord.ext import commands
import json


bot = commands.Bot(command_prefix='s.')
names = ["Krishin", "Dominick"]
lolnames = ["Ayuush", "Ayush"]
# triviaVal = {
#     "What is the golden rule of Staples High School?":["Swipe Right","Don't litter","Bully Dom","Get As in all ur classes"],
#     "What is the color of a fire hydrant?":["Red","Green","Blue","Purple"],
#     "Who is the principal of Staples High School?":["Stafford Thomas","Stafford Thompson","Sammy Thompson","Coleen Palmer"],
#     "What was the biggest problem in Staples High School?":["Old furniture","Coleytown mold refugees","Inconsistant grading standards","Cramped facilities"],
#     "Who will win homecoming?":["Not us!","Us!"],
#     "What is the easiest AP?":["APCSP","APUSH","AP Chemistry", "AP Biology","AP Stat", "AP Music Theory"],
#     "What is the most popular IO game in the library?":["surviv.io","shellshockers.io","agar.io","slither.io","bonk.io"],
#     "What Staples extracurricular is the best?":["Coding club","Science Olympiad","Nonfiction Reading Club","Esports Club"]
# }
with open('trivias.json', 'r') as fp:
    triviaVal = json.load(fp)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def hey(ctx):
    await ctx.send("Hey student! Make sure to swipe right!")

@bot.command()
async def handbook(ctx):
    await ctx.send("**The student handbook is a very prestigious, important book. Do you choose to accept?**")

@bot.command()
async def isSmart(ctx, name):
    if(name in names):
        await ctx.send("**"+name + " is totally smart**")
    elif(name==None):
        await ctx.send("Please enter a name")
    elif(name in lolnames):
        await ctx.send("**"+name + " is not smart, but his mum still sort of**")
    else:
        await ctx.send("**"+name + " is sort of smart*")

@bot.command()
async def trivia(ctx):
    boi = random.choice(list(triviaVal.keys()))
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

    msg = await bot.wait_for('message',check=check)
    ans = msg.content # Set the title
    print("You entered "+str(ans))
    print("The right answer is " + str(rightIndex))
    if(ans == str(rightIndex)):
        await ctx.send("Right!")
    else:
        await ctx.send("Wrong!")

@bot.command()
async def debug(ctx):
    print(triviaVal)
    await ctx.send("check the console.")


@bot.command()
async def rules(ctx, index):
    await ctx.send("There are no rules")


bot.run('NjM0MTAyMDgwNzkzMjE1MDIy.XadoDw.6nFelnwqXln8JvVDyHLnvFeiMb8')