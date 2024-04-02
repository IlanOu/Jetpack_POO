from machine import Pin


class ButtonDelegate:
    def __init__(self):
        pass
    
    def clicked(self):
        pass
    
    def released(self):
        pass



class Button:
    def __init__(self, nbPin, delegate=None):
        self.pin = Pin(nbPin, Pin.IN)
        self.currentClick = 0
        self.delegate = delegate
    
    def process(self):
        if self.pin.value():
            self.delegate.clicked()
        else:
            self.delegate.released()
        return self.pin.value()
        