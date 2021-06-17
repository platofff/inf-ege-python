#!/usr/bin/env python3
with open('27-B_demo.txt') as f:
	pairs = [[int(y) for y in x.split()] for x in f.readlines()[1:]]

r, min_diff = 0, 0

for i in range(len(pairs)):
	r += min(pairs[i])
	diff = abs(pairs[i][0] - pairs[i][1])
	if min_diff % 3 != 0:
		min_diff = min(min_diff, diff)

if r % 3 == 0:
	r += min_diff

print(r)
