from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")

db = client["database"] # создаем базу данных
collection = db["books"] # создаем коллекцию данных

with open('books.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

collection.insert_many(data)  # добавили данные в MongoDB

def find(query):
    list_of_books = db.books.find(query)
    for book in list_of_books:
        print(book)

query_0 = {'price': {'$gt': 30, '$lt': 60}} # запрос находит книги, цена которых больше 30, но меньше 60
find(query_0)

# query_1 = {'title': {'$regex': '[Ll]ight | [Ee]nd'}} # запрос находит книги, название которых содержит слова L(l)ight или E(e)nd
# find(query_1)

# query_2 = {"stock": {"$in": ["In stock (1 available)", "In stock (2 available)"]}} # запрос находит книги, которые есть в наличии в количестве 1 или 2
# find(query_2)