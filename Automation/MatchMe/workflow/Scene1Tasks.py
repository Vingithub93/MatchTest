'''
Created on 12-Apr-2018

@author: Automation
'''
from altunityrunner.runner import AltrunUnityDriver
from time import sleep

class Scene1Tasks(object):
    '''
    classdocs
    '''
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
    