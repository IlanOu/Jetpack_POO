from tools.toolbox.Debug import Debug
from tools.Auth import Authenticator
from tools.Say import Speaker, GttsEngine
from tools.Recommendation import BookRecommender
from JsonManager import JsonManager

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

import random

Debug.prefixActive = False


# ---------------------------------------------------------------------------- #
#                                    Checker                                   #
# ---------------------------------------------------------------------------- #
class Checker:
    def __init__(self):
        self.authenticator = Authenticator()
        self.json_manager = JsonManager()
        
    def check_user(self, id: str):
        if (id is None or not bool(id.strip())):
            id = str(random.randint(0, 1000))
            Debug.LogWarning("Ce badge n'a pas d'ID.")
            Debug.Log("Création d'un nouvel id : " + id)
            
            Debug.Log("Ajout de l'utilisateur au JSON")
            self.json_manager.write_user(id.strip())
        
        current_user = self.authenticator.authenticate(id)
        
        if current_user == None:
            self.json_manager.write_user(id.strip())
            current_user = self.authenticator.authenticate(id)
            
        if current_user == None:
            Debug.LogError("Il y a eu une erreur dans l'authentification")
        
        return current_user


# RFID 
# ---------------------------------------------------------------------------- #
reader = SimpleMFRC522()
Debug.Log("Passez votre badge devant le capteur")
# reader.write("")
id, text = reader.read()

# Authentification
# ---------------------------------------------------------------------------- #
checker = Checker()
current_user = checker.check_user(text)

# Recommendation
# ---------------------------------------------------------------------------- #
if (len(current_user.books_read) > 0):
    recommender = BookRecommender()
    book = current_user.books_read[0]
    recommendations = recommender.recommend_books(book)

    Debug.Log(f"Recommandations pour '{book.title}' :")
    for rec in recommendations:
        Debug.Log(f"- {rec.title} (par {rec.author})")


    # Summary
    # ---------------------------------------------------------------------------- #
    Debug.Log(f"Résumé pour '{book.title}' :")
    Debug.Log(f"{book.summary}")



    # Say hello
    # ---------------------------------------------------------------------------- #
    speek = True
    if speek:
        text = ""
        text += "Bonjour, " + current_user.name + " !"
        Speaker.say(text, GttsEngine())
        
        
        text = ""
        text += f"Recommandations pour '{book.title}' :"
        text += ", ".join(map(lambda x: x.title, recommendations))
        Speaker.say(text, GttsEngine())
        
        text = ""
        text += f"Résumé pour '{book.title}' :"
        text += f"{book.summary}"
        
        Speaker.say(text, GttsEngine())


# Success
# ---------------------------------------------------------------------------- #
Debug.LogSuccess("Finished")

