import sys

s = sys.stdin.readline()
while(s != ""):
    n = sys.stdin.readline()
    n = n.split()
    x = list(map(int,n))
    x.sort()
    y = list(set(x))
    y.sort()
    y = y[::-1]
    print(" ".join(list(map(str,x))))
    print(" ".join(list(map(str,y))))
    s = sys.stdin.readline()