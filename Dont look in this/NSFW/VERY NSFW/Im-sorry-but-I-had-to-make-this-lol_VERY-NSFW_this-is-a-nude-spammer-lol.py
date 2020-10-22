import discord
import time
import random
import string
from discord.utils import get
from discord.ext import commands
import asyncio
import requests
from requests import post
import nekos

def SpamSetUp():
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

with open("tokens.txt", "r") as f:
    tokens = f.read().splitlines()

class multibot(commands.Cog):
    """nfsw messages"""

    def __init__(self, client):
        self.client=client

    @commands.command()
    async def neko(self, ctx, message):
        global x
        """Shows hentai"""
        #await ctx.delete()
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        msg = message
        embed = discord.Embed(
            title=":flushed:", description="", colour=discord.Colour.from_rgb(r, g, b),
        )
        url = nekos.img(msg)
        embed.set_image(url=url)
        try:
            await ctx.send(embed=embed)
        except:
            await ctx.send(url)

    @commands.command()
    async def nekoalt(self, ctx):
        """Shows all options for neko"""
        #await ctx.delete()
        possible = [
            "**Feet** | **Yuri** | **Trap** | **Futanri** | **Hololewd** | **Lewdkemo** | **Solo** | **Feet** | **Cum** | **Erokemo** | **Les** | **Wallpaper** | **Lewd** | **Feed** | **Gecg** | **Femdom** | **Eroyuri** | **Eron** | **Blowjob** | **Kemonomimi** | **Gasm** | **Anal** | **Erok** | **Boobs** | **Smallboobs** | **Spank** | **Hentai** | **Holo** | **Keta** | **Pussy** | **Tits** | **Classic** | **Kuni** | **Waifu** | **Pat** | **Poke** | **Neko** | **Cuddle** | **Kiss** | **Baka** | **Smug**",
        ]

        list = ""
        for item in possible:
            list += f"{item}\n"
        r = random.randint(50, 255)
        g = random.randint(50, 255)
        b = random.randint(50, 255)
        embed = discord.Embed(
            title=":flushed: options:", description=f"{list}", colour=discord.Colour.from_rgb(r, g, b),
        )
        await ctx.send(embed=embed)

loop = asyncio.get_event_loop()
for i in range(len(tokens)):
    global client
    client = commands.Bot(command_prefix="-",fetch_offline_members=False,self_bot=False)
    client.add_cog(multibot(client))
    loop.create_task(client.start(tokens[i], bot=False))

SpamSetUp()

loop.run_forever()