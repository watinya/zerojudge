import sys

n = sys.stdin.readline()
while(n != ""):
    p = []
    for i in range(int(n)):
        s = sys.stdin.readline()
        p.append(s)
    p.sort()
    print("\n".join(p))
    n = sys.stdin.readline()