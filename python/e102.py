import sys

m = eval(input())
for i in range(m):
    s = sys.stdin.readline()
    while(s != ""):
        s = s.replace("\r", "").replace("\n", "")
        s = s.split()
        n = 1
        k = 1
        for i in range(int(s[0]),int(s[0]) - int(s[1]),-1):
            n *= i
        for i in range(int(s[1]),0,-1):
            k *= i
        t = n // k
        print(t)
        s = sys.stdin.readline()