#!/usr/bin/env python3
from functools import lru_cache

def moves(a):
    return a + 1, a * 3 - 1

@lru_cache(None)
def game(a):
    if a >= 33:
        return 'W'
    if any(game(m) == 'W' for m in moves(a)):
        return 'P1'
    if any(game(m) == 'P1' for m in moves(a)):
        return 'B1'
    if any(game(m) == 'B1' for m in moves(a)):
        return 'P2'
    if all(game(m) == 'P2' or game(m) == 'P1' for m in moves(a)):
        return 'B2'

for s in range(1, 32):
    if game(s) is not None:
       print(game(s), s)
