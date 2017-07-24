from Apprendre import Polynome

def bissextiles(n):
    return ((n % 4 == 0) and (n % 100 != 0)) or (n % 400 == 0)

p = Polynome([1, 2, 0, 3])
print(p.deg())

