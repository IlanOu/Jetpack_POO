from User import *
from Book import *
from Debug import Debug

Debug.prefixActive = False

# ---------------------------------------------------------------------------- #
#                                 Authenticator                                #
# ---------------------------------------------------------------------------- #


class Authenticator:
    def __init__(self) -> None:
        self.users = UserManager().get_users()

    def authenticate(self, id: str):
        for user in self.users:
            if user.id == id:
                return user
        return None



# ---------------------------------------------------------------------------- #
#                                     Test                                     #
# ---------------------------------------------------------------------------- #


# Authentification
# ---------------------------------------------------------------------------- #
authenticator = Authenticator()
current_user = authenticator.authenticate("1")
Debug.LogSuccess(current_user.books_read[1].title)