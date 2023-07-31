```python
import sqlite3
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class AuthenticationModel:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def create_user(self, username, password):
        user = User(None, username, password)
        self.cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                            (user.username, user.password_hash))
        self.conn.commit()

    def get_user(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user_data = self.cursor.fetchone()
        if user_data:
            return User(user_data[0], user_data[1], user_data[2])
        return None

    def authenticate_user(self, username, password):
        user = self.get_user(username)
        if user and user.check_password(password):
            return user
        return None
```