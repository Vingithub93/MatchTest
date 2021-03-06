
import os

from altunityrunner import AltrunUnityDriver
from appium import webdriver
import pytest
from generics import ExcelLibrary

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class BaseTest():

    altdriver = None
    driver=None
    eledriver=  None
    text= None
    platform = None
    
    @classmethod
    def setup_class(self):
        
        self.platform=ExcelLibrary.get_Cellvalue(PATH('../data/controller.xlsx'), 'execution_controller', 1, 1)
        print "platform name = "+self.platform
        
        self.desired_caps = {}
        
        if (self.platform == "Android"):
            self.desired_caps['platformName'] = 'Android'
            self.desired_caps['deviceName'] = 'device'
            self.desired_caps['app'] = PATH('../match.apk')
            self.desired_caps['newCommandTimeout'] = 400
        else: 
            self.desired_caps['platformName'] = 'iOS'
            self.desired_caps['deviceName'] = 'iPhone8'
            self.desired_caps['automationName'] = 'XCUITest'
            self.desired_caps['app'] = PATH('../match.ipa')

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.altdriver = AltrunUnityDriver(self.driver, self.platform)


    @classmethod
    def teardown_class(self):
        self.altdriver.stop()
        self.driver.quit()
        if ExcelLibrary.get_Cellvalue(PATH('../data/controller.xlsx'), 'execution_controller', 0, 1)=='Local Devices':
            os.chdir(PATH('../reports'))
            os.startfile('Report.bat')
      
if __name__ == '__main__':
    pytest.main()
