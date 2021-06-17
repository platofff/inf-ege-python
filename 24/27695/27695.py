#!/usr/bin/env python3
with open('zadanie24_2.txt') as f:
	data = f.read().rstrip()
last, r = '', 0
for sym in data:
	last += sym
	if last.replace('LDR', '') in ['', 'L', 'LD']:
		r = max(r, len(last))
	elif sym == 'L':
		last, r = sym, max(r, 1)
	else:
		last = ''
print(r)
