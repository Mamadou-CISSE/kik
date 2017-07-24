class Polynome(object):
    def __init__(self, coefficients):
        self.coefs = coefficients

    def deg(self):
        n = len(self.coefs)
        for i, c in enumerate(reversed(self.coefs)):
            if c != 0:
                return n - 1 - i
        return -1


p = Polynome([1, 2, 0, 3])
print(p.deg())
