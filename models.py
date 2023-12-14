from flask_sqlalchemy import SQLAlchemy
import vigenere
import caesar
import rc4
import time
import cProfile
import pstats
import psutil

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_v_encrypted = db.Column(db.String(128), nullable=False)
    password_c_encrypted = db.Column(db.String(128), nullable=False)
    password_r_encrypted = db.Column(db.String(128), nullable=False)

    def set_password(self, password):

        start_time = time.time()
        self.password_v_encrypted = vigenere.encrypt(password)
        vigenere_time = time.time() - start_time
        print(f"Vigenere encryption time: {vigenere_time} seconds")
        
        start_time = time.time()
        self.password_c_encrypted = caesar.encrypt(password)
        caesar_time = time.time() - start_time
        print(f"Caesar encryption time: {caesar_time} seconds")
        
        start_time = time.time()
        self.password_r_encrypted = rc4.encrypt(password)
        rc4_time = time.time() - start_time
        print(f"RC4 encryption time: {rc4_time} seconds")

    def check_password(self, password):
        if ((vigenere.decrypt(self.password_v_encrypted)) == password) and \
            ((caesar.decrypt(self.password_c_encrypted)) == password) and \
            ((rc4.decrypt(self.password_r_encrypted)) == password):
            return True
        return False