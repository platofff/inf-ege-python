#!/usr/bin/env python3
# Дискретные множества
a = {}
def asearch(x, inv=False):
        global a
        if not inv:
                a = set(list(a) + [x])
                return True
        else:
                l = list(a)
                try:
                        l.pop(l.index(x))
                        a = set(l)
                except ValueError:
                        pass
                return False

Q = {3, 6, 9, 12, 15}
P = {2, 4, 6, 8, 10, 12}

for x in range(0, 100):
        if not (x not in P or (not (x in Q and not asearch(x)) or x not in P)):
                asearch(x, True)
print(sum(a))

