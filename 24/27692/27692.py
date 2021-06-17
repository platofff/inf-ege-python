#!/usr/bin/env python3
import re
with open('zadanie24_1.txt') as f:
	print(max([len(x) for x in re.split(r'A|C', f.read().rstrip())]))

