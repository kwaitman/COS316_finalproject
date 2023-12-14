SHIFTVALUE = 7
# Generates an encrypted password given an inputted string
def encrypt(password):
    pw_ascii = list(bytes(password, 'ascii'))

    shift = list()
    for i in range(len(pw_ascii)):
        shift.append((pw_ascii[i] + SHIFTVALUE) % 128)
    
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

    pw_ascii = list()
    for i in range(len(split)):
        pw_ascii.append((split[i] - SHIFTVALUE + 128) % 128)

    decrypted = ''.join(chr(i) for i in pw_ascii)
    return decrypted

if __name__ == '__main__':
    encrypted = encrypt("Hello World")
    print(encrypted)
    decrypted = decrypt(encrypted)
    print(decrypted)