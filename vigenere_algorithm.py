def vignere_encrypt(plaintext:str, key:str):
    # fix the plaintext
    new_plaintext = ''
    for letter in plaintext:
        if letter.isalpha():
            new_plaintext += letter

    # algorithm
    ciphertext = ''
    plaintext_list = [ord(p) - 65 for p in new_plaintext]
    key_list = [ord(k) - 65 for k in key]
    n = len(plaintext_list)
    m = len(key_list)
    for i in range(n):
        ciphertext+= chr(65 + (plaintext_list[i] + key_list[i % m]) % 26)

    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ''
    ciphertext_list = [ord(c) - 65 for c in ciphertext]
    key_list = [ord(k) - 65 for k in key]
    n = len(ciphertext_list)
    m = len(key_list)
    for i in range(n):
        plaintext += chr(65 + (ciphertext_list[i] - key_list[i % m]) % 26)

    return plaintext

def main():
    plaintext = "mother is beautiful"
    key = "ambatublou"

    plaintext = plaintext.upper()
    key = key.upper()

    ciphertext = vignere_encrypt(plaintext, key)
    new_plaintext = vigenere_decrypt(ciphertext, key).lower()

    print("original plaintext:", plaintext.lower())
    print("ciphertext:", ciphertext)
    print("decrypted:", new_plaintext)

if __name__ == '__main__':
    main()