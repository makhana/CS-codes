def vernam(plaintext_ciphertext:str, key:str):
    result = ""
    for i in range(len(plaintext_ciphertext)):
        result += chr(65 + ((ord(plaintext_ciphertext[i]) - 65) ^ (ord(key[i]) - 65)) % 26)
    return result

def main():
    key = "ababhsdicjboibf"
    plaintext = "motherlovesmeee"

    key = key.upper()
    plaintext = plaintext.upper()
    ciphertext = vernam(plaintext.upper(), key)
    new_plaintext = vernam(ciphertext, key)

    print("original plaintext:", plaintext.lower())
    print("ciphertext:", ciphertext)
    print("decrypted:", new_plaintext.lower())
if __name__ == '__main__':
    main()