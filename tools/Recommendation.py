import json
from collections import defaultdict

class BookRecommender:
    def __init__(self, file_path):
        self.books = self.load_books(file_path)
        self.book_index = self.build_book_index(self.books)

    def load_books(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def build_book_index(self, books):
        book_index = defaultdict(list)
        for book_id, book_data in books.items():
            for feature in ['type', 'style']:
                book_index[book_data[feature]].append(book_id)
        return book_index

    def recommend_books(self, book_id, num_recommendations=3):
        book_data = self.books[book_id]
        recommendations = []
        
        for feature in ['type', 'style']:
            for similar_book_id in self.book_index[book_data[feature]]:
                if similar_book_id != book_id and similar_book_id not in recommendations:
                    recommendations.append(similar_book_id)
                    if len(recommendations) >= num_recommendations:
                        return recommendations
        
        return recommendations

# Exemple d'utilisation
recommender = BookRecommender('./books.json')
book_id = 'b-6'
recommendations = recommender.recommend_books(book_id)

print(f"Recommandations pour le livre '{recommender.books[book_id]['title']}' :")
for rec_id in recommendations:
    print(f"- {recommender.books[rec_id]['title']} (par {recommender.books[rec_id]['author']})")