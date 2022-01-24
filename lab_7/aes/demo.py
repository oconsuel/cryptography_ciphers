if __name__ == '__main__':

    import os
    import time

    import aes
    
    print('Шаг 1:')
    while True:
        print('Нажмите 1 для шифрования, 2 для дешифрования')
        way = input()
        if way not in ['1', '2']:
            print('Неверный ввод')
            continue
        else:
            break
    print()

    print('Шаг 2:')
    while True:
        print('Введите полное имя файла')
        input_path = os.path.abspath(input())

        if os.path.isfile(input_path):
            break
        else:
            print('Неверный ввод')
            continue
    print()

    print('Шаг 3:')
    while True:
        print('Введите секретное слово(ключ) меньше 16 символов')
        key = input()
        
        if len(key) > 16:
            print('Слишком длинный ключ, введите еще раз')
            continue
        
        for symbol in key:
            if ord(symbol) > 0xff:
                print('Используйте только латинские буквы и цифры')
                continue
        
        break

    time_before = time.time()

    # Input data
    with open(input_path, 'rb') as f:
        data = f.read()    

    if way == '1':
        crypted_data = []
        temp = []
        for byte in data:
            temp.append(byte)
            if len(temp) == 16:
                crypted_part = aes.encrypt(temp, key)
                crypted_data.extend(crypted_part)
                del temp[:]
        else:
            #padding v1
            # crypted_data.extend(temp)

            # padding v2
            if 0 < len(temp) < 16:
                empty_spaces = 16 - len(temp)
                for i in range(empty_spaces - 1):
                    temp.append(0)
                temp.append(1)
                crypted_part = aes.encrypt(temp, key)
                crypted_data.extend(crypted_part)

        out_path = os.path.join(os.path.dirname(input_path) , 'crypted_' + os.path.basename(input_path))

        # Ounput data
        with open(out_path, 'xb') as ff:
            ff.write(bytes(crypted_data))

    else: # if way == '2'
        decrypted_data = []
        temp = []
        for byte in data:
            temp.append(byte)
            if len(temp) == 16:
                decrypted_part = aes.decrypt(temp, key)
                decrypted_data.extend(decrypted_part)
                del temp[:] 
        else:
            #padding v1
            # decrypted_data.extend(temp)
            
            # padding v2
            if 0 < len(temp) < 16:
                empty_spaces = 16 - len(temp)
                for i in range(empty_spaces - 1):
                    temp.append(0)
                temp.append(1)
                decrypted_part = aes.encrypt(temp, key)
                decrypted_data.extend(crypted_part) 

        out_path = os.path.join(os.path.dirname(input_path) , 'decrypted_' + os.path.basename(input_path))

        # Ounput data
        with open(out_path, 'xb') as ff:
            ff.write(bytes(decrypted_data))

    time_after = time.time()
