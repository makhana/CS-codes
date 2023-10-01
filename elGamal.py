import random
import hashlib
import binascii

def elGamal():
    mess = """This document defines a deterministic digital signature generation
procedure.  Such signatures are compatible with standard Digital
Signature Algorithm (DSA) and Elliptic Curve Digital Signature
Algorithm (ECDSA) digital signatures and can be processed with
unmodified verifiers, which need not be aware of the procedure
described therein.  Deterministic signatures retain the cryptographic
security features associated with digital signatures but can be more
easily implemented in various environments, since they do not need
access to a source of high-quality randomness."""
    alfa = 1000133
    Ya = 60620549947
    q = 100000000003
    m = binascii.crc32(bytes(mess, 'utf-8'))
    Xa = 93275834
    K = 756004217
    s = [8121408200, 31409363618, 17091213583, 9849741372, 12274989154, 31279735200]
    for i in range(0, 3):
        V1 = pow(alfa, m, q)
        V2 = (pow(Ya, s[i * 2], q) * pow(s[i * 2], s[i * 2 + 1], q)) % q
        print(V1 == V2)

    S1 = pow(alfa, K, q)
    S2 = (pow(K, -1, q - 1) * (m - Xa * S1)) % (q - 1)
    print(S1, S2)


def main():
    elGamal()

if __name__ == '__main__':
    main()

