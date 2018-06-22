

from time import sleep
from workflow.Scene2Tasks import Scene2Tasks
from generics.Generics import Generics

class Scene2(object):

    altdriver=None
    driver=None
    def __init__(self, altdriver, driver):
        self.altdriver=altdriver
        self.driver=driver
    
    def S2_flow_01(self):
        self.altdriver.wait_for_current_scene_to_be('Map')
        sleep(2)
        self.driver.save_screenshot("../screenshots/Map_screen.png")
        sleep(1)
        self.scene2=Scene2Tasks(self.altdriver, self.driver)
        self.scene2.clickLives()
        sleep(1)
        self.driver.save_screenshot("../screenshots/Lives.png")
        sleep(1)
        self.scene2.clickClose()
        sleep(2)
        self.scene2.clickAchivements()
        self.driver.save_screenshot("../screenshots/Achivements.png")
        sleep(1)
        self.scene2.clickCloseRightPanel()
        sleep(2)
        self.scene2.clickSettings()
        #sleep(1)
        self.scene2.clickMusic()
        #sleep(1)
        self.scene2.clickMusic()
        #sleep(1)
        self.scene2.clickClose()
        sleep(2)
        
    def S2_Select_level(self, level):
        self.scene2=Scene2Tasks(self.altdriver, self.driver)
        self.altdriver.wait_for_current_scene_to_be('Map')
        self.driver.save_screenshot("../screenshots/Map"+level+"_screen.png")
        if level!='Level 1':   
            sleep(2)
            self.generics=Generics()
            self.generics.scroll(self.driver, 0.50, 0.50, 0.85, 0.15)
            sleep(1)
            self.generics.scroll(self.driver, 0.50, 0.50, 0.85, 0.15)
            sleep(2)
        self.scene2.selectLevel(level)
        self.altdriver.wait_for_element('text *level number*')
        self.level=self.altdriver.get_element_text('text *level number*')
        if self.level!=level.upper():
            print 'Expected : '+level.upper()+' Actual : '+self.level
            assert False
        self.scene2.clickPlay()