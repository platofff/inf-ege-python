#!/usr/bin/env python3
# Количество программ с избегаемым этапом
c = 0

def run(n, w612=False):
	global c
	if n in [6, 12]:
		w612 = True
	if n > 16:
		return
	elif n == 16:
		if not w612:
			c += 1
	else:
		run(n + 1, w612)
		run(n * 2, w612)
		run(n + 3, w612)
run(3)
print(c)
