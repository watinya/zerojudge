import sys

for s in sys.stdin:
    n = input()
    n = n.split()
    a = 0
    for w in range(int(len(n))):
        if (int(n[w]) <= 10):
            a += 1
    print(a)