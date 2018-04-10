import os
from time import sleep
import unittest
from appium import webdriver
from altunityrunner import AltrunUnityDriver
from altunityrunner import AltElement
import HtmlTestRunner



PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Test(unittest.TestCase):
    altdriver = None
    eledriver=  None
    text= None
    platform = "android" # set to iOS to change platform

    def setUp(self):
        self.desired_caps = {}
        if (self.platform == "android"):
            self.setup_android()
        else: 
            self.setup_ios()

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.altdriver = AltrunUnityDriver(self.driver, self.platform)
        self.assertTrue(True, 'Launching the application')


    def tearDown(self):
        self.assertTrue(True, 'Shutting down the application')
        self.altdriver.stop()
        self.driver.quit()

    def setup_android(self):
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['deviceName'] = 'device'
        self.desired_caps['newCommandTimeout'] = 400
        self.desired_caps['app'] = PATH('../../match.apk')

    def setup_ios(self):
        self.desired_caps['platformName'] = 'iOS'
        self.desired_caps['deviceName'] = 'iPhone8'
        self.desired_caps['automationName'] = 'XCUITest'
        self.desired_caps['app'] = PATH('../../../game.ipa')

    def test_simple_actions(self):
        self.assertTrue(True, 'Application is launched')
        self.altdriver.wait_for_current_scene_to_be('MainMenu')
        sleep(10)
        self.altdriver.wait_for_element('Play').tap()
        self.altdriver.wait_for_current_scene_to_be('Map')
        self.assertTrue(True, 'Level scene is loaded')
        sleep(3)
        dSize=self.driver.get_window_size()
        start_x=dSize['width']*0.50
        end_x=dSize['width']*0.50
        start_y=dSize['height']*0.15
        end_y=dSize['height']*0.85
        self.driver.swipe(start_x, start_y, end_x, end_y)

        sleep(3)
        start_y=dSize['height']*0.85
        end_y=dSize['height']*0.15
        self.driver.swipe(start_x, start_y, end_x, end_y)
        self.driver.swipe(start_x, start_y, end_x, end_y)

        sleep(3)
        
        self.altdriver.wait_for_element('Level 1').tap()
        self.altdriver.wait_for_element('text *level number*')
        title=self.altdriver.get_element_text('text *level number*')
        self.assertEqual(title, 'LEVEL 1', 'Starting Level 1')
        self.altdriver.wait_for_element('Button "Play"').tap()
        self.altdriver.wait_for_current_scene_to_be('mainGame')
        sleep(6)
        text=self.altdriver.get_element_text('counter')
        self.assertEqual(text,'8', 'Number of steps are verified')
        print text
        self.altdriver.wait_for_element('Counter')
        score=self.altdriver.get_element_text('Counter')
        str(score)
        self.assertEqual(score, '0', 'Score is checked')
        
        names=self.altdriver.find_elements_where_name_contains('token(Clone)')
        print len(names)
        #sleep(30)
        print type(text)
        text=int(text)
        while (text!=0):
            
            for i in range(len(names)):
                if i<len(names)-11:
                    if text!=0:
                        #names[i].dragToElement(names[i+1])
                        #names[i].dragToElement(names[i+9])
                        names[i].tap()
                        names[i+1].tap()
                        names[i].tap()
                        names[i+9].tap()
                        text=self.altdriver.get_element_text('counter')
                        text=int(text)
                        print text
                        if text==0:
                            print "Inner if "+str(text)
                            text=0
                            
                            break
        sleep(14)
        self.altdriver.wait_for_element('Text "Next"')
        win=self.altdriver.get_element_text('Text "Next"')
        self.assertEqual(win, 'NEXT', 'Level 1 is completed')
        self.altdriver.wait_for_element('Button "Next"').tap()
        sleep(10)
        title=self.altdriver.get_element_text('text *level number*')
        self.assertEqual(title, 'LEVEL 2', 'Starting Level 2')
        self.altdriver.wait_for_element('Button "Play"').tap() 
        self.altdriver.wait_for_element('counter')
        sleep(4)
        text=self.altdriver.get_element_text('counter')
        print text
        names=self.altdriver.find_elements_where_name_contains('token(Clone)')
        print len(names)
        
        #sleep(30)
        print type(text)
        text=int(text)
        while (text!=0):
            
            for i in range(len(names)):
                if i<len(names)-11:
                    if text!=0:
                        #names[i].dragToElement(names[i+1])
                        #names[i].dragToElement(names[i+9])
                        names[i].tap()
                        names[i+1].tap()
                        names[i].tap()
                        names[i+9].tap()
                        text=self.altdriver.get_element_text('counter')
                        text=int(text)
                        print text
                        if text==0:
                            print "Inner if "+str(text)
                            text=0
                            
                            break

           

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='game_reports'))
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
