import discord
import time
import random
import string
from discord.utils import get
from discord.ext import commands
import asyncio
import requests
from requests import post

global autodm
global ftime
global stime
stime = 0
ftime = '0'
autodm = '1'

def SpamSetUp():
    global inv
    global messagecount
    global messagesend
    global thedm
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

    thedm = input('What do you want the dm on message to be? ')
    if thedm == '':
        thedm = '👋 Why, hello there 👋'

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
        global autodm
        global thedm
        global ftime
        await client.process_commands(message)
        print(f'In {message.guild}, {message.author.name} sent: {message.content}')
        if autodm == '1':
            #triggerwords = ['hi', 'this', 'is', 'cool']
            #for x in triggerwords:
                #if x in message.content:
                    try:
                        print(f'Sending the dm: {thedm}')
                        await message.author.send(thedm)
                        time.sleep(1)
                        print('Done')
                    except:
                        pass
              #  else:
                   # pass
        else:
            return

    @commands.command()
    async def spam(self,ctx,args1,args2):
        x=0
        for x in range(0,int(args2)):
            asyncio.sleep(0.7)
            print("sending message "+random.choice(string.ascii_letters))
            try:
                await ctx.send(args1)
            except:
                print("message error")
                pass
            x=x+1

  #  @commands.command()
   # async def dall(self,ctx, *, message):
    #    for member in get_all_members():
     #       #await member.send(message)
      #      print(member)

    @commands.command()
    async def spamuser(self,ctx,args1,args2,args3): #formate -spamuser {message} {ammount of times} {userid}
        x=0
        try:
            intargs2 = int(args2)
            intargs3 = int(args3)
        except:
            ctx.send('The formate is: -spamuser {message} {ammount of times} {userid}')
            return
        for x in range(0,intargs2):
            asyncio.sleep(0.7)
            print("sending message "+random.choice(string.ascii_letters))
            try:
                user = client.get_user(intargs3)
                await user.send(args1)#('👀')
            except:
                print("message error")
                pass
            x=x+1

    @commands.command()
    async def spamstart(self,ctx):
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
    async def stop(self,ctx):
        exit(0)

async def timer():
    global stime
    print('This is a one sec delay')
    if stime == 0:
        return
    else:
        stime = stime - 1
    await asyncio.sleep(1.5)
    await timer()

loop = asyncio.get_event_loop()
for i in range(len(tokens)):
    global client
    client = commands.Bot(command_prefix="-",fetch_offline_members=False,self_bot=False)
    client.add_cog(multibot(client))
    loop.create_task(client.start(tokens[i], bot=False))

SpamSetUp()

loop.run_forever()

