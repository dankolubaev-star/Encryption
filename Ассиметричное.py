from math import gcd 

def _isprime(a):
    if a < 2: return False
    if a % 2 == 0:
        return a == 2
    i = 5
    while i * i <= a:
        if a % i == 0: return False 
        i += 2
    return True
def _nextp(x): 
    x = x if x % 2 else x + 1 
    while not _isprime(x): x += 2
    return x

def _inv(a, m): 
    x0, x1, r0, r1 = 1, 0, a, m
    while r1:
        q = r0 // r1
        x0, x1, r0, r1 = x1, x0 - q * x1, r1, r0 - q * r1 
    if r0 != 1: raise ValueError("e и φ простые")
    return x0 % m

def rsa_keygen(p_seed=7, q_seed=8, e=9):
    p, q = _nextp(p_seed), _nextp(q_seed if q_seed != p_seed else q_seed + 2)
    if p == q: q = _nextp(q + 2)
    a, phi = p * q, (p - 1) * (q - 1)
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1: e += 2
    d = _inv(e, phi)
    return (e, a), (d, a)

def _pack(b):
    return int.from_bytes(b, "big")

def _unpack(y):
    length = (x.bit_length() + 7) // 8 or 1
    return x.to_bytes(length, "big")

def encrypt(data, public):
    e, a = public
    b = data.encode() if isinstance(data, str) else bytes(data)
    m = _pack(b)
    if m >= a: raise ValueError("Сообщение длинное (int(msg) >= a)")
    return hex(pow(m, e, a))[2:]

def decrypt(ct_hex, private, as_text=True):
    d, a = private
    m = pow(int(ct_hex, 16), d, a)
    b = _unpack(m)
    return b.decode() if as_text else b
