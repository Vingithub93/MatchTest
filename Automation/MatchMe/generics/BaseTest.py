'''

@author: Vinayak
'''
import os
import unittest
from appium import webdriver
from altunityrunner import AltrunUnityDriver

from scenes.Scene1 import Scene1
from scenes.Scene2 import Scene2
from scenes.Scene3 import Scene3
import HtmlTestRunner




PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class BaseTest(unittest.TestCase):
    
    '''
    
    '''
    altdriver = None
    driver=None
    eledriver=  None
    text= None
    platform = "android" # set to iOS to change platform

    @classmethod
    def setUpClass(self):
        self.desired_caps = {}
        if (self.platform == "android"):
            self.desired_caps['platformName'] = 'Android'
            self.desired_caps['deviceName'] = 'device'
            self.desired_caps['newCommandTimeout'] = 400
            self.desired_caps['app'] = PATH('../../../match.apk')
        else: 
            self.desired_caps['platformName'] = 'iOS'
            self.desired_caps['deviceName'] = 'iPhone8'
            self.desired_caps['automationName'] = 'XCUITest'
            self.desired_caps['app'] = PATH('../../../match.ipa')

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.altdriver = AltrunUnityDriver(self.driver, self.platform)
        
    def test_01(self):
        self.scene1=Scene1(self.altdriver, self.driver)
        self.scene2=Scene2(self.altdriver, self.driver)
        self.scene3=Scene3(self.altdriver, self.driver)
        self.scene1.S1_flow_01()
        self.scene2.S2_flow_01()
        self.scene3.S3_flow_01()

    @classmethod
    def tearDownClass(self):
        self.altdriver.stop()
        self.driver.quit()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()