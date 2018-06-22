
class Scene2Tasks(object):

    altdriver=None
    driver=None
    def __init__(self, altdriver, driver):
        self.altdriver=altdriver
        self.driver=driver
        
    def clickLives(self):
        self.altdriver.wait_for_element('Base').tap()
        self.altdriver.wait_for_element('Close').tap()
    
    def clickAchivements(self):
        self.altdriver.wait_for_element('Achievements Icon').tap()
        
    def clickSettings(self):
        self.altdriver.wait_for_element('Settings')
        names=self.altdriver.find_elements('Normal')
        names[1].tap()
        
        
    def clickClose(self):
        self.altdriver.wait_for_element('Close').tap()
        
    def clickCloseRightPanel(self):
        self.altdriver.wait_for_element('Close Button').tap()
        
    def selectLevel(self, level):
        self.altdriver.wait_for_element(level).tap()
    
    def clickPlay(self):
        self.altdriver.wait_for_element('Button "Play"').tap()
        
    def clickMusic(self):
        self.altdriver.wait_for_element('Music').tap()
        
    def enableMusic(self):
        self.altdriver.wait_for_element('Music Off').tap()
        
    def quitScreen(self):
        self.altdriver.wait_for_element('Quit').tap()