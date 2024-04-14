from Debug import Debug
from Auth import Authenticator
from Say import Speaker


Debug.prefixActive = False



# ---------------------------------------------------------------------------- #
#                                    Checker                                   #
# ---------------------------------------------------------------------------- #
class Checker:
    def __init__(self):
        self.authenticator = Authenticator()
        
    def check_user(self, id):
        current_user = self.authenticator.authenticate(id)
        
        if (current_user is None):
            Debug.LogError("Il n'y a pas d'utilisateur avec l'ID : " + str(id))
        else:
            return current_user



# Authentification
# ---------------------------------------------------------------------------- #
checker = Checker()
current_user = checker.check_user("0")


# Say hello
# ---------------------------------------------------------------------------- #
Speaker.say("Bonjour, " + current_user.name + " !")


# Success
# ---------------------------------------------------------------------------- #
Debug.LogSuccess("Finished")

