from machine import Pin, SoftI2C
from time import sleep
from poc_accel import *
from poc_button import *
from wireless_manager import *
from checker import Checker
from debug import Debug


# ----- Accéléromètre

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)

accelTestDelegate = AccelTestDelegate()

# Création du capteur à partir de la classe Accel
accelero1 = Accel(i2c,0x68, accelTestDelegate)


# --------- Bouton

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
        

wirelessManager = WirelessManager(wsCallback=WebsocketCallback())

# ---------- Setup

testAll = True

allObjects = [btn1, accelero1, wirelessManager]
# allObjects = [wirelessManager]

allChecked = False

if testAll:
    allChecked = Checker.check(allObjects)



# ---------- Joystick

class Joystick:
    def __init__(self, accelerometer, button, wirelessManager=None):
        self.accelerometer = accelerometer
        self.button = button
        
        self.socketActive = True
        self.accelActive = True
        self.buttonActive = True
        
        self.wirelessManager = None
        
        if self.socketActive:
            self.wirelessManager = wirelessManager
            if self.wirelessManager != None :
                self.wirelessManager.startWSServer()
    
    def send_datas(self, datasToSend):
        self.wirelessManager.sendDataToWS(datasToSend)
    
    def process(self):
        if self.socketActive:
            if self.wirelessManager == None:
                Debug.LogWarning("Le wirelessManager n'est pas définis alors que le socket est actif. Le socket a besoin du wirelessManager.")
                return "stop"
            
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
                Debug.LogWhisper("Send datas " + datasToSend)
        else:
            Debug.LogWarning("Le socket n'est pas actif. Le programme est prévu pour fonctionner avec un socket actif")
            return "stop"





# --------- Boucle

if allChecked:
    joystick = Joystick(accelero1, btn1, wirelessManager)
    
    while True :
        value = joystick.process()
        sleep(0.25)
        if value == "stop":
            break
else:
    Debug.LogError("Toutes les vérifications des capteurs ne sont pas passées...")