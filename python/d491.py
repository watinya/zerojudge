import sys

s = sys.stdin.readline()
while(s != ""):
    p = []
    s = s.split()
    for i in range(2):
        L = int(s[i])
        p.append(L)
    p.sort()
    a = int(p[0])
    b = int(p[1])
    if(a % 2 != 0):
        a += 1
    if(b % 2 != 0):
        b -= 1
    n = ((b - a) / 2) + 1
    print(int(((a + b) * n) / 2))
    s = sys.stdin.readline()