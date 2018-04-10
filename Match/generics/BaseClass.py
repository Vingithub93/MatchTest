import os
from appium import webdriver
from altunityrunner import AltrunUnityDriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class BaseClass():
    
    altdriver = None
    eledriver=  None
    platform = "android" # set to iOS to change platform

    def setUp(self):
        self.desired_caps = {}
        if (self.platform == "android"):
            self.setup_android()
        else: 
            self.setup_ios()

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.altdriver = AltrunUnityDriver(self.driver, self.platform)


    def tearDown(self):
        self.altdriver.stop()
        self.driver.quit()

    def setup_android(self):
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['deviceName'] = 'device'
        self.desired_caps['newCommandTimeout'] = 90
        self.desired_caps['app'] = PATH('../match.apk')

    def setup_ios(self):
        self.desired_caps['platformName'] = 'iOS'
        self.desired_caps['deviceName'] = 'iPhone8'
        self.desired_caps['automationName'] = 'XCUITest'
        self.desired_caps['app'] = PATH('../../../sampleGame.ipa')
