import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import json
from tools.toolbox.Debug import Debug


GPIO.setwarnings(False)


class JsonManager:
    def __init__(self, path="./tools/"):
        self.path = path
        self.reader = SimpleMFRC522()
        

    def write_user(self, id):
        dict = {}
        
        dict[id] = {
            "name":"",
            "books_read":[]
        }
        
        with open(self.path + 'users.json','r+') as f:
            try:
                dic = json.load(f)
            except json.JSONDecodeError:
                dic = {}
            
            # if id in dic:
            #     Debug.LogError("Ton identifiant existe déjà fils de pute !")
            # else:
            dic.update(dict)
            f.seek(0)
            json.dump(dic, f)
            f.truncate()
            
            self.reader.write(id)

    def get_user(self, id):
        with open(self.path + 'users.json','r') as f:
            datas = json.load(f)
            return datas.get(id)



json_manager = JsonManager()
json_manager.write_user("22")
Debug.LogSuccess(json_manager.get_user("22"))
