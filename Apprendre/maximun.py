def max(x, y):
    if x <= y:
        return y
    else:
        return x


def max1(x, y):
    return y if x <= y else x


def max2(x, y, z):
    return z if max1(x, y) <= z else max1(x, y)

