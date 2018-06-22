
class Scene1Tasks(object):

    altdriver=None
    driver=None
    def __init__(self, altdriver, driver):
        self.altdriver=altdriver
        self.driver=driver
    
    def checkInformation(self):
        self.altdriver.wait_for_element('button "information"').tap()
        self.altdriver.wait_for_element('Information Pop-up')
        self.altdriver.wait_for_element('Close').tap()
        
    def clickPlay(self):
        self.altdriver.wait_for_element('Play').tap()
    
    def clickFacebook(self):
        self.altdriver.wait_for_element('Facebook Connect').tap()
    