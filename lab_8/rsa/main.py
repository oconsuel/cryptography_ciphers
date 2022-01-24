from math import gcd
#инициализация алфавита
alphabet_lower = {'а':0, 'б':1, 'в':2, 'г':3, 'д':4,
                  'е':5, 'ж':6, 'з':7, 'и':8, 'й':9,
                  'к':10, 'л':11, 'м':12, 'н':13, 'о':14,
                  'п':15, 'р':16, 'с':17, 'т':18, 'у':19,
                  'ф':20, 'х':21, 'ц':22, 'ч':23, 'ш':24,
                  'щ':25, 'ъ':26, 'ы':27, 'ь':28, 'э':29,
                  'ю':30, 'я':31, ' ':32, ",":33, ".":34
                  }

#проверка на простое число
def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n
#расширенный алгоритм Евклида или (e**-1) mod fe
def modInverse(e,el):
    e = e % el
    for x in range(1,el):
        if ((e * x) % el == 1):
            return x
    return 1

#инициализация p,q,e,n
p = int(input("Введите p: "))
print(IsPrime(p))
q = int(input("Введите q: "))
print(IsPrime(q))
n = p * q
print("N =",n)
el = (p-1) * (q-1)
print("El =",el)
e = 257
print("E =",e)
if gcd(e,el) == 1:
    print(gcd(e,el),"E подходит")
else:
    print(gcd(e,el),"False")
#нахождение секретной экспоненты D
d = modInverse(e,el)
print("D =",d)
print("Открытый ключ e={} n={}".format(e,n))
print("Секретный ключ d={} n={}".format(d,n))
#хэширование сообщения
msg = input("Введите сообщение:")
msg_list = list(msg)
alpha_code_msg = list()
for i in range(len(msg_list)):
    alpha_code_msg.append(int(alphabet_lower.get(msg_list[i])))
print("Длина исходного сообщения {} символов".format(len(alpha_code_msg)))
def hash_value(n,alpha_code):
    i = 0
    hashing_value = 1
    while i < len(alpha_code_msg):
        hashing_value = (((hashing_value-1) + int(alpha_code_msg[i]))**2) % n
        i += 1
        print (hashing_value)
    return hashing_value

hash_code_msg = hash_value(n, alpha_code_msg)
print("Хэш сообщения", hash_code_msg)
#подпись сообщения s=Sa(m) = m^d mod n
def signature_msg(hash_code,n,d):
    sign = (hash_code**d)%n
    return sign

sign_msg = signature_msg(hash_code_msg,n,d)
print("Значение подписи: {}".format(sign_msg))
#передаём пару m,s
def check_signature(sign_msg, n,e):
    check = (sign_msg**e) % n
    print (check)
    return check

check_sign = check_signature(sign_msg,n,e)
print("Значение проверки подписи = {}".format(check_sign))
