# -*- coding:utf-8 -*-

import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e,r):
    for i in range(r):
        if((e*i)%r == 1):
            return i

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    #n = pq
    n = p * q

    phi = (p-1) * (q-1)

    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)
    

if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    print("RSA")
    p = int(input("Введите p: "))
    q = int(input("Введите q: "))
    public, private = generate_keypair(p, q)
    print("Публичный ключ: ", public ,"Секретный ключ: ", private)
    message = input("Введите сообщение: ")
    encrypted_msg = encrypt(private, message)
    print("Зашифрованное сообщение: ")
    print(''.join([str(x) for x in encrypted_msg]))
    print("Расшифрованное сообщение: ")
    print(decrypt(public, encrypted_msg))