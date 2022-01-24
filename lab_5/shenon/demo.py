# -*- coding: utf-8 -*-
from shenon import encode, decode
import numpy as np

key = input('Пожалуйста, введите ключ: ')

print ('Пожалуйства, введите текст: ')
to_encrypt = input()

dict = {'.': 'тчк', ',': 'зпт', '!' : 'вск', '?' : 'впр'}

def replace(to_encrypt, dict):
    to_encrypt = to_encrypt.replace(' ', '')
    for i, j in dict.items():
        to_encrypt = to_encrypt.replace(i, j)
    return to_encrypt

def replace2(to_decrypt, dict):
    for i, j in dict.items():
        to_decrypt = to_decrypt.replace(j, i)
    return to_decrypt

def input_enc():
    return replace(to_encrypt, dict)

def dec_text(decrypted_text):
    return replace2(decrypted_text, dict)

to_encrypt = to_encrypt.lower()

txt_encoded = encode(input_enc())
txt_decoded = dec_text(decode(txt_encoded[0], txt_encoded[1]))

print(f'''
Результат шифровки: 
{txt_encoded}
Результат расшифровки:
{txt_decoded}
    ''')
