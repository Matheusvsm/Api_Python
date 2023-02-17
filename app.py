from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb+srv://5nsGyX2gWPUACLso:5nsGyX2gWPUACLso@api.6zng7jt.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client["mydb"]
products_collection = db["products"]


@app.route("/products", methods=["GET"])
def get_products():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    query = request.args.get('query', {})

    try:
        products = list(products_collection.find(query).skip((page - 1) * limit).limit(limit))

        if len(products) == 0:
            return jsonify({"message": "No products found"}), 404
        else:
            return jsonify(products), 200

    except:
        return jsonify({"message": "Error processing request"}), 500


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


@app.route("/products/<id>", methods=["PATCH"])
def update_product(id):
    name = request.json.get("name")
    price = request.json.get("price")
    if not name and not price:
        return jsonify({'error': 'The request must have the name or price fields'}), 400

    product = products_collection.find_one({"_id": ObjectId(id)})
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    update_data = {}
    if name:
        update_data["name"] = name
    if price:
        update_data["price"] = price

    products_collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    product = products_collection.find_one({"_id": ObjectId(id)})
    product["_id"] = str(product["_id"])

    return jsonify(product)


@app.route("/products/<id>", methods=["DELETE"])
def delete_product(id):
    result = products_collection.delete_one({"_id": ObjectId(id)})

    if result.deleted_count == 0:
        return jsonify({'error': 'Product not found'}), 404
    else:
        return jsonify({"message": "Product deleted"})


if __name__ == "__main__":
    app.run()

