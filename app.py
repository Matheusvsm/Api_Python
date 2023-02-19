from flask import Flask, jsonify, render_template
from products import products


app = Flask(__name__)
app.register_blueprint(products)

@app.route('/')
def index():
    return render_template('./templates/index.html')


if __name__ == "__main__":
    app.run()




