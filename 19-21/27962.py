#!/usr/bin/python3
# Одна куча
class Combination:
    def __init__(self, _sum, l):
        self.sum = _sum
        self.l = l
def iter(k, n):
    n -= 1
    if n > 0:
        return Combination(k,
                          [iter(k + 1, n),
                           iter(k + 3, n),
                           iter(k * 2, n)])
    return Combination(k,
                      [k + 1,
                       k + 3,
                       k * 2])

for s in range(1, 67):
    combos = iter(s, 2)
    for petya1 in combos.l: # Петя 1
        for vanya1 in petya1.l: # Ваня 1
            if vanya1 >= 48:
                print(s)
                exit()

