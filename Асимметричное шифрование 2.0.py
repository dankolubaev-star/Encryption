from math import gcd

def _isprime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        if n == 2:
            return True 
        else:
            return False
i = 3
while i * i <= n: 
    if n % i == 0:
        return False
    i = i + 2
    return True

def _nextprime(x):
    if x <= 2:
        return 2
    if x % 2 == 0:
        x += 1
    while not _isprime(x):
        x += 2 
    return x

def _inverse(a, m):
    x0, x1 = 1, 0
    r0, r1 = a, m 
while r1 != 0:
    q = r0 // r1
         old_r0, old_r1 = r0, r1
         old_x0, old_x1 = x0, x1
         r0 = old_r1
         r1 = old_r0 - q * old_r1
         x0 = old_x1
         x1 = old_x0 - q * old_x1
if r0 != 1:
    raise ValueError("Ошибка, нет обратного по молудю")
return x0 % m

def rsa_keygen(p_seed=7, q_seed=11, e=3):
    p = _nextprime(p_seed) 
    q = _nextprime(q_seed)
    if p == q:
        q = _nextprime(q + 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2
    d = inverse(e, phi) 
    return (e, n), (d, n)

def encrypt(message, public_key):
    e, n = public_key
    message_bytes = message.encode()
    m = int.from_bytes(message_bytes, "big")
    if m >= n:
        raise ValueError("Много символом")
    c = pow(m, e, n)
    return c

def decrypt(ciphertext, private_key):
    d, n = private_key
    m = pow(ciphertext, d, n)
    message_bytes = m.to_bytes((m.bit_length() + 7) // 8, "big")
    message = message_bytes.decode()
    return message
       
