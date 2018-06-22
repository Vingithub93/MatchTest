
from time import sleep
from workflow.Scene1Tasks import Scene1Tasks

class Scene1(object):

    altdriver=None
    driver=None
    def __init__(self, altdriver, driver):
        self.altdriver=altdriver
        self.driver=driver
    
    def S1_flow_01(self):
        
        self.scene1=Scene1Tasks(self.altdriver, self.driver)
        
        self.altdriver.wait_for_current_scene_to_be('MainMenu')
        sleep(6)
        self.driver.save_screenshot("../screenshots/Home_screen.png")
        sleep(1)
        self.scene1.checkInformation()
        self.scene1.clickPlay()