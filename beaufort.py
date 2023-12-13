import vigenere

SECRET_KEY="SystemsAreFun"
a_to_z="abcdefghijklmnopqrstuvwxyz"
z_to_a="zyxwvutsrqponmlkjihgfedcba"

def _transform_password(password):
    # do this algorithm
    a_to_z
def _detransform_password(password):
    # do this algorithm
    z_to_a

# Generates an encrypted password given an inputted string
def encrypt(password):
    transformed = _transform_password(password)
    return vigenere.encrypt(transformed)

def decrypt(encrypted):
    decrypted = vigenere.decrypt(encrypt)
    return _detransform_password(decrypted)

if __name__ == '__main__':
    encrypted = encrypt("Hello World")
    print(encrypted)
    decrypted = decrypt(encrypted)
    print(decrypted)