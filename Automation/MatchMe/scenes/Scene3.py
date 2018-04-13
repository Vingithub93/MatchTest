'''


@author: Vinayak
'''
from time import sleep
from workflow.Scene3Tasks import Scene3Tasks
from workflow.Scene2Tasks import Scene2Tasks
from workflow.Scene1Tasks import Scene1Tasks

class Scene3(object):
    '''
    classdocs
    '''

    altdriver=None
    driver=None
    def __init__(self, altdriver, driver):
        self.altdriver=altdriver
        self.driver=driver
    
    def S3_flow_01(self):
        self.scene1=Scene1Tasks(self.altdriver, self.driver)
        self.scene2=Scene2Tasks(self.altdriver, self.driver)
        self.scene3=Scene3Tasks(self.altdriver, self.driver)
        
        self.altdriver.wait_for_current_scene_to_be('mainGame')
        sleep(6)
        self.driver.save_screenshot("../screenshots/Level_1_Game_screen.png")
        sleep(1)
        self.scene3.sequentialMoves()
        sleep(14)
        self.driver.save_screenshot("../screenshots/Level_1_complete.png")
        sleep(1)
        self.scene3.clickNext()
        sleep(8)
        self.scene2.clickPlay()
        sleep(14)
        self.driver.save_screenshot("../screenshots/Level_2_Game_screen.png")
        sleep(1)
        self.scene3.sequentialMoves()
        sleep(14)
        self.driver.save_screenshot("../screenshots/Level_2_complete.png")
        sleep(1)
        self.scene3.clickNext()
        sleep(8)
        self.scene2.clickPlay()
        sleep(10)
        self.scene3.clickSettings()
        sleep(2)
        self.scene2.quitScreen()
        sleep(1)
        self.scene2.clickClose()
        self.altdriver.wait_for_current_scene_to_be('Map')
        