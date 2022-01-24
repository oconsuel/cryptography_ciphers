import numpy as np
def encrypt(text, key):
    s_box = list(range(256)) # список в 256
    j = 0 
    for i, s in enumerate(s_box): # создание коллеции (0, 1), (0,2)...
        j = (j + s + ord(key[i % len(key)])) % 256 # Шифрование
        s_box[i], s_box[j] = s_box[j], s_box[i] # перестановка 
    i = j = 0
    out = list()
    for char in text:
        i = (i + 1) % 256 # смещение на 1
        j = (j + s_box[i]) % 256 # смещение на показатель i
        s_box[i], s_box[j] = s_box[j], s_box[i] #перестановка
        g = s_box[(s_box[i] + s_box[j]) % 256] # сложение строк 
        out.append(chr(ord(char) ^ g)) #вывод
    return out
f = open('s_blok.txt', 'r')
S_box = f.read()
S_box_split = S_box.split(" ")
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
j = []
for i in range(len(S_box_split)):
    if i >= 0 and i <= 15:
        a.append(S_box_split[i])
    elif i >= 16 and i <= 31:
        b.append(S_box_split[i])
    elif i >= 32 and i <= 47:
        c.append(S_box_split[i])
    elif i >= 48 and i <= 63:
        d.append(S_box_split[i])
    elif i >= 64 and i <= 79:
        e.append(S_box_split[i])
    elif i >= 80 and i <= 95:
        f.append(S_box_split[i])
    elif i >= 96 and i <= 111:
        g.append(S_box_split[i])
    elif i >= 112 and i <= 127:
        h.append(S_box_split[i])
    elif i >= 128 and i <= 143:
        j.append(S_box_split[i])
S_box_matr = np.matrix([a, b, c, d, e, f, g, h, j])

def decrypt(text, key):
    s_box = list(range(256))
    j = 0
    for i, s in enumerate(s_box):
        j = (j + s + ord(key[i % len(key)])) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
    i = j = 0
    out = list()
    for char in text:
        i = (i + 1) % 256
        j = (j + s_box[i]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
        g = s_box[(s_box[i] + s_box[j]) % 256]
        out.append(chr(ord(char) ^ g))
    return out


def main():
    message = "Вот пример статьи на тысячу символов. Это достаточно маленький текст, оптимально подходящий для карточек товаров в интернет или магазинах или для небольших информационных публикаций. В таком тексте редко бывает более двух или трёх абзацев и обычно один подзаголовок. Но можно и без него. На тысячу символов рекомендовано использовать один или два ключа и одну картину. Текст на тысячу символов это сколько примерно слов? Статистика показывает, что тысяча включает в себя стопятьдесят или двести слов средней величины. Но, если злоупотреблять предлогами, союзами и другими частями речи на один или два символа, то количество слов неизменно возрастает. В копирайтерской деятельности принято считать тысячи с пробелами или без. Учет пробелов увеличивает объем текста примерно на сто или двести символов именно столько раз мы разделяем слова свободным пространством. Считать пробелы заказчики не любят, так как это пустое место. Однако некоторые фирмы и биржи видят справедливым ставить стоимость за тысячу символов с пробелами, считая последние важным элементом качественного восприятия. Согласитесь, читать слитный текст без единого пропуска, никто не будет. Но большинству нужна цена за тысячу знаков без пробелов."
    secret_key = "Ключ"
    print ('Секретный ключ:\n', secret_key)
    print ('Исходное сообщение:\n', message)
    crypted_message = encrypt(message, secret_key)
    print ('Зашифрованное сообщение:\n', crypted_message)
    print ('Расшифрованное сообщение:\n', decrypt(crypted_message, secret_key))
    


if __name__ == '__main__':
    main()
