import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import json
from tools.toolbox.Debug import Debug

import random

GPIO.setwarnings(False)


class JsonManager:
    def __init__(self, path="./tools/"):
        self.path = path
        self.reader = SimpleMFRC522()
        

    # Add a user to JSON and write id on badge
    # ---------------------------------------------------------------------------- #
    def write_user(self, id):
        dict = {}
        
        # book = random.choice(["b-1", "b-0", "b-3", "b-2"])
        # dict[id] = {
        #     "name":"",
        #     "books_read":[book]
        # }
        
        dict[id] = {
            "name":"",
            "books_read":[]
        }
        
        
        with open(self.path + './users.json','r+') as f:
            try:
                dic = json.load(f)
            
            except json.JSONDecodeError:
                Debug.LogError("Le json n'a pas été décodé...")
                dic = {}
            
            # if id in dic:
            #     Debug.LogError("Ton identifiant existe déjà fils de pute !")
            # else:
            dic.update(dict)
            f.seek(0)
            json.dump(dic, f)
            f.truncate()
            
            
            Debug.LogWarning("Ajout de l'user avec l'id : " + id)
            Debug.Log("Passez votre badge devant le capteur...")
            self.reader.write(id)


    # Get user in the JSON
    # ---------------------------------------------------------------------------- #
    def get_user(self, id):
        with open(self.path + 'users.json','r') as f:
            datas = json.load(f)
            return datas.get(id)



# json_manager = JsonManager()
# json_manager.write_user("22")
# Debug.LogSuccess(json_manager.get_user("22"))
