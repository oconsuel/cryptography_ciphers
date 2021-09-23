def decode(msg, key):
    
    decrypted = ''
    alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    offset = 0
    for ix in range(len(msg)):
        if msg[ix] not in alph: #проверка на соответствие алфавиту
            output = msg[ix] #возврат исходного значения
            offset += -1
        #если выходит за массив алфавита
        elif (alph.find(msg[ix])) > (len(alph) - 
                            # найти позвицию буквы
                            (alph.find(key[((ix + offset) % len(key))])) - 1):
            output = alph[(alph.find(msg[ix]) - 
                            (alph.find(key[((ix + offset) % len(key))]))) % 33]
        else:
            output = alph[alph.find(msg[ix]) - 
                                (alph.find(key[((ix + offset) % len(key))]))]
        decrypted += output
    return decrypted


def encode(msg, key):
    ''' INPUT: str (unencrypted), key (used w tabula recta to encrypt)
        OUTPUT: str (encrypted)
    '''
    encoded = ''
    alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    offset = 0
    for ix in range(len(msg)):
        if msg[ix] not in alph:
            output = msg[ix]
            offset += -1
        elif (alph.find(msg[ix])) > (len(alph) - 
                            (alph.find(key[((ix + offset) % len(key))])) - 1):
            output = alph[(alph.find(msg[ix]) + 
                            (alph.find(key[((ix + offset) % len(key))]))) % 33]
        else:
            output = alph[alph.find(msg[ix]) + 
                                (alph.find(key[((ix + offset) % len(key))]))]
        encoded += output
    return encoded