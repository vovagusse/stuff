def add_one(x):
    return x + 1

def sq(x):
    return x * x

def applyfunctions(l,n):
    for f in l:
        print(f(x))

applyfunctions([add_one, sq, float], 4)