
import random
import time


def cipher(key, clearText):
    alphabet_lower = ['а', 'б', 'в', 'г', 'д',
                      'е', 'ж', 'з', 'и', 'к',
                      'л', 'м', 'н', 'о', 'п',
                      'р', 'с', 'т', 'у', 'ф',
                      'х', 'ц', 'ч', 'ш', 'щ',
                      'ь', 'ы', 'э', 'ю', 'я']

    text = clearText
    
    new_alphabet = []  
    for i in range(len(key)):
        new_alphabet.append(key[i]) 
    for i in range(len(alphabet_lower)):
        bool_buff = False 
        for j in range(len(key)):
            if alphabet_lower[i] == key[j]: # Если символ ключа = символ алфавита
                bool_buff = True
                break
        if bool_buff == False: # Если символ ключа /= символ алфавита
            new_alphabet.append(alphabet_lower[i])  
    
    # Формируем матричный алфавит
    mtx_abt_j = []  # Заготовка под матричный алфавит по j
    counter = 0
    for j in range(5):
        mtx_abt_i = []  # Заготовка под матричный алфавит по i в j
        for i in range(6):
            # Добавляем букву в матрицу
            mtx_abt_i.append(new_alphabet[counter])
            counter = counter + 1
        mtx_abt_j.append(mtx_abt_i)
    print('\n'.join(map(str, mtx_abt_j)))
    if len(text) % 2 == 1:  # Если последняя биграмма состоит из одной буквы, то добавляем букву в конец
        text = text + "я"
    
    # Шифруем
    enc_text = ""  
    for t in range(0, len(text), 2): 
        flag = True  # флаг для выхода из всех циклов
        for j_1 in range(5):
            if flag == False:
                break
            for i_1 in range(6):
                if flag == False:
                    break
                if mtx_abt_j[j_1][i_1] == text[t]:
                    for j_2 in range(5):
                        if flag == False:
                            break
                        for i_2 in range(6):
                            if mtx_abt_j[j_2][i_2] == text[t+1]:
                                # Если буквы по диагонали
                                if j_1 != j_2 and i_1 != i_2:
                                    enc_text = enc_text + \
                                        mtx_abt_j[j_1][i_2] + \
                                        mtx_abt_j[j_2][i_1]
                                # Если буквы на одной строке
                                elif j_1 == j_2 and i_1 != i_2:
                                    # %6 для предотвращения выхода за строку
                                    enc_text = enc_text + \
                                        mtx_abt_j[j_1][(i_1+1) % 6] + \
                                        mtx_abt_j[j_2][(i_2+1) % 6]
                                # Если буквы в одном столбце
                                elif j_1 != j_2 and i_1 == i_2:
                                    # %5 для предотвращения выхода за столбец
                                    enc_text = enc_text + \
                                        mtx_abt_j[(j_1+1) % 5][i_1] + \
                                        mtx_abt_j[(j_2+1) % 5][i_2]
                                # Если буквы совпадают
                                elif j_1 == j_2 and i_1 == i_2:
                                    enc_text = enc_text + \
                                        mtx_abt_j[j_1][i_1] + \
                                        mtx_abt_j[j_1][i_1]
                                # print(
                                #     " {}{} -> {}{}".format(text[t], text[t+1], enc_text[t], enc_text[t+1]))
                                flag = False
                                break
    print("\n Зашифрованный текст = {} \n".format(enc_text))
    return enc_text


def decipher(key, clearText):
    alphabet_lower = ['а', 'б', 'в', 'г', 'д',
                      'е', 'ж', 'з', 'и', 'к',
                      'л', 'м', 'н', 'о', 'п',
                      'р', 'с', 'т', 'у', 'ф',
                      'х', 'ц', 'ч', 'ш', 'щ',
                      'ь', 'ы', 'э', 'ю', 'я']

    text = clearText
    # Формируем алфавит
    new_alphabet = []  
    for i in range(len(key)):
        new_alphabet.append(key[i])  
    for i in range(len(alphabet_lower)):
        bool_buff = False  
        for j in range(len(key)):
            
            if alphabet_lower[i] == key[j]:
                bool_buff = True
                break
        if bool_buff == False:  
            new_alphabet.append(alphabet_lower[i])  
    mtx_abt_j = []  # Заготовка под матричный алфавит по j
    counter = 0
    for j in range(5):
        mtx_abt_i = []  # Заготовка под матричный алфавит по i в j
        for i in range(6):
            # Добавляем букву в матрицу
            mtx_abt_i.append(new_alphabet[counter])
            counter = counter + 1
        mtx_abt_j.append(mtx_abt_i)
    if len(text) % 2 == 1:  # Если последняя биграмма состоит из одной буквы, то добавляем букву в конец
        text = text + "я"

    # Расшифровываем
    enc_text = ""
    for t in range(0, len(text), 2):
        flag = True  # флаг для выхода из всех циклов
        for j_1 in range(5):
            if flag == False:
                break
            for i_1 in range(6):
                if flag == False:
                    break
                if mtx_abt_j[j_1][i_1] == text[t]:
                    for j_2 in range(5):
                        if flag == False:
                            break
                        for i_2 in range(6):
                            if mtx_abt_j[j_2][i_2] == text[t+1]:
                                # Если буквы по диагонали
                                if j_1 != j_2 and i_1 != i_2:
                                    enc_text = enc_text + \
                                        mtx_abt_j[j_1][i_2] + \
                                        mtx_abt_j[j_2][i_1]
                                # Если буквы на одной строке
                                elif j_1 == j_2 and i_1 != i_2:
                                    # %6 для предотвращения выхода за строку
                                    enc_text = enc_text + \
                                        mtx_abt_j[j_1][(i_1-1) % 6] + \
                                        mtx_abt_j[j_2][(i_2-1) % 6]
                                # Если буквы в одном столбце
                                elif j_1 != j_2 and i_1 == i_2:
                                    # %5 для предотвращения выхода за столбец
                                    enc_text = enc_text + \
                                        mtx_abt_j[(j_1-1) % 5][i_1] + \
                                        mtx_abt_j[(j_2-1) % 5][i_2]
                                # Если буквы совпадают
                                elif j_1 == j_2 and i_1 == i_2:
                                    enc_text = enc_text + \
                                        mtx_abt_j[j_1][i_1] + \
                                        mtx_abt_j[j_1][i_1]
                                # print(
                                #     " {}{} -> {}{}".format(text[t], text[t+1], enc_text[t], enc_text[t+1]))
                                flag = False
                                break
    print("\n Расшифрованный текст = {}\n ".format(enc_text))
    return enc_text
