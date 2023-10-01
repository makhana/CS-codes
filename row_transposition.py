def row_encrypt(plaintext:str, key:str, filler_char:str):
    matrix = []
    ciphertext = ''

    while len(plaintext) % len(key) != 0:
        plaintext += filler_char

    i = 0
    help_array = []
    for p in plaintext:
        help_array.append(p)
        i += 1
        if(i == len(key)):
            i = i % len(key)
            matrix.append(help_array)
            help_array = []

    for j in range(1, len(key)+1):
        for i in range(len(matrix)):
            ciphertext += matrix[i][key.index(str(j))]

    return ciphertext

def row_decrypt(ciphertext:str, key:str):
    matrix = []
    plaintext = ''

    i = 0
    help_array = []
    ciphertext_groups = []
    for i in range(0, len(ciphertext), len(ciphertext) // len(key)):
        ciphertext_groups.append(list(ciphertext[i:i+len(key)]))

    print(ciphertext_groups)
    for i in range(0, len(key)):
        matrix.append(ciphertext_groups[int(key[i])-1]) # ZIMENI MSM DA NIJE DOBRA LOGIKA UZIMANJA INDEKSA KLJUCEVA
    print(matrix)

    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            plaintext += matrix[i][j]

    return plaintext

def main():
    plaintext = "mamavolimilovanaa"
    key = "2134"
    ciphertext = row_encrypt(plaintext, key, 'x')
    new_plaintext = row_decrypt(ciphertext, key)

    print("original plaintext:", plaintext.lower())
    print("ciphertext:", ciphertext)
    print("decrypted:", new_plaintext)

if __name__ == '__main__':
    main()