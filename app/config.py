from pymongo import MongoClient

client = MongoClient("mongodb+srv://matheusmm:matheusmm@api.dhjd4xd.mongodb.net/?retryWrites=true&w=majority")
db = client["mydb"]