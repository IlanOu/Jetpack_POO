from machine import Pin, SoftI2C
from time import sleep
from poc_accel import *
from poc_button import *
from wireless_manager import *


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

accelero_active = True

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

button_active = True


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
        

socket_active = True

if socket_active:
    wirelessManager = WirelessManager(wsCallback=WebsocketCallback())

    wirelessManager.process()
    wirelessManager.sendDataToWS("--- Initialization ---")




class Joystick:
    def __init__(self, accelerometer, button, wirelessManager):
        self.accelerometer = accelerometer
        self.button = button
        self.wirelessManager = wirelessManager
        
        self.socketActive = True
        self.buttonActive = True
        self.accelActive = True
    
    
    def send_datas(self, datasToSend):
        wirelessManager.sendDataToWS(datasToSend)
    
    def process(self):
        datasToSend = ""
        if self.socketActive:
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


# --------- Boucle

joystick = Joystick(accelero1, btn1, wirelessManager)

while True :
    joystick.process()
    sleep(0.25)
