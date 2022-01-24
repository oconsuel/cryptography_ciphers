import random
import collections

alphabet_lower = {'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4,
            'е': 5, 'ё': 6, 'ж': 7, 'з': 8, 'и': 9, 'й': 10,
            'к': 11, 'л': 12, 'м': 13, 'н': 14, 'о': 15,
            'п': 16, 'р': 17, 'с': 18, 'т': 19, 'у': 20,
            'ф': 21, 'х': 22, 'ц': 23, 'ч': 24, 'ш': 25,
            'щ': 26, 'ъ': 27, 'ы': 28, 'ь': 29, 'э': 30,
            'ю': 31, 'я': 32
            }


class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init

    def shift(self, x, y):
        self.x += x
        self.y += y

    def __repr__(self):
        return "".join(["( x=", str(self.x), ", y=", str(self.y), ")"])


x_1 = 0
y_1 = 0

EllipticCurve = collections.namedtuple(
    'EllipticCurve', 'name p q_mod a b q g n h')
curve = EllipticCurve(
    'secp256k1',
    p=0x17A5C9F23BC278000000000000000000000000000000000,
    q_mod=0x3C825B847BC0E60000000000000000000000000000000000000000,

    a=7,
    b=11,

    g=(0x3C825B847BC0E60000000000000000000000000000000000000000,
       0xBB3809F12E50080000000000000000000000000000000000000000),
    q=(0x172F11F4F0DE7E00000000000000000000000000000000000,
       0x122E265BE03CF000000000000000000000000000000000000000),

    n=0x168D57CB4705C200000000000000000000000000000000000000,

    h=0x17BA7A383CD13B000000000000000000000000000000000000000,
)


def ciphergostd(clearText):
    msg = clearText
    msg_list = list(msg)
    alpha_code_msg = list()
    for i in range(len(msg_list)):
        alpha_code_msg.append(int(alphabet_lower.get(msg_list[i])))
    print("Длина исходного сообщения {} символов".format(len(alpha_code_msg)))

    print("Q mod", int(curve.q_mod))
    print("P mod", int(curve.p))

    hash_code_msg = hash_value(curve.p, alpha_code_msg)
    print("Хэш сообщения:={}".format(hash_code_msg))

    e = hash_code_msg % curve.q_mod
    print("E={}".format(e))

    k = random.randint(1, curve.q_mod)
    print("K={}".format(k))

    d = 10
    print("D={}".format(d))
    x, y = scalar_mult(k, curve.g)
    point_c = Point(x, y)
    print("Point_C={}".format(point_c))
    r = point_c.x % curve.q_mod
    print("R={}".format(r))
    s = (r*curve.p + k*e) % curve.q_mod
    print("S={}".format(s))

    v = inverse_mod(e, curve.p)
    print("V={}".format(v))
    z1 = (s*v) % curve.q_mod
    z2 = ((curve.p-r)*v) % curve.q_mod
    x_1, y_1 = scalar_mult(d, curve.g)
    print("Point_Q=( x={}, y={} )".format(x_1, y_1))
    point_c_new = Point(x, y)
    x, y = point_add(scalar_mult(z1, curve.g),
                     scalar_mult(z2, curve.q))
    r_1 = point_c_new.x % curve.q_mod
    print("R_new={}".format(r_1))
    if r == r_1:
        print("Подпись прошла проверку!\n")
    else:
        print("Ошибка проверки!")


def hash_value(mod, alpha_code_msg):
    i = 0
    hashing_value = 1
    while i < len(alpha_code_msg):
        hashing_value = (
            ((hashing_value-1) + int(alpha_code_msg[i]))**2) % curve.p
        i += 1
    return hashing_value


def is_on_curve(point):
    if point is None:
        return True

    x, y = point

    return (y * y - x * x * x - curve.a * x - curve.b) % curve.p == 0


def point_neg(point):
    if point is None:
        return None
    x, y = point
    result = (x, -y % curve.p)
    return result


def inverse_mod(k, p):
    if k == 0:
        raise ZeroDivisionError('деление на 0')

    if k < 0:
        return p - inverse_mod(-k, p)

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
    if point1 is None:
        return point2
    if point2 is None:
        return point1

    x1, y1 = point1
    x2, y2 = point2

    if x1 == x2 and y1 != y2:
        return None

    if x1 == x2:
        m = (3 * x1 * x1 + curve.a) * inverse_mod(2 * y1, curve.p)
    else:
        m = (y1 - y2) * inverse_mod(x1 - x2, curve.p)

    x3 = m * m - x1 - x2
    y3 = y1 + m * (x3 - x1)
    result = (x3 % curve.p,
              -y3 % curve.p)
    return result


def scalar_mult(k, point):
    if k % curve.n == 0 or point is None:
        return None

    if k < 0:
        return scalar_mult(-k, point_neg(point))

    result = None
    addend = point

    while k:
        if k & 1:
            result = point_add(result, addend)
        addend = point_add(addend, addend)
        k >>= 1
    return result


def main():
    print('ГОСТ Р 34.10-2012:')

if __name__ == "__main__":
    main()
