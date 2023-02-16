from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://7bjvhYCvfzwrFrDy:bjvhYCvfzwrFrDy@cluster0.jmctn5d.mongodb.net")
db = client["mydb"]
products_collection = db["products"]

@app.route("/products", methods=["GET"])
def get_products():
    products = list(products_collection.find({}))
    return jsonify(products)

@app.route("/products", methods=["POST"])
def create_product():
    name = request.json["name"]
    price = request.json["price"]
    product = {"name": name, "price": price}
    products_collection.insert_one(product)
    return jsonify(product)

@app.route("/products/<id>", methods=["PUT"])
def update_product(id):
    name = request.json["name"]
    price = request.json["price"]
    product = products_collection.find_one({"_id": id})
    product["name"] = name
    product["price"] = price
    products_collection.save(product)
    return jsonify(product)

@app.route("/products/<id>", methods=["DELETE"])
def delete_product(id):
    products_collection.delete_one({"_id": id})
    return jsonify({"message": "Product deleted"})

if __name__ == "__main__":
    app.run()
