from flask import Flask, jsonify, render_template, url_for
from products import products
from flask_login import LoginManager
from controllers import controllers

app = Flask(__name__, template_folder='/templates')
app.register_blueprint(products)


login_manager = LoginManager(app)



