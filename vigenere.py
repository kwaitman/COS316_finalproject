SECRET_KEY="SystemsAreFun"

# Adjust the key string to match the length of password
def _adjust_key(pw_length):
    if pw_length == len(SECRET_KEY):
        return SECRET_KEY
    
    if pw_length < len(SECRET_KEY):
        return SECRET_KEY[:pw_length]
    
    repetitions = pw_length // len(SECRET_KEY)
    extra = pw_length % len(SECRET_KEY)
    result = ""
    for _ in range(1, repetitions+1):
        result += SECRET_KEY

    result += SECRET_KEY[:extra]
    return result

# Generates an encrypted password given an inputted string
def encrypt(password):
    key = _adjust_key(len(password))

    pw_ascii = list(bytes(password, 'ascii'))
    key_ascii = list(bytes(key, 'ascii'))

    shift = list()
    for i in range(len(pw_ascii)):
        shift.append((pw_ascii[i] + key_ascii[i]) % 127)
    
    for i in range(len(shift)):
        shift[i] = format(shift[i], '#010b')[2:]
    
    encrypted = ''.join(shift)
    return encrypted

def decrypt(encrypted):
    split = list()
    for i in range(0, len(encrypted), 8):
        split.append(encrypted[i:i+8])

    for i in range(len(split)):
       split[i] = int(split[i], 2)

    key = _adjust_key(len(split))
    key_ascii = list(bytes(key, 'ascii'))

    pw_ascii = list()
    for i in range(len(split)):
        pw_ascii.append((split[i] - key_ascii[i] + 127) % 127)

    decrypted = ''.join(chr(i) for i in pw_ascii)
    return decrypted

if __name__ == '__main__':
    encrypted = encrypt("Hello World")
    print(encrypted)
    decrypted = decrypt(encrypted)
    print(decrypted)