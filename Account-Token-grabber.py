import time
from selenium import webdriver
from DiscordAccount import DiscordAccount
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from LocalStorage import LocalStorage
from sys import argv
import pyperclip
import sys

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

global email
global pswd
global save
global dosave
save = input('Do you want to save this token to tokens.txt? (y/n) ')
if save == 'y' or save == 'yes':
    dosave = 1
else:
    dosave = 0
email = input('What is the email? ')
pswd = input('What is the password? ')
retry = 0



def token():
    account = DiscordAccount()
    print('Getting the token...')
    l_storage = LocalStorage(driver)
    token = l_storage.get("token")
    token = token[1:-1]
    account.token = token
    print('Token: ' + account.token)
    if dosave == 1:
        print('Saving data...')
        with open('tokens.txt', 'a') as a:
            a.write(account.token)
            a.write('\n')
        driver.quit()
        exit()
    else:
        print('(Note: Your token was copied to your clipboard)')
        pyperclip.copy(str(account.token))
        driver.quit()
        exit()

def waitforaccountlogin():
    if driver.current_url == 'https://discord.com/channels/@me':
        token()
    else:
        waitforaccountlogin()

driver.get('https://discord.com/login')
time.sleep(0.1)

emailbox = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/input')
emailbox.send_keys(email)
time.sleep(0.1)
pswdbox = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input')
pswdbox.send_keys(pswd)
time.sleep(0.1)
loginbutton = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')
loginbutton.click()
while driver.current_url == 'https://discord.com/login':
    if retry == 0:
        print('Logging in... (Note: if the program freezes here, it is very likely your used a incorrect password)')
        retry = 1

time.sleep(0.1)
waitforaccountlogin()