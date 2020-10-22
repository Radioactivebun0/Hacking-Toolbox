import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from sys import argv
import sys

# some code so that chrome doesnt know your using selenium :)
useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": useragent.random})
print(driver.execute_script("return navigator.userAgent;"))

driver.get('https://discord.com/login')

time.sleep(2)

token = input('What is the token? ')

script1 = '''setInterval(() => { document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"'''
script2 = '''"` }, 50); setTimeout(() => { location.reload(); }, 2500);'''

scriptToExecut = script1 + token + script2

driver.execute_script(scriptToExecut)