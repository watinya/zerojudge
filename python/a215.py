import sys

for s in sys.stdin:
    s = s.split()
    n = 1
    a = int(s[0])
    b = int(s[1])
    q = a
    while(q != ""):
        if (q > b):
            print(n)
            break
        else:
            n += 1
            a += 1
            q += a