import random

def mono_alpha_encrypt(plaintext:str, key:str):
    key_dict = {}
    ciphertext = ""

    for i in range(26):
        key_dict[chr(97 + i)] = key[i]


    for letter in plaintext:
        if letter.isalpha():
            if letter.islower():
                ciphertext += key_dict[letter]
            else:
                ciphertext += key_dict[letter.lower()].upper()
        else:
            ciphertext += letter

    return ciphertext

def mono_alpha_decrypt(ciphertext:str, key:str):
    inv_key = {}
    plaintext = ""

    for i in range(26):
        inv_key[key[i]] = chr(97 + i)


    for letter in ciphertext:
        if letter.isalpha():
            if letter.islower():
                plaintext += inv_key[letter]
            else:
                plaintext += inv_key[letter.lower()].upper()
        else:
            plaintext += letter

    return plaintext

def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = ''.join(random.sample(alphabet, len(alphabet)))
    plaintext = input()

    ciphertext = mono_alpha_encrypt(plaintext, key)
    new_plaintext = mono_alpha_decrypt(ciphertext, key)

    print("original plaintext:", plaintext)
    print("ciphertext:", ciphertext)
    print("decrypted:", new_plaintext)


if __name__=='__main__':
    main()