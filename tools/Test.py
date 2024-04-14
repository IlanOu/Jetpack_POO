from Debug import Debug
from Auth import Authenticator
from Say import Speaker
from Recommendation import BookRecommender

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


# Recommendation
# ---------------------------------------------------------------------------- #
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
speek = False
if speek:
    text = ""
    text += "Bonjour, " + current_user.name + " !"
    Speaker.say(text)
    
    
    text = ""
    text += f"Recommandations pour '{book.title}' :"
    text += ", ".join(map(lambda x: x.title, recommendations))
    Speaker.say(text)
    
    text = ""
    text += f"Résumé pour '{book.title}' :"
    text += f"{book.summary}"
    
    Speaker.say(text)


# Success
# ---------------------------------------------------------------------------- #
Debug.LogSuccess("Finished")

