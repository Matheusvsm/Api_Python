from flask import render_template, Blueprint
from __init__ import __init__

controllers = Blueprint("controllers", __name__)

@controllers.route('/register', methods=['GET', 'POST'])
def register():
   return render_template('register.html')

@controllers.route('/login', methods=['GET', 'POST'])
def login():
   return render_template('login.html')

#app.run(debug=True)
app.run(host='201.51.102.81/32')