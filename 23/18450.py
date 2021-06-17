#!/usr/bin/env python3
# Количество программ с обязательным этапом
c = 0

def run(n, w14=False):
	global c
	if n == 14:
		w14 = True
	if n > 29:
		return
	elif n == 29:
		if w14:
			c += 1
	else:
		run(n + 1, w14)
		run(n * 2, w14)
run(2)
print(c)
