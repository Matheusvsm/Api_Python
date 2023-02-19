from flask import Flask, jsonify
from products import products


app = Flask(__name__)
app.register_blueprint(products)

if __name__ == "__main__":
    app.run()




