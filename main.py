import os
import time

def home():
    os.system("cls" if os.name == "nt" else "clear")
    print('RadioActivebun0s Toolbox:')
    print('[01] Discord Spamming Tool(SelfBot)')
    print('[02] Discord Alt and token generator')
    print('[03] Discord Email Verifier')
    print('[04] Discord Token Checker')
    print('[05] Discord Token Grabber')
    print('[06] Discord Token Login Tool')
    print('----------')
    print('[99] Exit')
    op = input('> ')
    if op == '01':
        print('Launching Discord Spamming Tool(SelfBot)...')
        DST()
    elif op == '02':
        print('Launching Discord Alt and token generator...')
        ALTM()
    elif op == '03':
        print('launching Discord Email Verifier...')
        DVF()
    elif op == '04':
        print('Launching Discord Token Checker...')
        TKC()
    elif op == '05':
        print('Launching Discord Token Grabber')
        DTG()
    elif op == '06':
        print('Launching Discord Token Login Tool')
        DTLT()
    elif op == '99':
        print('Exiting...')
        quit()
    else:
        print('Please enter a vaild input')
        print(op)
        home()
#cls" if os.name == "nt" else
def DST():
    os.system('py -3 Mass-Dmer.py' if os.name == "nt" else 'python3 Mass-Dmer.py')
    home()

def ALTM():
    print('Do you want to save the account?')
    s = input('> ')
    if s == 'y' or s == 'yes':
        #os.system('python3 alt_maker.py claim-account')
        os.system('py -3 alt_maker.py claim-account' if os.name == "nt" else 'python3 alt_maker.py claim-account')
    elif s == 'n' or s == 'no':
        os.system('py -3 alt_maker.py' if os.name == "nt" else 'python3 alt_maker.py')
        #os.system('python3 alt_maker.py')
    elif s == 'h' or s == 'help':
        os.system('py -3 alt_maker.py help' if os.name == "nt" else 'python3 alt_maker.py help')
        #os.system('python3 alt_maker.py help')
    else:
        print('please anser yes or no')
        home()
    home()

def DVF():
    os.system('py -3 email_variflyer.py' if os.name == "nt" else 'python3 email_variflyer.py')
    #os.system('python3 email_variflyer.py')
    home()

def DTG():
    os.system('py -3 Account-Token-grabber.py' if os.name == "nt" else 'python3 Account-Token-grabber.py')
    home()

def TKC():
    os.system('py -3 token-filter.py' if os.name == "nt" else 'python3 token-filter.py')
    #os.system('python3 token-filter.py')
    time.sleep(5)
    home()

def DTLT():
    os.system('py -3 Login-with-a-token.py' if os.name == "nt" else 'python3 Login-with-a-token.py')

if __name__ == '__main__':
    def noclose():
        try:
            home()
        except KeyboardInterrupt:
            print('Interrupted')
            noclose()
    noclose()
