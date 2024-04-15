from toolbox.Singleton import singleton


# ---------------------------------------------------------------------------- #
#                                   BooksDatas                                 #
# ---------------------------------------------------------------------------- #

class BookDatasProtocole:
    def __init__(self, id: str, title: str, author: str, summary: str, type: str, style: str):
        self.id = id
        self.title = title
        self.author = author
        self.summary = summary
        self.type = type
        self.style = style


class BookDatas(BookDatasProtocole):
    def __init__(self, id: str, title: str, author: str, summary: str, type: str, style: str):
        self.id = id
        self.title = title
        self.author = author
        self.summary = summary
        self.type = type
        self.style = style



# ---------------------------------------------------------------------------- #
#                                     Book                                     #
# ---------------------------------------------------------------------------- #

class BookProtocol:
    def __init__(self, book_datas: BookDatas):
        self.id = book_datas.id
        self.title = book_datas.title
        self.author = book_datas.author
        self.summary = book_datas.summary
        self.type = book_datas.type
        self.style = book_datas.style

class Book(BookProtocol):
    def __init__(self, book_datas: BookDatas):
        self.id = book_datas.id
        self.title = book_datas.title
        self.author = book_datas.author
        self.summary = book_datas.summary
        self.type = book_datas.type
        self.style = book_datas.style





# ---------------------------------------------------------------------------- #
#                                 Books Manager                                #
# ---------------------------------------------------------------------------- #

@singleton
class BooksManager:
    def __init__(self):
        self.books = []
        self._create_books()

    def _create_books(self):
        import json
                
        with open('./books.json', 'r', encoding='utf-8') as f:
            book_data_dicts = json.load(f)
           
            for id, book_data in book_data_dicts.items():
                book_datas = BookDatas(
                    id=id,
                    title=book_data["title"],
                    author=book_data["author"],
                    summary=book_data["summary"],
                    type=book_data["type"],
                    style=book_data["style"]
                )
                
                self.books.append(Book(book_datas=book_datas))
    
    
    def get_book_by_id(self, id):
        for book in self.books:
            if book.id == id:
                return book
        return None
    
    
    def get_books(self):
        return self.books

    def reload_books(self):
        self.books = []
        self._create_books()