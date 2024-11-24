# Запросы:

def find(query):
    list_of_books = db.books.find(query)
    for book in list_of_books:
        print(book)

query_0 = {'price': {'$gt': 30, '$lt': 60}}
find(query_0)