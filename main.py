import time, json
from teams_handlers import Handlers
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

config = None

with open('config.json') as f:
   config = json.load(f)

class MyDriver:
    options = Options()
    options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
    })

    driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)

    driver.get('https://teams.microsoft.com')
    time.sleep(7)

    handler = Handlers(driver)
    handler.setConfiguration(config)

    handler.login(config['login'], config['password'])

    time.sleep(4)

    handler.scanClasses()

    # time.sleep(3)
    # driver.quit()

if __name__=='__main__':
    MyDriver()
    
