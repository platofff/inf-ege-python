#!/usr/bin/env python3
# Количество программ с обязательным и избегаемым этапами
c = 0

def run(n, w10=False, w16=False):
	global c
	if n == 10:
		w10 = True
	if n == 16:
		w16 = True
	if n > 21:
		return
	elif n == 21:
		if w10 and not w16:
			c += 1
	else:
		run(n + 1, w10, w16)
		run(n * 2, w10, w16)
run(1)
print(c)
