def cezar_encrypt(plaintext:str, offset:int):
    ciphertext = ""
    for letter in plaintext:
        if(letter.isalpha()):
            if(letter.islower()):
                ciphertext += chr(65 + (ord(letter.upper()) - 65 + offset) % 26).lower()
            else:
                ciphertext += chr(65 + (ord(letter) - 65 + offset) % 26)
        else:
            ciphertext += letter

    return ciphertext

def cezar_decrypt(ciphertext:str, offset:int):
    plaintext = ""
    for letter in ciphertext:
        if (letter.isalpha()):
            if (letter.islower()):
                plaintext += chr(65 + (ord(letter.upper()) - 65 - offset) % 26).lower()
            else:
                plaintext += chr(65 + (ord(letter) - 65 - offset) % 26)
        else:
            plaintext += letter

    return plaintext
def main():
    plaintext = input()
    offset = input()
    ciphertext = cezar_encrypt(plaintext, int(offset))
    new_plaintext = cezar_decrypt(ciphertext, int(offset))

    print("original plaintext:", plaintext)
    print("ciphertext:", ciphertext)
    print("decrypted:", new_plaintext)

if __name__=='__main__':
    main()