#!/usr/bin/env python3
with open('27985_B.txt') as f:
	nums = list([int(x) for x in f.readlines()][1:])

r2, r7, r14 = 0, 0, 0
for num in nums:
	if num % 14 == 0:
		r14 = max(r14, num)
	if num % 2 == 0:
		r2 = max(r2, num)
	if num % 7 == 0:
		r7 = max(r7, num)
print(max(r2 * r7, r14 * max(nums)))
