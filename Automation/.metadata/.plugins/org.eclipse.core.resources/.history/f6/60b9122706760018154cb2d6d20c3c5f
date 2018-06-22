
from generics.BaseTest import BaseTest
from scenes.Scene1 import Scene1
from scenes.Scene2 import Scene2
from scenes.Scene3 import Scene3
import pytest

class Test_Case1(BaseTest):

    screen=None
    
    @pytest.allure.CRITICAL
    def test_01(self):
        '''
        Complete end to end testing of Level 1
        '''
        
        self.scene1=Scene1(self.altdriver, self.driver)
        self.scene2=Scene2(self.altdriver, self.driver)
        self.scene3=Scene3(self.altdriver, self.driver)
        
        self.scene1.S1_flow_01()
        self.scene2.S2_flow_01()
        self.scene2.S2_Select_level('Level 1')
        self.scene3.S3_Level_complete('Level 1', 'Level 2')
        
    @pytest.allure.CRITICAL
    def test_02(self):
        '''
        Complete end to end testing of Level 2
        '''
        
        self.scene1=Scene1(self.altdriver, self.driver)
        self.scene2=Scene2(self.altdriver, self.driver)
        self.scene3=Scene3(self.altdriver, self.driver)
        
        self.scene2.S2_Select_level('Level 2')
        self.scene3.S3_Level_complete('Level 2', 'Level 3')