import discum

def login():
    bot = discum.Client(token='Your token here')
    test()

def test():
    t = bot.getGuilds(update=True)
    print(t)
    bot.getGuilds(update=False)

login()
