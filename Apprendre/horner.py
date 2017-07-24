def horner(p, x):
    if len(p) == 1:
        return p[0]
    p[-2] += x * p[-1]
    return horner(p[:-1], x)