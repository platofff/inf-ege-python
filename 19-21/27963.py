#!/usr/bin/python3
# Одна куча
from itertools import chain

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
    combos = iter(s, 3)
    w = 0
    for petya1 in combos.l: # Петя 1
        if petya1.sum >= 48: # Петя может выиграть 1 ходом - пропускаем
            w = 0
            break
        for vanya1 in petya1.l: # Ваня 1
            if vanya1.sum >= 48: # Ваня может выиграть 2 ходом - пропускаем
                w = 0
                break
            for petya2 in vanya1.l: # Петя 2
                if petya2 >= 48:
                    w += 1
                    break
            else: break
        else: break

    if w > 0:
        print(s)
