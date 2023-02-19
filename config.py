from pymongo import MongoClient

client = MongoClient("mongodb+srv://5nsGyX2gWPUACLso:5nsGyX2gWPUACLso@api.6zng7jt.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client["mydb"]