from machine import Pin
from checker import CheckableClass

class ButtonDelegate:
    def __init__(self):
        pass
    
    def clicked(self):
        pass
    
    def released(self):
        pass



class Button(CheckableClass):
    def __init__(self, nbPin, delegate=None):
        self.pin = Pin(nbPin, Pin.IN)
        self.currentClick = 0
        self.delegate = delegate
    
    def test(self):
        return {
            "result": "100",
            "class": self.__class__
            }
    
    def process(self):
        if self.pin.value():
            self.delegate.clicked()
        else:
            self.delegate.released()
        return self.pin.value()
    
    