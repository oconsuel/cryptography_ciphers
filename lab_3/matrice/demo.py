# -*- coding: utf-8 -*-
from matrice import decrypt, encrypt, matrix_mod_inv, alphabet
import numpy as np

inp = input('Введите матрицу в строку через пробел: ')
inp = inp.split(' ')

#3 10 20 20 19 17 23 78 17

key = np.matrix([[int(inp[0]), int(inp[1]), int(inp[2])], [int(inp[3]), int(inp[4]), int(inp[5])], [int(inp[6]), int(inp[7]), int(inp[8])]])
Kinv = matrix_mod_inv(key, len(alphabet))
print ('Введите текст')
to_encrypt = input()
# to_encrypt = 'Вот пример статьи на тысячу символов. Это достаточно маленький текст, оптимально подходящий для карточек товаров в интернет или магазинах или для небольших информационных публикаций. В таком тексте редко бывает более двух или трёх абзацев и обычно один подзаголовок. Но можно и без него. На тысячу символов рекомендовано использовать один или два ключа и одну картину. Текст на тысячу символов это сколько примерно слов? Статистика показывает, что тысяча включает в себя стопятьдесят или двести слов средней величины. Но, если злоупотреблять предлогами, союзами и другими частями речи на один или два символа, то количество слов неизменно возрастает. В копирайтерской деятельности принято считать тысячи с пробелами или без. Учет пробелов увеличивает объем текста примерно на сто или двести символов именно столько раз мы разделяем слова свободным пространством. Считать пробелы заказчики не любят, так как это пустое место. Однако некоторые фирмы и биржи видят справедливым ставить стоимость за тысячу символов с пробелами, считая последние важным элементом качественного восприятия. Согласитесь, читать слитный текст без единого пропуска, никто не будет. Но большинству нужна цена за тысячу знаков без пробелов.'

dict = {'.': 'тчк', ',': 'зпт', '!' : 'ввв', '?' : 'ььь', '–' : 'ъъъ'}

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

print(f'''
Зашифрованный текст:
{encrypt(input_enc(), key).replace(" ", "")}
Расшифрованный текст:
{dec_text(decrypt(encrypt(
    input_enc(), key), Kinv)).replace(" ", "")}
    ''')