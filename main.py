import time, json
import helper
from teams_handlers import Handlers
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

config = None

with open('config.json') as f:
   config = json.load(f)

def initDriver():
    options = Options()
    options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
    })

    return webdriver.Chrome(executable_path='./chromedriver.exe', options=options)

def runner():
    try:
        driver = initDriver()

        driver.get('https://teams.microsoft.com')
        time.sleep(7)

        handler = Handlers(driver)
        handler.setConfiguration(config)

        handler.login(config['login'], config['password'])

        time.sleep(4)

        handler.scanClasses()

        helper.wait(60*45)#45 mins, time of during a class
        driver.quit()
    except:
        pass


if __name__=='__main__':
    while True:
        print('{}New session of chrome is starting{}'.format(helper.Colors.RED, helper.Colors.RESET))
        runner()
        time.sleep(2)
    
