def is_simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

def is_primitive(n, w):
    for p in range(2, n + 1):
        if n % p == 0 and is_simple(p) and w ** (n / p) - 1 == 0:
            return False
    return True
