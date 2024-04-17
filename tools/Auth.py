from User import *
from Book import *


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



