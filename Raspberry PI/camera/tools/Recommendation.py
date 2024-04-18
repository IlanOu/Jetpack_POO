from collections import defaultdict
from Book import BooksManager

class BookRecommender:
    def __init__(self):
        self.books = BooksManager().get_books()
        self.book_index = self.build_book_index(self.books)

    def build_book_index(self, books):
        """
        Crée un dictionnaire inversé pour faciliter les recommandations.
        
        Args:
            books (list): Une liste d'objets Livre.
        
        Returns:
            defaultdict: Un dictionnaire inversé où les clés sont les types/styles de livres
                         et les valeurs sont des listes d'objets Livre.
        """
        book_index = defaultdict(list)
        for book in books:
            for feature in ['type', 'style']:
                book_index[getattr(book, feature)].append(book)
        return book_index

    def recommend_books(self, book, num_recommendations=3):
        """
        Recommande des livres similaires à un livre donné.
        
        Args:
            book (Book): L'objet Livre pour lequel faire des recommandations.
            num_recommendations (int): Le nombre de recommandations à retourner.
        
        Returns:
            list: Une liste d'objets Livre recommandés.
        """
        recommendations = []
        
        for feature in ['type', 'style']:
            for similar_book in self.book_index[getattr(book, feature)]:
                if similar_book.id != book.id and similar_book not in recommendations:
                    recommendations.append(similar_book)
                    if len(recommendations) >= num_recommendations:
                        return recommendations
        
        return recommendations

