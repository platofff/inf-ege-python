#!/usr/bin/env python3
# Поиск количества чисел по заданному числу команд
r = []

def run(n, nc=0):
	global r
	if nc == 8:
		r = list(set(r + [n]))
	elif nc > 8:
		return
	else:
		nc += 1
		run(n * 8, nc)
		run(n // 2, nc)
run(512)
print(len(r))
