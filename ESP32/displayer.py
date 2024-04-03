import time
from debug import *

"""
Succes
100 -> 199

Erreur de capteur
200 -> 299

Erreur de branchement
300 -> 399

Erreur code utilisateur
400 -> 499

"""


class ResultCodes:
    _code = {
        "100": {
            "name": "Succes ✅",
            "type": "success",
            "message": "L'opération s'est effectuée avec succès",
            "ledDebug": [
                {"on": 2000}
            ]
        },
        "200": {
            "name": "Erreur de capteur ❌",
            "type": "error",
            "message":"Le capteur ne répond pas correctement. Verifiez s'il est correctement branché ou changez de capteur puis réessayez.",
            "ledDebug": [
                {"on": 500},
                {"off": 500},
                {"on": 500}
            ]
        },
        "300": {
            "name": "Erreur de branchement ❌",
            "type": "error",
            "message": "Le capteur n'a pas été trouvé. Vérifiez s'il est correctement branché et réessayez.",
            "ledDebug": [
                {"on": 500},
                {"off": 500},
                {"on": 500},
                {"off": 500},
                {"on": 500}
            ]
        },
        "400": {
            "name": "Erreur code utilisateur ❌",
            "type": "error",
            "message": "Il faut spécifier un code d'erreur. Exemple : `ResultCodes.getCode(\"001\")`",
            "ledDebug": [
                {"on": 500},
                {"off": 500},
                {"on": 500},
                {"off": 500},
                {"on": 500},
                {"off": 500},
                {"on": 500}
            ]
        }
    }
    
    def __init__(self):
        pass
    
    @staticmethod
    def getName(code):
        return ResultCodes._code[code]["name"]
    @staticmethod
    def getMessage(code):
        return ResultCodes._code[code]["message"]
    @staticmethod
    def getCode(code):
        return ResultCodes._code[code]["ledDebug"]
    def getResult(code):
        return ResultCodes._code[code]


class Displayer:
    def __init__(self):
        pass
    
    @staticmethod
    def switchLed(isOn):
        if isOn:
            Debug.LogWhisper("Led ON")
            # Allumer la led
            pass
        else:
            Debug.LogWhisper("Led OFF")
            # Eteindre la led
            pass
    
    @staticmethod
    def raiseResult(result, classError=None):
        code = ResultCodes.getResult(result)
        
        name = code["name"]
        type = code["type"]
        message = code["message"]
        ledDebug = code["ledDebug"]
        
        # Create result message
        messageToPrint = ""
        messageToPrint += "Code: " + result 
        messageToPrint += "\nResultat: " + str(name)
        messageToPrint += "\nMessage: " + str(message)
        
        if classError != None:
            if classError.__class__:
                messageToPrint += "\nNom de la classe: " + str(classError.__name__ + "()")
        
        
        # Show error with the LED 
        for state in ledDebug:
            ledOn = False
            timeToWait = 0
            if "on" in state:
                ledOn = True 
                timeToWait = state["on"]
            elif "off" in state:
                timeToWait = state["off"]
        
            Displayer.switchLed(ledOn)
            time.sleep(timeToWait/1000)
        
        Displayer.switchLed(False)
        
        
        # Print error
        if type == "error":
            Debug.LogError(messageToPrint)
        elif type == "warning":
            Debug.LogWarning(messageToPrint)
        elif type == "success":
            Debug.LogSuccess(messageToPrint)



# ----- Test -----
Displayer.raiseResult("100")