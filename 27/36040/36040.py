#!/usr/bin/env python3
with open('27_B.txt') as f:
	triades = [sorted([int(y) for y in x.split()]) for x in f.readlines()[1:]]

k, min_diff, s = 109, 20000, 0
for triade in triades:
	s += triade[2]
	max_mid = triade[2] - triade[1]
	max_min = triade[2] - triade[0]
	if max_mid % k != 0:
		min_diff = min(min_diff, max_mid)
	elif max_min % k != 0:
		min_diff = min(min_diff, max_min)

print(s if s % k != 0 else s - min_diff)
