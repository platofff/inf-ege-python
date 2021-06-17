#!/usr/bin/env python3
# Поиск количества программ по заданному числу
c = 0

def run(n):
	global c
	if n > 57:
		return
	elif n == 57:
		c += 1
	else:
		run(n + 1)
		run(n + 10)
run(35)
print(c)
