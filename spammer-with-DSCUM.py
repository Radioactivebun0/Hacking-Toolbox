import discum

def login():
    bot = discum.Client(token='NzY2NzU1NTM5MTIzMzA2NTQ4.X4n_Fg.g4UrMo7JSY4tDFak7ekIrle9jmU')
    test()

def test():
    t = bot.getGuilds(update=True)
    print(t)
    bot.getGuilds(update=False)

login()
