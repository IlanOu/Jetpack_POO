from Debug import Debug
from Auth import Authenticator
from Say import Speaker
from Recommendation import BookRecommender
from Book import BooksManager

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



# Say hello
# ---------------------------------------------------------------------------- #
Speaker.say("Bonjour, " + current_user.name + " !")
Speaker.say(f"Recommandations pour '{book.title}' :")
Speaker.say(", ".join(map(lambda x: x.title, recommendations)))



# Success
# ---------------------------------------------------------------------------- #
Debug.LogSuccess("Finished")

