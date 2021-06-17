#!/usr/bin/env python3
# Подсчет количества слов с ограничениями
c = 0
for i in range(100000, 999999):
	l = [int(x) for x in list(str(i))]
	if len(set(l)) == 6 and i % 5 == 0 and [x % 2 == 0 for x in l] in [[False, True, False, True, False, True], [True, False, True, False, True, False]]:
		c += 1
print(c)
