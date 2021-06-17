#!/usr/bin/env python3
num = 357
base = 7
new_num = ''

while num > 0:
    new_num = str(num % base) + new_num
    num //= base

print(len(new_num))

