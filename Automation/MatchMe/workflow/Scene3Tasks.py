from time import sleep

class Scene3Tasks(object):

    altdriver=None
    driver=None
    def __init__(self, altdriver, driver):
        self.altdriver=altdriver
        self.driver=driver
        
    def sequentialMoves(self):
        text=self.altdriver.get_element_text('counter')
        print 'Number of moves'+text
        text=int(text)
        names=self.altdriver.find_elements_where_name_contains('token(Clone)')
        print 'Number of elements'+str(len(names))
        while (text!=0):
            
            for i in range(len(names)):
                if i<len(names)-10:
                    if text!=0:
                        names[i].tap()
                        names[i+1].tap()
                        names[i].tap()
                        names[i+9].tap()
                        text=self.altdriver.get_element_text('counter')
                        text=int(text)
                        print text
                        if text==0:
                            print "Moves are 0"
                            break
                        
    def clickNext(self):
        self.altdriver.wait_for_element('Text "Next"').tap()
        
    def clickSettings(self):
        self.altdriver.wait_for_element('Normal').tap()
        
    
        