#!/usr/bin/env python3
'''
НЕ ДЛЯ ЭКЗАМЕНА!
Здесь я просто решил повыпендриваться и сделать многопоточность на уровне ОС.
Удалось добиться прироста производительности примерно в 9 раз относительно однопоточного решения на Ryzen 7 5700U (8/16 потоков) под Linux:
> time ./35915.py
14 679730035

real	0m6,141s (!)
user	0m6,137s
sys	0m0,004s

> time ./35915mp.py
14 679730035

real	0m0,709s (!)
user	0m7,789s
sys	0m0,111s
'''
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Value, cpu_count
from bisect import bisect_left

m, c = Value('i', 0), Value('i', 0)

with open('26.txt') as f:
	nums = sorted([int(x) for x in f.readlines()[1:]])
neven = []
for num in nums:
	if num % 2 == 1:
		neven.append(num)

def binary_search(a, x):
    pos = bisect_left(a, x)
    return pos != len(a) and a[pos] == x

def check(range):
	for i in range:
		for num2 in neven[i+1:]:
			avg = (neven[i] + num2) // 2
			if avg % 1 == 0.0 and binary_search(nums, avg):
				m.value = max(avg, m.value)
				c.value += 1
def main():
	with ProcessPoolExecutor() as executor:
		nlen = len(neven)
		compute_operations = sum([nlen - x for x in range(nlen)])
		per_process = compute_operations // cpu_count()
		ranges, tmp, tmp2 = [], 0, 0
		for i in range(nlen):
			tmp += nlen - i + 1
			if tmp > per_process:
				ranges.append(range(tmp2, i))
				tmp2 = i
				tmp = 0
		executor.map(check, ranges)
	print(c.value, m.value)
if __name__ == '__main__':
	main()
