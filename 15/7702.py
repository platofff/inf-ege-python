#!/usr/bin/env python3
P = {2, 4, 6, 8, 10, 12}
Q = {4, 8, 12, 16}
A = {}

def get_a(x, f=False):
	global A
	if not f:
		A = set(list(A) + [x])
		return True
	else:
		al = list(A)
		try:
			al.pop(al.index(x))
		except ValueError:
			pass
		A = set(al)

def f(x):
	return (x not in P) or not ((x in Q and not get_a(x)) or x not in P)

for i in range(0, 1000):
	if not f(i):
		get_a(i, f=True)

print(sum(A))
