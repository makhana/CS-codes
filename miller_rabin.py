def miller_rabin(n: int, a: int):
    q = n-1
    k = 0
    while not q & 1:
        k += 1
        q >>= 1

    if pow(a, q, n) == 1 :
        return True

    for j in range(0, k):
        if pow(a, pow(2, j) * q, n) == n-1:
            return True

    return False

def main():
    n = input()
    a = input()
    print(miller_rabin(int(n), int(a)))

if __name__ == '__main__':
    main()