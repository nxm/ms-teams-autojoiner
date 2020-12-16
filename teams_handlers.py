import time
from webhook import sendMessage
from helper import Colors
from selenium.webdriver.common.keys import Keys

class Handlers:
    config = None
    foundActiveClass = False

    def __init__(self, driver):
        self.driver = driver

    def setConfiguration(self, config):
        self.config = config

    def login(self, login, password):
        emailLabel = self.driver.find_element_by_xpath('//*[@id="i0116"]')
        emailLabel.click()
        emailLabel.send_keys(login)
        emailLabel.send_keys(Keys.ENTER)
        
        time.sleep(2)

        passwordLabel = self.driver.find_element_by_xpath('//*[@id="i0118"]')
        passwordLabel.click()
        passwordLabel.send_keys(password)
        passwordLabel.send_keys(Keys.ENTER)

        submitLabel = self.driver.find_element_by_xpath('//*[@id="idSIButton9"]')
        submitLabel.click()

        time.sleep(6) #długo to trwa

        webChoiceLabel = self.driver.find_element_by_xpath('//*[@id="download-desktop-page"]/div/a')
        webChoiceLabel.click()


    def scanClasses(self):
        """
        TODO: return true/false i w main kontynuować ;)
        """


        while self.foundActiveClass == False:
            myClasses = self.driver.find_elements_by_xpath('//a[@data-team-id]')
            print('Subjects length:', len(myClasses))

            for i in myClasses:
                i.click()

                className = i.get_attribute('data-tid').lower()
                print('{} - {}{}'.format(Colors.LIGHT_GREY, className, Colors.RESET))

                skipClass = False

                try:
                    currentMeeting = i.find_element_by_xpath('//span[@class="ts-active-calls-counter flex-fill"]')
                    print('{}[+] Found active class! ({}){}'.format(Colors.GREEN, className, Colors.RESET))

                    for b in self.config['blacklist']:
                        if className == b:
                            print('{}This class is blacklisted, so you can\'t join to meeting :({}'.format(Colors.RED, Colors.RESET))
                            skipClass = True

                    if skipClass:
                        continue
                    else:
                        self.foundActiveClass = True
                        print('\n{}Trying to join...{}'.format(Colors.BLUE, Colors.RESET))
                        self.joinMeeting(className)
                        return True
                except:
                    pass

                time.sleep(1.5)

            print(' [!] Unfortunately we couldn\'t find class for you :[')

            time.sleep(30) #TODO: every 5 mins or set by config value

    def joinMeeting(self, className):

        try:
            joinButton = self.driver.find_element_by_class_name("ts-calling-join-button")
            joinButton.click()
        except:
            pass

        webcamButton = self.driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]')

        if webcamButton.get_attribute('title') == 'Turn camera off':
            webcamButton.click()
        time.sleep(1)

        micButton = self.driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]')

        if micButton.get_attribute('title') == 'Mute microphone':
            micButton.click()
        time.sleep(1)

        joinNowButton = self.driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
        joinNowButton.click()

        sendMessage(self.config, className, "success")

