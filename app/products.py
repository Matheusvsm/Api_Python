from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from bson import json_util
from config import db

products = Blueprint("products", __name__, url_prefix="/products")


@products.route("")
def get_products():
    try:
        products = list(db.products.find())

        return json_util.dumps(products), 200, {'Content-Type': 'application/json'}

    except Exception as e:
        return jsonify({"message": f"Error processing request: {str(e)}"}), 500


@products.route("", methods=["POST"])
def create_product():
    if not request.json or not 'name' in request.json or not 'price' in request.json:
        return jsonify({'error': 'The request must have the name and price fields'}), 400

    name = request.json["name"]
    price = request.json["price"]
    product = {"name": name, "price": price}

    result = db.products.insert_one(product)
    product["_id"] = str(result.inserted_id)

    return jsonify(product)


@products.route("/<id>", methods=["PATCH"])
def update_product(id):
    name = request.json.get("name")
    price = request.json.get("price")
    if not name and not price:
        return jsonify({'error': 'The request must have the name or price fields'}), 400

    product = db.products.find_one({"_id": ObjectId(id)})
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    update_data = {}
    if name:
        update_data["name"] = name
    if price:
        update_data["price"] = price

    db.products.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    product = db.products.find_one({"_id": ObjectId(id)})
    product["_id"] = str(product["_id"])

    return jsonify(product)


@products.route("/<id>", methods=["DELETE"])
def delete_product(id):
    result = db.products.delete_one({"_id": ObjectId(id)})

    if result.deleted_count == 0:
        return jsonify({'error': 'Product not found'}), 404
    else:
        return jsonify({"message": "Product deleted"})
