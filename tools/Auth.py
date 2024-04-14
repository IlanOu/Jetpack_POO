import json
from User import *


# ---------------------------------------------------------------------------- #
#                                 Authenticator                                #
# ---------------------------------------------------------------------------- #


class Authenticator:
    def __init__(self) -> None:
        self.users = []
        self._load_users()

    def _load_users(self):
        with open('./users.json', 'r') as f:
            user_data_dicts = json.load(f)
            self.users = []

            for id, user_data in user_data_dicts.items():
                user_datas = UserDatas(
                    id=id,
                    name=user_data['name'],
                    books_read=user_data['books_read']
                )
                self.users.append(User(user_datas=user_datas))

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
print(current_user.books_read)