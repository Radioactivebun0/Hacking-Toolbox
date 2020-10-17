import time
from selenium import webdriver
from DiscordAccount import DiscordAccount
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from LocalStorage import LocalStorage
from sys import argv
import sys

useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": useragent.random})
print(driver.execute_script("return navigator.userAgent;"))

def savedata():
    print('Saving data...')
    with open('tokens.txt', 'a') as a:
        a.write(account.token)
        a.write('\n')
    with open('username_and_passwords.txt', 'a') as a:
        a.write('Account details: Username: ' + account.username + ' Email: ' + account.email + ' Password: ' + account.password + ' Token: ' + account.token)
        a.write('\n')

def token():
    print('Getting the token...')
    l_storage = LocalStorage(driver)
    token = l_storage.get("token")
    token = token[1:-1]
    account.token = token
    print('Account details: Usermame: ' + account.username + ' Email: ' + account.email + ' Password: ' + account.password  + ' Token: ' + account.token)
    savedata()

def claim_account():
    x = 0
    print('Enter a random data lol')
    date_enter_button = driver.find_element_by_xpath('//*[@id="app-mount"]/div[6]/div[2]/div/div/div[2]/div/div/div/form/div[4]/div/button')
    if date_enter_button.is_enabled() == True:
        try:
            print()
            date_enter_button.click()
            print('Entered the date')
            claim_account1()
        except:
            print('Retrying')
            time.sleep(1)
            claim_account()
    else:
        if x == 0:
            print('The button is not visible, enter a date.')
            claim_account()
            x = 1
        else:
            time.sleep(0.1)
            claim_account()

def claim_account1():
    try:
        the_x = driver.find_element_by_xpath('//*[@id="app-mount"]/div[6]/div[2]/div/div/div[2]/button')
        the_x.click()
        print('xing that')
        claim_account2()
    except:
        print('Retrying')
        time.sleep(1)
        claim_account1()

def claim_account2():
    try:
        claim_email = driver.find_element_by_xpath('//*[@id="app-mount"]/div[6]/div[2]/div/div/div[2]/form/div[1]/div/input')
        claim_email.send_keys(email)
        time.sleep(2)
        claim_password = driver.find_element_by_xpath('//*[@id="app-mount"]/div[6]/div[2]/div/div/div[2]/form/div[2]/div/input')
        claim_password.send_keys(password)
        time.sleep(2)
        Claim_Account = driver.find_element_by_xpath('//*[@id="app-mount"]/div[6]/div[2]/div/div/div[2]/form/button')
        Claim_Account.click()
        print('Claimed account')
        time.sleep(5)
        claim_account3()
    except:
        print('Retrying')
        time.sleep(1)
        claim_account2()

def claim_account3():
    trys = 0
    try:
        if trys == '5':
            print('Error... Geting the token')
            token()
        else:
            trys = trys + 1
            print('xing that')
            the_second_x = driver.find_element_by_xpath('//*[@id="app-mount"]/div[6]/div[2]/div/div/div[2]/button')
            the_second_x.click()
            print('xed that')
            token()
    except:
        print('Retrying')
        time.sleep(1)
        claim_account3()

cap = 0
claim = 'false'

argument_list = argv[1:]
if len(argument_list) > 0 and argument_list[0] == "claim_account":
    claim = 'true'
    print("Will claim the account")

if len(argument_list) == 0:
    print('Will not claim the token')

if len(argument_list) > 0 and argument_list[0] == 'help':
    print('use py Auto_alt_maker claim_account to claim the account it gennerates otherwise it will no claim the account')
    exit(0)

account = DiscordAccount()
account.generate_random_credentials()
username = account.username
email = account.email
password = 'Soccer0127'
print("Makeing alt: " + username + " Email: " + email +
      " Password: " + password)

driver.get('https://discord.com/')
time.sleep(5)

Open_discord_in_your_browser = driver.find_element_by_xpath('//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/button')
Open_discord_in_your_browser.click()
time.sleep(5)
Enter_a_username = driver.find_element_by_xpath('//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/form/input')
Enter_a_username.send_keys(username)
time.sleep(5)
Enter_a_username_confurm_button = driver.find_element_by_xpath('//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/form/button')
Enter_a_username_confurm_button.click()
while driver.current_url == 'https://discord.com/':
    if cap == 0:
        print('You need to do the captia')
        time.sleep(1)
        cap = 1
    else:
        time.sleep(1)
if claim == 'true':
    print('Claiming the account')
    time.sleep(5)
    claim_account()
else:
    account.email = 'There is no account email, this is not a claimed account'
    account.password = 'There is no account password, this is not a claimed account'
    print('Done')
    token()