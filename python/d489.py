import sys

N = sys.stdin.readline()
while(N != ""):
    N = N.split()
    a = int(N[0])
    b = int(N[1])
    c = int(N[2])
    s = (a + b + c) / 2
    ans = s * (s - a) * (s - b) * (s - c)
    print("%.0f"%ans)
    N = sys.stdin.readline()