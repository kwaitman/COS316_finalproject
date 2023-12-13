from flask_sqlalchemy import SQLAlchemy
from vigenere import encrypt, decrypt

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_encrypted = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_encrypted = encrypt(password)

    def check_password(self, password):
        if (decrypt(self.password_encrypted)) == password:
            return True
        return False