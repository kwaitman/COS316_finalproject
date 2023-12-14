SECRET_KEY = "SystemsAreFun"

def _initialize_keystream(pw_length):
    key_int = list(bytes(SECRET_KEY, 'ascii'))

    key_array = list(range(256))
    
    j = 0
    for i in range(256):
        j = (j + key_array[i] + key_int[i % len(SECRET_KEY)]) % 256
        key_array[i], key_array[j] = key_array[j], key_array[i]
    
    i = 0
    j = 0
    keystream = list(range(pw_length))
    for k in range(pw_length):
        i = (i + 1) % 256
        j = (j + key_array[i]) % 256
        key_array[i], key_array[j] = key_array[j], key_array[i]
        t = (key_array[i] + key_array[j]) % 256
        keystream[k] = key_array[t]
    
    return keystream

def encrypt(password):
    pw_ascii = list(bytes(password, 'ascii'))
    keystream = _initialize_keystream(len(password))

    encrypted = list()
    for i in range(len(pw_ascii)):
        temp = pw_ascii[i]^keystream[i]
        encrypted.append(format(temp, '#010b')[2:])
    
    encrypted = ''.join(encrypted)
    return encrypted

def decrypt(encrypted):
    encrypted_ascii = list()
    for i in range(0, len(encrypted), 8):
        encrypted_ascii.append(int(encrypted[i:i+8], 2))
    
    keystream = _initialize_keystream(len(encrypted_ascii))

    decrypt = list()
    for i in range(len(encrypted_ascii)):
        decrypt.append(encrypted_ascii[i]^keystream[i])
    
    decrypted = ''.join(chr(i) for i in decrypt)
    return decrypted

if __name__ == '__main__':
    encrypted = encrypt("Hello World")
    print(encrypted)
    decrypted = decrypt(encrypted)
    print(decrypted)