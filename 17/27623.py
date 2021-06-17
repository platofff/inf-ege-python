#!/usr/bin/env python3
_min, c = 7856, 0
for i in range(4855, 7856):
    if i % 8 == 0 and i % 19 == 0 and i % 7 != 0 and i % 16 != 0 and i % 24 != 0 and i % 26 != 0:
        _min = min(_min, i)
        c += 1
print(c, _min)
