def composition(f, g):
    return lambda x: f(g(x))