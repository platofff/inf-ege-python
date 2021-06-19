#!/usr/bin/env python3
# Прислал https://vk.com/xfce.optimization
def d(n, m):
    return n % m == 0

def f(x, a):
    _1 = d(x, a)
    _2 = d(x, 21) + d(x, 35)
    return not(_1) or _2

for a in range(1, 50_000):
    ok = True
    for x in range(1, 50_000):
        if not(f(x, a)):
            ok = False
            break
    if ok:
        print(a)
        exit()
