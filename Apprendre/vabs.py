def vabs(x):
    if x >= 0:
        return x
    else:
        return -x


def vabs1(x):
    return x if x >= 0 else -x


def step():
    W=0
    y=W**2
    for i in range(1,4):
        W=i
        print("W",W)
        print("y=W^2",y)
        return
step()