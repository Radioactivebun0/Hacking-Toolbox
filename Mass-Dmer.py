import discord
import time
import random
import string
from discord.utils import get
from discord.ext import commands
import asyncio
import requests
from requests import post
def SpamSetUp():
    global inv
    global messagecount
    global messagesend
    inv=input("what is the invite link (just the string of letters or enter nothing if they are already in): ")

    link = "https://discord.com/api/v6/invites/" + inv.split("/")[-1]
    joined = 0
    failed = 0
    with open("tokens.txt", "r") as f:
        tokens = f.read().splitlines()
        for token in tokens:
            headers = {"Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
                    "Authorization" : token}

            response = post(link, headers=headers).status_code
            if response > 199 and response < 300:
                joined += 1

            else:
                failed += 1

        print("Accounts that joined: "+str(joined))
        print("Accounts that could not join: "+str(failed))
    
    print("-----")
    
    messagecount=input("how many messages should each user send (must be integer): ")

    messagesend = input("type what you want the bots to spam here: ")

def randomletters(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

time.sleep(2)

with open("tokens.txt", "r") as f:
    tokens = f.read().splitlines()

class multibot(commands.Cog):
    global client
    def __init__(self, client):
        self.client=client

    @commands.Cog.listener()
    async def on_message(self,message):
        await client.process_commands(message)
        print(message.content)
        #triggerwords = ['hi', 'this', 'is', 'cool']
        #for x in triggerwords:
         #   if x in message.content:
        try:
            print('Sending the dm 👋 "Why, hello there 👋"...')
            await message.author.send('👋 Why, hello there 👋')
            print('Done')
        except:
            pass


    @commands.command()
    async def spam(self,ctx):
        global inv
        global messagecount
        global messagesend
        x=0
        for x in range(0,int(messagecount)):
            asyncio.sleep(0.7)
            print("sending message "+random.choice(string.ascii_letters))
            try:
                await ctx.send(messagesend)
            except:
                print("message error")
                pass
            x=x+1

    @commands.command()
    async def massroleping(self,ctx):
        guild = ctx.guild
        print(f'pinging {len(guild.roles)} roles...')
        for role in guild.roles:
            if str(role) == '@everyone':
                print(f'bybassing {role}')
                pass
            print(f'role: {role} ping: {role.mention}')
            await ctx.send(role.mention)

    @commands.command()
    async def massuserping(self,ctx):
        guild = ctx.guild
        print(f'pinging {len(guild.members)} users...')
        for member in guild.members:
            print(f'user: {member} ping: {member.mention}')
            await ctx.send(member.mention)

    @commands.command()
    async def dmall(self, ctx, *, message):
        for member in ctx.guild.members:
            await member.send(message)

    @commands.command()
    async def stop(self,ctx):
        exit(0)
            
loop = asyncio.get_event_loop()
for i in range(len(tokens)):
    global client
    client = commands.Bot(command_prefix="-",fetch_offline_members=False,self_bot=False)
    client.add_cog(multibot(client))
    loop.create_task(client.start(tokens[i], bot=False))

SpamSetUp()

loop.run_forever()

