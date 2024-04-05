from debug import Debug
from checker import CheckableClass



class CommunicationCallback:
    
    def __init__(self):
        pass
    
    def connectionCallback(self):
        print("Connected")
    
    def disconnectionCallback(self):
        print("Disconected")
    
    def didReceiveCallback(self,value):
        print(f"Received {value}")
    

class WirelessManager(CheckableClass):
    
    def __init__(self,bleCallback = None,wsCallback = None):
        self.bleCallback = bleCallback
        self.wsCallback = wsCallback
        
        self.server = None
        
        if self.bleCallback != None:
            from ble_simple_peripheral import bluetooth,BLESimplePeripheral
            self.ble = bluetooth.BLE()
            self.blePeripheral = BLESimplePeripheral(self.ble,name=self.bleCallback.bleName)
            self.blePeripheral.on_write(self.bleCallback.didReceiveCallback)
            
        
        
    def test(self):
        tests = []
        
        # First part testing
        result = self.startWSServer()
        tests.append(result)

        
        # Second part testing
        # if not self.isConnected():
        #     connection_result = {
        #         "result": "201",
        #         "class": self.__class__
        #     }
        #     tests.append(connection_result)
        
        
        if result["result"] == "100":
            if self.server != None:
                self.server.stop()
            
        return tests
    
    
    def startWSServer(self):
        result_code = "100"
        
        if self.wsCallback != None:
            from ws_server import WebSocketServer
            self.server = WebSocketServer(self.wsCallback.connectionCallback,self.wsCallback.disconnectionCallback,self.wsCallback.didReceiveCallback)
            self.server.start(3000)
            Debug.LogWhisper(">>> Lancement du serveur")
        else:
            result_code = "400"
        
        return {
            "result": result_code,
            "class": self.__class__
        }
        
    
    def isConnected(self):
        if self.bleCallback != None:
            return self.blePeripheral.is_connected()
        if self.wsCallback != None:
            if self.server.isConnected:
                Debug.LogWhisper(">>> Client connecté")
            return self.server.isConnected
            
    
    def sendDataToBLE(self,data):
        if self.bleCallback != None:
            if self.blePeripheral.is_connected():
                self.blePeripheral.send(data)
                
    def sendDataToWS(self,data):
        if self.wsCallback != None:
            if self.server.isConnected:
                self.server.send_to_all(data)
                self.server.process_all()
    
    def process(self):
        if self.wsCallback != None:
            self.server.process_all()
    