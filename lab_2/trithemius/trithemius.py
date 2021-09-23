# -*- coding: utf-8 -*-
 
alphabet: str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
 
def decode(text):
    decode: str = ""
    k = 0
    for position, symbol in enumerate(text):
        index = (alphabet.find(symbol) + k) % len(alphabet)
        decode += alphabet[index]
        k -= 1
    return decode


def encode(text):
    encode = ""
    k = 0
    for position, symbol in enumerate(text):
        index = (alphabet.find(symbol) + k) % len(alphabet)
        encode += alphabet[index]
        k += 1
    return encode

