def make_key_matrix(key:str):
    # make key_matrix
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key_matrix = [[], [], [], [], []]
    key_set = set()
    i = 0
    j = 0
    for letter in key:
        if letter not in key_set:
            key_set.add(letter)
            key_matrix[i].append(letter)
        j += 1
        if (j == 5):
            i += 1
            j = j % 5

    for a in range(26):
        if alphabet[a] not in key_set:
            if (alphabet[a] == 'j'):
                continue
            key_matrix[i].append(alphabet[a])
            j += 1
            if (j == 5):
                i += 1
                j = j % 5

    return key_matrix

def playfair_encrypt(plaintext:str, key_matrix, filler_char:str):
    ciphertext = ""

    #make pairs of plaintext
    plaintext_pairs = []
    new_plaintext = ""
    for p in plaintext:
        if p.isalpha():
            new_plaintext += p

    i = 0
    while i < len(new_plaintext):
        if(i+1 == len(new_plaintext) or new_plaintext[i] == new_plaintext[i+1]):
            plaintext_pairs.append(new_plaintext[i] + 'x')
            i+=1
        else:
            plaintext_pairs.append(new_plaintext[i] + new_plaintext[i+1])
            i+=2


    if(len(plaintext_pairs[len(plaintext_pairs)-1]) == 1):
        plaintext_pairs[len(plaintext_pairs)-1] = plaintext_pairs[len(plaintext_pairs)-1]+filler_char

    #encryption
    for elem in plaintext_pairs:
        leave = False
        i = 0
        j = 0
        for i in range(len(key_matrix)):
            for j in range(len(key_matrix[i])):
                if key_matrix[i][j] == elem[0]:
                    leave = True
                    break
            if (leave): break
        row1 = i
        column1 = j

        i = 0
        j = 0
        leave = False

        for i in range(len(key_matrix)):
            for j in range(len(key_matrix[i])):
                if key_matrix[i][j] == elem[1]:
                    leave = True
                    break
            if (leave): break

        row2 = i
        column2 = j

        if(row1 == row2):
            ciphertext += key_matrix[row1][(column1 + 1) % 5]
            ciphertext += key_matrix[row2][(column2 + 1) % 5]
        elif(column1 == column2):
            ciphertext += key_matrix[(row1 + 1) % 5][column1]
            ciphertext += key_matrix[(row2 + 1) % 5][column2]
        else:
            ciphertext += key_matrix[row1][column2]
            ciphertext += key_matrix[row2][column1]

    return ciphertext

def playfair_decrypt(ciphertext:str, key_matrix):
    plaintext = ""

    #make pairs of plaintext
    ciphertext_pairs = []

    for i in range(0, len(ciphertext), 2):
        ciphertext_pairs.append(ciphertext[i:i + 2])


    #decryption
    for elem in ciphertext_pairs:
        leave = False
        i = 0
        j = 0
        for i in range(len(key_matrix)):
            for j in range(len(key_matrix[i])):
                if key_matrix[i][j] == elem[0]:
                    leave = True
                    break
            if (leave): break
        row1 = i
        column1 = j

        i = 0
        j = 0
        leave = False
        for i in range(len(key_matrix)):
            for j in range(len(key_matrix[i])):
                if key_matrix[i][j] == elem[1]:
                    leave = True
                    break
            if (leave): break

        row2 = i
        column2 = j

        if(row1 == row2):
            plaintext += key_matrix[row1][(column1 - 1 + 5) % 5]
            plaintext += key_matrix[row2][(column2 - 1 + 5) % 5]
        elif(column1 == column2):
            plaintext += key_matrix[(row1 - 1 + 5) % 5][column1]
            plaintext += key_matrix[(row2 - 1 + 5) % 5][column2]
        else:
            plaintext += key_matrix[row1][column2]
            plaintext += key_matrix[row2][column1]

    if plaintext[len(plaintext) - 1] ==  'x':
        plaintext = plaintext[0: len(plaintext)-1]
    return plaintext

def main():
    filler_char = 'x'
    key = "monarchy"
    plaintext = input()
    key_matrix = make_key_matrix(key)
    ciphertext = playfair_encrypt(plaintext, key_matrix, filler_char)
    new_plaintext = playfair_decrypt(ciphertext, key_matrix)

    print("original plaintext:", plaintext)
    print("ciphertext:", ciphertext)
    print("decrypted:", new_plaintext)
if __name__ == '__main__':
    main()
