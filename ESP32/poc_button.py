from machine import Pin
from checker import CheckableClass
import time
from debug import Debug


class ButtonDelegate:
    def __init__(self):
        pass
    
    def clicked(self):
        pass
    
    def released(self):
        pass


class ButtonTestDelegate(ButtonDelegate):
    def __init__(self):
        super().__init__()
        self.verbose = False
        
    def clicked(self):
        if self.verbose:
            print("Le bouton a été pressé")
        
    def released(self):
        if self.verbose:
            print("Le bouton a été relaché")


class Button(CheckableClass):
    def __init__(self, nbPin, delegate=None):
        self.pin = Pin(nbPin, Pin.IN)
        self.currentClick = 0
        self.delegate = delegate
    
    def test(self):
        Debug.LogWhisper("Start testing button")
        Debug.Log("Please press on the button")
        
        time_to_wait = 5
        
        start_time = time.time()
        end_time = start_time + time_to_wait
        
        button_values = []
        
        while time.time() < end_time:
            button_values.append(self.pin.value())
            if (self.pin.value()):
                Debug.LogWhisper("Button pressed")
            time.sleep(0.25)
        
        if all(valeur == button_values[0] for valeur in button_values) == True:
            print("ERROR")
            return [{
                "result": "300",
                "class": self.__class__
            }]
        
        Debug.LogWhisper("Stop testing button")
        
        return [{
            "result": "100",
            "class": self.__class__
        }]
    
    
    def process(self):
        if self.pin.value():
            self.delegate.clicked()
        else:
            self.delegate.released()
        return self.pin.value()
    
    