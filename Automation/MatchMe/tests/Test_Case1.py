'''


@author: Vinayak
'''
from generics.BaseTest import BaseTest
from scenes.Scene1 import Scene1
from scenes.Scene2 import Scene2
from scenes.Scene3 import Scene3


class Test_Case1(BaseTest):


    def test_01(self):
        self.scene1=Scene1(self.altdriver, self.driver)
        self.scene2=Scene2(self.altdriver, self.driver)
        self.scene3=Scene3(self.altdriver, self.driver)
        self.scene1.S1_flow_01()
        self.scene2.S2_flow_01()
        self.scene3.S3_flow_01()
        
        self.assertEqual('first', 'first')