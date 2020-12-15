import discord
from discord.ext import commands

async def spam_filter(msg1,msg2):
    if msg1.content != msg2.content:
        if msg1.author == msg2.author:
            if ((msg1.created_at - msg2.created_at).seconds) > 2:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

class SpamFilter(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
     
    @commands.Cog.listener()
    async def on_message(self,msg):
        messages = await msg.channel.history(limit=2).flatten()
        if await spam_filter(messages[0], messages[1]) == True:
            await msg.channel.send("Go ahead") #person is not spamming.
        else:
            await msg.channel.send("Spammer Begone") #getting False as return means spam is detected.

def setup(bot):
    bot.add_cog(SpamFilter(bot))