from .User import *
from .Book import *


# ---------------------------------------------------------------------------- #
#                                 Authenticator                                #
# ---------------------------------------------------------------------------- #


class Authenticator:
    def __init__(self):
        pass
        
    def authenticate(self, id: str):
        UserManager().reload_users()
        self.users = UserManager().get_users()
        for user in self.users:
            if user.id.strip() == id.strip():
                return user
        


