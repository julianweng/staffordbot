import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='s.')
names = ["Krishin", "Dominick"]
lolnames = ["Ayuush", "Ayush"]
triviaVal = {
    "What is the golden rule of Staples High School?":["Swipe Right","Don't litter","Bully Dom","Get As in all ur classes"],
    "What is Julian's favorite color?":["Red","Green","Blue","Purple"]
}
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
    thing = triviaVal[boi]
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

    def check(user):
        print(ctx.message.author)
        print(ctx.author)
        return (ctx.author == ctx.message.author)

    msg = await bot.wait_for('message',check=check)
    ans = msg.content # Set the title
    print(ans)
    print(rightIndex)
    if(ans == str(rightIndex)):
        await ctx.send("Right!")
    else:
        await ctx.send("Wrong!")

@bot.command()
async def rules(ctx, index):
    ctx.send("There are no rules")


bot.run('NjM0MTAyMDgwNzkzMjE1MDIy.XadoDw.6nFelnwqXln8JvVDyHLnvFeiMb8')