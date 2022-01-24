import re

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "

dict = {'.': 'тчк', ',': 'зпт'}

print ('Введите текст')
to_encrypt = input()

def replace_all_to(input_text, dict):
    input_text = input_text.replace(' ', '')
    for i, j in dict.items():
        input_text = input_text.replace(i, j)
    return input_text


def replace_all_from(input_text, dict):
    for i, j in dict.items():
        input_text = input_text.replace(j, i)
    return input_text


def input_for_cipher_short():
    return replace_all_to(to_encrypt, dict)


def input_for_cipher_long():
    return replace_all_to(to_encrypt, dict)


def output_from_decrypted(decrypted_text):
    return replace_all_from(decrypted_text, dict)