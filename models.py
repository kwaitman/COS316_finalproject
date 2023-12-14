from flask_sqlalchemy import SQLAlchemy
import vigenere
import caesar
import rc4

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_v_encrypted = db.Column(db.String(128), nullable=False)
    password_c_encrypted = db.Column(db.String(128), nullable=False)
    password_r_encrypted = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_v_encrypted = vigenere.encrypt(password)
        self.password_c_encrypted = caesar.encrypt(password)
        self.password_r_encrypted = rc4.encrypt(password)
       

    def check_password(self, password):
        if ((vigenere.decrypt(self.password_v_encrypted)) == password) and \
            ((caesar.decrypt(self.password_c_encrypted)) == password) and \
            ((rc4.decrypt(self.password_r_encrypted)) == password):
            return True
        return False