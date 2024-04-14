from Book import *
from toolbox.Singleton import singleton



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



# ---------------------------------------------------------------------------- #
#                                 User Manager                                 #
# ---------------------------------------------------------------------------- #

@singleton
class UserManager:
    def __init__(self):
        self.users = []
        self._create_users()
    

    def _create_users(self):
        import json
        
                
        with open('./users.json', 'r', encoding='utf-8') as f:
            user_data_dicts = json.load(f)
           
          
            for id, user_data in user_data_dicts.items():
                # books_read = BooksManager().get()
                
                books_read_objects = []
                
                for book in user_data["books_read"]:
                    book_object = BooksManager().get_book_by_id(book)
                    if (book_object is not None):
                        books_read_objects.append(book_object)
                
                user_datas = UserDatas(
                    id=id,
                    name=user_data['name'],
                    books_read=books_read_objects
                )
                
                self.users.append(User(user_datas=user_datas))
    
    def get_user_by_id(self, id):
        for user in self.users:
            if user.id == id:
                return user
        return None
    
    
    def get_users(self):
        return self.users

    def reload_users(self):
        self.users = []
        self._create_users()
