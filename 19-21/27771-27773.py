#!/usr/bin/env python3
# WIP: неправильный ответ на 19
# Взято с https://www.youtube.com/watch?v=bPuqNdSm3nM
# Допилил https://github.com/RedMaun
from functools import lru_cache

def moves(h):
    a, b = h
    # Если в куче остаётся на 1 меньше
    return (a - 1, b), (a, b - 1), (a // 2, b), (a, b // 2)
    # Если в куче остаётся на 1 больше
    # return (a - 1, b), (a, b - 1), ((a + 1) // 2, b), (a, (b + 1) // 2)

@lru_cache(None)
def game(h):
    if sum(h) <= 20:
        return 'W'
    if min(h) == 0:
        return None
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if any(game(m) == 'P1' for m in moves(h)):
        return 'B1'
    if any(game(m) == 'B1' for m in moves(h)):
        return 'P2'
    if all(game(m) == 'P2' or game(m) == 'P1' for m in moves(h)):
        return 'B2'

for s in range(11, 100):
    if game( (10, s) ) is not None:
       print(game( (10,s) ), s)
       pass
