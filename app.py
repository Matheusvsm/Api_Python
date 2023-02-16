from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb+srv://7bjvhYCvfzwrFrDy:7bjvhYCvfzwrFrDy@cluster0.jmctn5d.mongodb.net/mydb?retryWrites=true&w=majority")
db = client["mydb"]
products_collection = db["products"]

@app.route("/products", methods=["GET"])
def get_products():
    products = list(products_collection.find({}))
    return jsonify(products)

@app.route("/products", methods=["POST"])
def create_product():
    if not request.json or not 'name' in request.json or not 'price' in request.json:
        return jsonify({'error': 'The request must have the name and price fields'}), 400

    name = request.json["name"]
    price = request.json["price"]
    product = {"name": name, "price": price}
    result = products_collection.insert_one(product)
    product["_id"] = str(result.inserted_id)
    return jsonify(product)

@app.route("/products/<id>", methods=["PUT"])
def update_product(id):
    if not request.json or not 'name' in request.json or not 'price' in request.json:
        return jsonify({'error': 'The request must have the name and price fields'}), 400

    name = request.json["name"]
    price = request.json["price"]
    product = products_collection.find_one({"_id": ObjectId(id)})
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    products_collection.update_one({"_id": ObjectId(id)}, {"$set": {"name": name, "price": price}})
    product = products_collection.find_one({"_id": ObjectId(id)})
    product["_id"] = str(product["_id"])
    return jsonify(product)

@app.route("/products/<id>", methods=["DELETE"])
def delete_product(id):
    result = products_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify({"message": "Product deleted"})

if __name__ == "__main__":
    app.run()

