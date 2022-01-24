import random
import collections
#инициализация алфавита
alphabet_lower = {'а':0, 'б':1, 'в':2, 'г':3, 'д':4,
                  'е':5, 'ж':6, 'з':7, 'и':8, 'й':9,
                  'к':10, 'л':11, 'м':12, 'н':13, 'о':14,
                  'п':15, 'р':16, 'с':17, 'т':18, 'у':19,
                  'ф':20, 'х':21, 'ц':22, 'ч':23, 'ш':24,
                  'щ':25, 'ъ':26, 'ы':27, 'ь':28, 'э':29,
                  'ю':30, 'я':31, ' ':32, ",":33, ".":34
                  }

#хэшируем сообщение
msg = input("Введите текст:")
msg_list = list(msg)
alpha_code_msg = list()
for i in range(len(msg_list)):
    alpha_code_msg.append(int(alphabet_lower.get(msg_list[i])))
print("Длина исходного сообщения {} символов".format(len(alpha_code_msg)))
def hash_value(mod,alpha_code):
    i = 0
    hashing_value = 1
    while i < len(alpha_code_msg):
        hashing_value = (((hashing_value-1) + int(alpha_code_msg[i]))**2) % curve.p
        i += 1
    return hashing_value

#класс точки, нужен для хранения точек и вывода их
class Point:
    def __init__(self,x_init,y_init):
        self.x = x_init
        self.y = y_init

    def shift(self, x, y):
        self.x += x
        self.y += y

    def __repr__(self):
        return "".join(["( x=", str(self.x), ", y=", str(self.y), ")"])

x_1=0 #магические переменные, которые хранят координаты точки Q
y_1=0 #магические переменные, которые хранят координаты точки Q
EllipticCurve = collections.namedtuple('EllipticCurve', 'name p q_mod a b q g n h') #тюпл(статичный массив, именной, хранит переменные(параметры эк))
curve = EllipticCurve(
    'secp256k1',
    #параметры поля
    #модуль поля
    p=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f,
    q_mod = 0xfffffffffefffffffffcfffffffffffcfffffffffffffffffffffffefffffc2f,
    #коэфф а и b
    a=7,
    b=11,
    #Базовая точка эк записано в hex
    g=(0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
    0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8),
    q=(0xA0434D9E47F3C86235477C7B1AE6AE5D3442D49B1943C2B752A68E2A47E247C7,
       0x893ABA425419BC27A3B6C7E693A24C696F794C2ED877A1593CBEE53B037368D7),
    #Подгруппа группы точек
    n=0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141,
    #Подгруппа
    h=1,
)
print("Q mod",int(curve.q_mod))
print("P mod",int(curve.p))
def is_on_curve(point):
    """Возвращает True если точка лежит на элиптической кривой."""
    if point is None:
        return True

    x, y = point

    return (y * y - x * x * x - curve.a * x - curve.b) % curve.p == 0

def point_neg(point):
    """Инвертирует точку по оси y -point."""
    #assert is_on_curve(point)

    if point is None:
        # -0 = 0
        return None

    x, y = point
    result = (x, -y % curve.p)

    #assert is_on_curve(result)

    return result

def inverse_mod(k, p):
    """Возвращает обратное k по модулю p.
    Эта функция возвращает число x удовлетворяющее условию (x * k) % p == 1.
    k не должно быть равно 0 и p должно быть простым.
    """
    if k == 0:
        raise ZeroDivisionError('деление на 0')

    if k < 0:
        # k ** -1 = p - (-k) ** -1  (mod p)
        return p - inverse_mod(-k, p)

    # Раширенный алгоритм Евклида.
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = p, k

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    gcd, x, y = old_r, old_s, old_t

    assert gcd == 1
    assert (k * x) % p == 1

    return x % p

def point_add(point1, point2):
    """Возвращает результат операции сложения point1 + point2 оперируя законами операции над группами."""
    #assert is_on_curve(point1)
    #assert is_on_curve(point2)

    if point1 is None:
        # 0 + point2 = point2
        return point2
    if point2 is None:
        # point1 + 0 = point1
        return point1

    x1, y1 = point1
    x2, y2 = point2

    if x1 == x2 and y1 != y2:
        # point1 + (-point1) = 0
        return None

    if x1 == x2:
        # This is the case point1 == point2.
        m = (3 * x1 * x1 + curve.a) * inverse_mod(2 * y1, curve.p)
    else:
        # This is the case point1 != point2.
        m = (y1 - y2) * inverse_mod(x1 - x2, curve.p)

    x3 = m * m - x1 - x2
    y3 = y1 + m * (x3 - x1)
    result = (x3 % curve.p,
              -y3 % curve.p)

    #assert is_on_curve(result)

    return result

def scalar_mult(k, point):
    """Возвращает k * точку используя дублирование и алгоритм сложения точек."""
    #assert is_on_curve(point)

    if k % curve.n == 0 or point is None:
        return None

    if k < 0:
        # k * point = -k * (-point)
        return scalar_mult(-k, point_neg(point))

    result = None
    addend = point

    while k:
        if k & 1:
            # Add.
            result = point_add(result, addend)

        # Double.
        addend = point_add(addend, addend)

        k >>= 1

    #assert is_on_curve(result)

    return result

#Вывод хэш-значения
hash_code_msg = hash_value(curve.p, alpha_code_msg)
print("Хэш сообщения:={}".format(hash_code_msg))
#вычисляем е, обращаемся через тюпл к перемнной p
e = hash_code_msg%curve.q_mod
print("E={}".format(e))
#генерация k
k = random.randint(1,curve.q_mod)
print("K={}".format(k))
print("")
#нахождение точки элиптической кривой из базовый точки C=K * P(x,y)
d = 10
print("D={}".format(d))
x,y = scalar_mult(k,curve.g)
point_c = Point(x,y)
print("Point_C={}".format(point_c))
r = point_c.x % curve.q_mod
print("R={}".format(r))
s = (r*curve.p + k*e)%curve.q_mod
print("S={}".format(s))
#проверка подписи
v = inverse_mod(e,curve.p)
print("V={}".format(v))
z1 = (s*v)%curve.q_mod
z2 = ((curve.p-r)*v)%curve.q_mod
x_1,y_1 = scalar_mult(d,curve.g)
print("Point_Q=( x={}, y={} )".format(x_1,y_1))
point_c_new = Point(x,y)
x,y = point_add(scalar_mult(z1,curve.g),
                scalar_mult(z2,curve.q))
r_1 = point_c_new.x% curve.q_mod
print("R_new={}".format(r_1))
if r == r_1:
    print("Подпись прошла проверку!")
else:
    print("Ошибка проверки!")
