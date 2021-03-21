import sys

for n in sys.stdin:
    s = sys.stdin.readline()
    s = s.replace("\r", "").replace("\n", "")
    s = s.split()
    d = 1
    t = 0
    for s in s:
        s = int(s)
        t += s*d
        d += 1
    print(t)