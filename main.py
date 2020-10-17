import os
import time

def home():
    os.system('cls')
    print('RadioActivebun0s Toolbox:')
    print('[01] Discord Spamming Tool(SelfBot)')
    print('[02] Discord Alt and token generator')
    print('[03] Discord Token Checker')
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
        print('Launching Discord Token Checker...')
        TKC()
    elif op == '99':
        print('Exiting...')
        quit()
    else:
        print('Please enter a vaild input')
        home()

def DST():
    os.system('py Mass-Dmer.py')
    home()

def ALTM():
    print('Do you want to save the account?')
    s = input('> ')
    if s == 'y' or s == 'yes':
        os.system('py alt_maker.py claim-account')
    elif s == 'n' or s == 'no':
        os.system('py alt_maker.py')
    elif s == 'h' or s == 'help':
        os.system('py alt_maker.py help')
    else:
        print('please anser yes or no')
        home()
    home()

def TKC():
    os.system('py token-filter.py')
    time.sleep(5)
    home()

if __name__ == '__main__':
    def noclose():
        try:
            home()
        except KeyboardInterrupt:
            print('Interrupted')
            noclose()
    noclose()
