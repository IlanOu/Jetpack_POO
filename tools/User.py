# ---------------------------------------------------------------------------- #
#                                   UsersDatas                                 #
# ---------------------------------------------------------------------------- #

class UserDatasProtocole:
    def __init__(self, id: str, name: str, books_read: list):
        self.id = id
        self.name = name
        self.books_read = books_read

class UserDatas(UserDatasProtocole):
    def __init__(self, id: str, name: str, books_read: list):
        self.id = id
        self.name = name
        self.books_read = books_read



# ---------------------------------------------------------------------------- #
#                                     User                                     #
# ---------------------------------------------------------------------------- #

class UserProtocol:
    def __init__(self, user_datas: UserDatas):
        self.id = user_datas.id
        self.name = user_datas.name
        self.books_read = user_datas.books_read

class User(UserProtocol):
    def __init__(self, user_datas: UserDatas):
        self.id = user_datas.id
        self.name = user_datas.name
        self.books_read = user_datas.books_read