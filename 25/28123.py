#!/usr/bin/env python3
for i in range(125256, 125330):
	divs = []
	for j in range(2, i + 1):
		if j % 2 == 0 and i % j == 0:
			divs.append(str(j))
	if len(divs) == 6:
		print(' '.join(divs))
