from config import db
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_by_username(username):
        user_data = db.users.find_one({"username": username})
        if user_data:
            return User(user_data["username"], user_data["password"])
        else:
            return None

