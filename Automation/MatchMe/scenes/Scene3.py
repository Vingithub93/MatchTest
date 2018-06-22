
from time import sleep
from workflow.Scene3Tasks import Scene3Tasks
from workflow.Scene2Tasks import Scene2Tasks
from workflow.Scene1Tasks import Scene1Tasks

class Scene3(object):

    altdriver=None
    driver=None
    def __init__(self, altdriver, driver):
        self.altdriver=altdriver
        self.driver=driver
    
    def S3_Level_complete(self, fLevel, sLevel):
        self.scene1=Scene1Tasks(self.altdriver, self.driver)
        self.scene2=Scene2Tasks(self.altdriver, self.driver)
        self.scene3=Scene3Tasks(self.altdriver, self.driver)
        
        self.altdriver.wait_for_current_scene_to_be('mainGame')
        sleep(6)
        self.driver.save_screenshot("../screenshots/+"+fLevel+"_Game_screen.png")
        sleep(1)
        self.scene3.sequentialMoves()
        sleep(14)
        self.altdriver.wait_for_element('Counter')
        self.gScore=self.altdriver.get_element_text('Counter')
        self.driver.save_screenshot("../screenshots/+"+fLevel+"_complete.png")
        sleep(1)
        self.altdriver.wait_for_element('Text *Score*')
        self.pScore=self.altdriver.get_element_text('Text *Score*')
        if self.gScore!=self.pScore:
            print 'Expected : '+self.pScore+' Actual : '+self.gScore
            assert False
        self.scene3.clickNext()
        sleep(8)
        self.level=self.altdriver.get_element_text('text *level number*')
        if self.level!=sLevel.upper():
            print 'Expected : '+sLevel.upper()+' Actual : '+self.level
            assert False
        self.scene2.clickPlay()
        sleep(12)
        self.scene3.clickSettings()
        sleep(2)
        self.scene2.quitScreen()
        sleep(1)
        self.scene2.clickClose()
        self.altdriver.wait_for_current_scene_to_be('Map')
        