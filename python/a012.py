import sys

for s in sys.stdin:
    s = s.split()
    a = int(s[0])
    b = int(s[1])
    if (a > b):
        print(a - b)
    else:
        print(b - a)