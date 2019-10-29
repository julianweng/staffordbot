import discord
async def snd(bob,message):
    await message.channel.send(bob)
messages = {"help": [snd,"Hey student! Make sure to swipe right!"],
            "ping": [snd,"pong"],
            "screw you": [snd,"no you"]
}

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if("s." in message.content):
            bruh = message.content.replace('s.','')
            print(bruh)
            for key in messages:
                if (bruh == key):
                    await messages[key][0](messages[key][1],message)
                    # await message.channel.send(messages[key])


client = MyClient()
client.run('NjM0MTAyMDgwNzkzMjE1MDIy.XadoDw.6nFelnwqXln8JvVDyHLnvFeiMb8')