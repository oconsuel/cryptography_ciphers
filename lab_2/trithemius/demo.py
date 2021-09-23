# -*- coding: utf-8 -*-
from trithemius import decode, encode


print ('Введите текст')
to_encrypt = input()
# to_encrypt = 'Вот пример статьи на тысячу символов. Это достаточно маленький текст, оптимально подходящий для карточек товаров в интернет или магазинах или для небольших информационных публикаций. В таком тексте редко бывает более двух или трёх абзацев и обычно один подзаголовок. Но можно и без него. На тысячу символов рекомендовано использовать один или два ключа и одну картину. Текст на тысячу символов это сколько примерно слов? Статистика показывает, что тысяча включает в себя стопятьдесят или двести слов средней величины. Но, если злоупотреблять предлогами, союзами и другими частями речи на один или два символа, то количество слов неизменно возрастает. В копирайтерской деятельности принято считать тысячи с пробелами или без. Учет пробелов увеличивает объем текста примерно на сто или двести символов именно столько раз мы разделяем слова свободным пространством. Считать пробелы заказчики не любят, так как это пустое место. Однако некоторые фирмы и биржи видят справедливым ставить стоимость за тысячу символов с пробелами, считая последние важным элементом качественного восприятия. Согласитесь, читать слитный текст без единого пропуска, никто не будет. Но большинству нужна цена за тысячу знаков без пробелов.'
# пprint ('Введите значение ключа')
# keyword = input()

dict = {'.': 'тчк', ',': 'зпт'}

def replace(to_encrypt, dict):
    to_encrypt = to_encrypt.replace(' ', '')
    for i, j in dict.items():
        to_encrypt = to_encrypt.replace(i, j)
    return to_encrypt

def replace2(to_decrypt, dict):
    for i, j in dict.items():
        to_decrypt = to_decrypt.replace(j, i)
    return to_decrypt

# def input_for_cipher_short():
#     return replace(file_to_string('short.txt'), dict)

def input_enc():
    return replace(to_encrypt, dict)

def dec_text(decrypted_text):
    return replace2(decrypted_text, dict)

to_encrypt = to_encrypt.lower()

print(f'''
{encode(input_enc())}
Расшифрованный текст:
{dec_text(decode(encode(
    input_enc())))}
    ''')
# encrypted_msg = trithemius_encode (to_encrypt)
# print(f'\nЗашифрованный вид: \n{encrypted_msg}\n')

# demo = trithemius_decode(encrypted_msg)
# print(f'Дешиврованный вид: \n{demo}')