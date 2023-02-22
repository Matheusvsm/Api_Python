from flask import render_template, request, redirect, url_for
from flask_login import login_required, login_user, logout_user
from models.models import User
from app import app, login_manager, db

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return render_template('register.html', error='Both username and password are required')

        if db.users.find_one({"username": username}):
            return render_template('register.html', error='Username already taken')

        user = User(username, password)
        db.users.insert_one({"username": user.username, "password": user.password_hash})

        return redirect(url_for('controllers.login'))

    return render_template('register.html')

