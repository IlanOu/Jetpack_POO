from machine import Pin, SoftI2C
from time import sleep
from poc_accel import *
from poc_button import *
from wireless_manager import *
from checker import Checker


# ----- Accéléromètre


class AccelTestDelegate(AccelDelegate):
    def __init__(self):
        super().__init__()
        self.verbose = False
        
    def right(self):
        if self.verbose:
            print("Direction : Droite")
        
    def left(self):
        if self.verbose:
            print("Direction : Gauche")


i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)

accelTestDelegate = AccelTestDelegate()

# Création du capteur à partir de la classe Accel
accelero1 = Accel(i2c,0x68, accelTestDelegate)

# --------- Bouton



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

PIN_BUTTON_1 = 13

buttonTestDelegate = ButtonTestDelegate()

btn1 = Button(PIN_BUTTON_1, buttonTestDelegate)


# --------- Connect Websocket 


class WebsocketCallback(CommunicationCallback):

    def __init__(self):
        pass
    
    def connectionCallback(self):
        print("Connected")
    
    def disconnectionCallback(self):
        print("Disconected")
    
    def didReceiveCallback(self,value):
        print(f"Received {value}")
        



# ----------

testAll = True

allObjects = [btn1, accelero1]

if testAll:
    for obj in allObjects:
        Checker.check(obj)


class Joystick:
    def __init__(self, accelerometer, button, wirelessManager):
        self.accelerometer = accelerometer
        self.button = button
        self.wirelessManager = wirelessManager
        
        self.socketActive = False
        self.accelActive = False
        self.buttonActive = True
    
    
    def send_datas(self, datasToSend):
        wirelessManager.sendDataToWS(datasToSend)
    
    def process(self):
        
        if self.socketActive:
            datasToSend = ""
            if self.accelActive:
                orientation = self.accelerometer.process()
                if int(orientation["x"]) != 0:
                    datasToSend += str("gyro-" + str(orientation["y"]) + "///")
            
            if self.buttonActive:
                btnValue = self.button.process()
                if btnValue:
                    datasToSend += "btn-1///"
                else:
                    datasToSend += "btn-0///"
                
            self.wirelessManager.process()
            if datasToSend != "":
                self.send_datas(datasToSend)
                print("Send datas " + datasToSend)
        else:
            return None


# --------- Boucle
"""
wirelessManager = WirelessManager(wsCallback=WebsocketCallback())

joystick = Joystick(accelero1, btn1, wirelessManager)

while True :
    joystick.process()
    sleep(0.25)
"""