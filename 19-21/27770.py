#!/usr/bin/python3
# Две кучи
from types import SimpleNamespace
def iter(k1, k2, n):
    n -= 1
    if n > 0:
        return SimpleNamespace(sum=k1 + k2, l=[iter(k1 + 1, k2, n), iter(k1, k2 + 1, n), iter(k1 * 2, k2, n), iter(k1, k2 * 3, n)])
    return SimpleNamespace(sum=k1 + k2, l=[(k1 + 1, k2), (k1, k2 + 1), (k1 * 2, k2), (k1, k2 * 3)])

for s in range(1, 67):
    combos = iter(16, s, 4)
    first_win_combos = []
    for petya1 in combos.l: # Петя 1
        for vanya1 in petya1.l: # Ваня 1
            if vanya1.sum >= 84:
                first_win_combos.append(petya1) # Добавляем комбинацию, при которой Ваня выигрывает 1 ходом
                break
    if len(first_win_combos) == 4: # Ваня может выиграть 1 ходом при любых ходах Пети
        continue
    w = 0
    for petya1 in combos.l: # Петя 1
        if petya1 not in first_win_combos:
            for vanya1 in petya1.l: # Ваня 1
                for petya2 in vanya1.l: # Петя 2
                    if petya2.sum >= 84: break # Петя не должен выиграть 2 ходом
                    for vanya2 in petya2.l: # Ваня 2
                        if sum(vanya2) >= 84: # Ваня выигрывает 2 ходом
                            w += 1
                            break
                    else: break
                else: break
            else: break
        else:
            w += 4
    if w == 16:
        print(s)
        break

