'''


@author: Vinayak
@
'''

from time import sleep
from workflow.Scene2Tasks import Scene2Tasks

class Scene2(object):
    '''
    '''

    altdriver=None
    driver=None
    def __init__(self, altdriver, driver):
        self.altdriver=altdriver
        self.driver=driver
    
    def S2_flow_01(self):
        self.altdriver.wait_for_current_scene_to_be('Map')
        sleep(5)
        self.driver.save_screenshot("../screenshots/Map_screen.png")
        sleep(1)
        self.scene2=Scene2Tasks(self.altdriver, self.driver)
        self.scene2.clickLives()
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
        self.scene2.selectLevel('Level 1')
        self.scene2.clickPlay()