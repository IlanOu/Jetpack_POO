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
        "201": {
            "name": "Erreur de connexion ❌",
            "type": "error",
            "message":"Le serveur n'est pas connecté. Vérifiez si vous êtes bien connecté à internet puis réessayez.",
            "ledDebug": [
                {"on": 1000},
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
            "message": "Hmm... Il semblerait que vous ayez oublié un paramètre ou un valeur... Vérifiez votre code puis réessayez.",
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
    def getType(code):
        return ResultCodes._code[code]["type"]
    @staticmethod
    def getMessage(code):
        return ResultCodes._code[code]["message"]
    @staticmethod
    def getCode(code):
        return ResultCodes._code[code]["ledDebug"]
    @staticmethod
    def getResult(code):
        return ResultCodes._code[code]


class Displayer:
    def __init__(self):
        pass
    
    @staticmethod
    def switchLed(isOn, timeToWait):
        if isOn:
            # Debug.LogWhisper("Led ON")
            for i in range(timeToWait/10):
                Debug.LogWhisper(i)
                time.sleep(0.01)
            # Allumer la led
            pass
        else:
            # Debug.LogWhisper("Led OFF")
            time.sleep(timeToWait/1000)
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
                messageToPrint += "\nObjet testé: " + str(classError.__name__ + "()")
        
        
        # Show error with the LED 
        for state in ledDebug:
            ledOn = False
            timeToWait = 0
            if state.get("on") != None:
                ledOn = True 
                timeToWait = state["on"]
            elif state.get("off") != None:
                timeToWait = state["off"]
        
            Displayer.switchLed(ledOn, timeToWait)
            # time.sleep(timeToWait/1000)
        
        # Displayer.switchLed(False)
        
        
        # Print error
        if type == "error":
            Debug.LogError(messageToPrint)
        elif type == "warning":
            Debug.LogWarning(messageToPrint)
        elif type == "success":
            Debug.LogSuccess(messageToPrint)



# ----- Test -----
# Displayer.raiseResult("200")