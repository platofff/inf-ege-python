#!/usr/bin/env python3
from bisect import bisect_left

with open('26.txt') as f:
	data = sorted([int(x) for x in f.readlines()[1:]])
neven = []
for x in data:
	if x % 2 == 1:
		neven.append(x)

def binary_search(a, x):
	'''
	Это НАМНОГО быстрее обычной проверки x in list.
	Работает только с сортированными списками.
	Запомни, иначе придётся ждать по 10 минут.
	'''
	pos = bisect_left(a, x)
	return pos != len(a) and a[pos] == x

c, avg_max = 0, 0

for i in range(len(neven)):
	for j in range(i + 1, len(neven)):
		avg = (neven[i] + neven[j]) // 2
		if binary_search(data, avg):
			c += 1
			avg_max = max(avg_max, avg)
print(c, avg_max)
