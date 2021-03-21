import sys

d = sys.stdin.readline()
while(d != ""):
    dd = 1
    t = 0
    n = 1
    for i in range(50):
        t += n
        n += dd
        dd += int(d)
    print(t)
    d = sys.stdin.readline()