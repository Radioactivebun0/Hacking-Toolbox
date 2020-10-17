import discum
import time
import os

bot = discum.Client(token='NzY2NzU1NTM5MTIzMzA2NTQ4.X4n_Fg.g4UrMo7JSY4tDFak7ekIrle9jmU')

guildnum = 0

def home():
    print('Discord Toolbox by RadioactiveBun0')
    print('[01] Discord Friend Spammer')
    print('[02] Discord Guild Grabber')
    print('----------------------------------')
    print('[99] Exit')
    ch = input('> ')
    if ch == '01':
        global s
        global t
        global intt
        global ChatId
        global guild
        global x
        global xx
        x = 0
        xx = 0
        os.system('cls')
        print('whats the chat id?')
        ChatId = input('> ')
        print('what do you want to say?')
        s = input('> ')
        print('how many times?')
        t = input('> ')
        try:
            intt = int(t)
        except:
            print('Please give a number')
            exit()
        spam()
    elif ch == '02':
        os.system('cls')
        guild = bot.getGuilds(update=True)
        print('Getting guilds...')
        GetAllGuilds()
    elif ch == '03':
        global guildnumber
        global guildnumberloop
        os.system('cls')
        print('What is the guild number')
        guildnumber = input('> ')
        guildnumberloop = 0
        GetUserData()
    elif ch == '99':
        print('Exiting...')
        quit()
    else:
        print('Please enter a vaild input')

def GetAllGuilds():
    global guildnum
    global guild
    try:
        gn = guild[guildnum]['name']
        gid = guild[guildnum]['id']
        print(f'Guild name: {gn} Guild id: {gid} Guild number: {guildnum}')
        guildnum += 1
        GetAllGuilds()
    except:
        print('Done')
        home()

#def Getpingableroles():
 #

def GetUserData():
    global guild
    global guildnumber
    global guildnumberloop
    try:
        gn = guild[int(guildnumber)]['members']
        GuildUserInfo = gn[guildnumberloop]#['user']
        print(GuildUserInfo)
        guildnumberloop += 2
        GetUserData()
    except:
        print('Done')

def spam():
    global x
    global xx
    global s
    global t
    if xx == intt:
        print(f'sent {xx} messages')
        time.sleep(3)
        os.system('cls')
        home()
    elif x >= 10:
        print('sent 10 messages, waiting 10 seconds...')
        x = 0
        time.sleep(11)
        spam()
    else:
        print('sending message')
        bot.sendMessage(ChatId,s)
        x += 1
        xx += 1
        time.sleep(0.1)
        spam()

if __name__ == '__main__':
    def noclose():
        try:
            home()
        except KeyboardInterrupt:
            print('Interrupted')
            noclose()
    noclose()
