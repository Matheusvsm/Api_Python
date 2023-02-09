from pymongo import MongoClient
def get_database():

 CONNECTION_STRING = "mongodb+srv://7bjvhYCvfzwrFrDy:7bjvhYCvfzwrFrDy@apirestaurant.g6hojny.mongodb.net/?retryWrites=true&w=majority"

 client = MongoClient(CONNECTION_STRING)

 print("Conectado ao mongoDb")
 if __name__ == "__main__":   
  
  dbname = get_database()
 
 return client

