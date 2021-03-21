import sys

s = sys.stdin.readline()
while(s != ""):
    p = []
    for i in range(int(s)):
        n = sys.stdin.readline()
        p.append(int(n))
    p.sort()
    p = list(map(str,p))
    print("\n".join(p))
    s = sys.stdin.readline()