from machine import Pin

class Button:
    
    def __init__(self, nbPin):
        self.pin = Pin(nbPin, Pin.IN)
        self.currentClick = 0
    
    def process(self):
        return self.pin.value()
        