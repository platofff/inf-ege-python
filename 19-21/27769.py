#!/usr/bin/python3
# Две кучи
class Combination:
    def __init__(self, _sum, l):
        self.sum = _sum
        self.l = l
def iter(k1, k2, n):
    n -= 1
    if n > 0:
        return Combination(k1 + k2,
                          [iter(k1 + 1, k2, n),
                           iter(k1, k2 + 1, n),
                           iter(k1 * 2, k2, n),
                           iter(k1, k2 * 3, n)])
    return Combination(k1 + k2,
                      [(k1 + 1, k2),
                       (k1, k2 + 1),
                       (k1 * 2, k2),
                       (k1, k2 * 3)])

for s in range(1, 67):
    combos = iter(16, s, 3)
    
    w = 0
    for petya1 in combos.l: # Петя 1
        if petya1.sum >= 84: break
        for vanya1 in petya1.l: # Ваня 1
            if vanya1.sum >= 84:
                w = 0
                break
            for petya2 in vanya1.l: # Петя 2
                if sum(petya2) >= 84:
                    w += 1
                    break
            else: break
        else: break
    else: continue
    
    if w == 4:
        print(s)

