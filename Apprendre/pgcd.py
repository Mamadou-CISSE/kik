def reste(a, b):
    if b == 0:
        return None
    while a >= b:
        a -= b
    return a


def pgcd(a, b):
    while b > 0:
        a, b = b, reste(a, b)
    return a

