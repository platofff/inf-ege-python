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
    combos = iter(s, 4)
    first_win_combos = []
    for petya1 in combos.l:
        for vanya1 in petya1.l:
            if vanya1.sum > 48:
                first_win_combos.append(petya1) # Добавляем комбинацию, при которой Ваня выигрывает 1 ходом
                break
    if len(first_win_combos) == 3: # Ваня может выиграть 1 ходом при любых ходах Пети
        continue
    w = 0
    for petya1 in combos.l: # Петя 1
        if petya1 not in first_win_combos:
            for vanya1 in petya1.l: # Ваня 1
                for petya2 in vanya1.l: # Петя 2
                    if petya2.sum >= 48: break # Петя может выигать 2 ходом - пропускаем
                    for vanya2 in petya2.l:
                        if vanya2 >= 48: # Ваня может выиграть 2 ходом, добавляем 1 ко счётчику
                            w += 1
                            break
                    else: break
                else: break
            else: break
        else:
            w += 3
    if w == 9:
        print(s)
        break
