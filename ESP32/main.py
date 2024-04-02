from machine import Pin, SoftI2C
from time import sleep
from poc_accel import Accel
from poc_button import Button
from wireless_manager import *


# ----- Accéléromètre

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)
# Création du capteur à partir de la classe Accel
accelero1 = Accel(i2c,0x68)

accelero_active = True

# --------- Bouton

PIN_BUTTON_1 = 13

btn1 = Button(PIN_BUTTON_1)

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

# --------- Boucle

while True :
    
    datasToSend = ""
    
    if accelero_active :
        orientation = accelero1.get_orientation()
        if int(orientation["x"]) != 0:
            if socket_active:
                datasToSend += str("gyro-" + str(orientation["y"]) + "///")
            
        # print(orientation["x"])
        
    if button_active :
        btnValue = btn1.process()
        
        if btnValue:
            datasToSend += "btn-1///"
        else:
            datasToSend += "btn-0///"
        
    
    if socket_active:
        wirelessManager.process()
        if datasToSend != "":
            wirelessManager.sendDataToWS(datasToSend)
            # print(">>> Send datas to user : " + datasToSend)
    sleep(0.25)
