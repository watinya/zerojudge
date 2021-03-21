import sys

s = sys.stdin.readline()
while(s != ""):
    n = sys.stdin.readline()
    n = n.split()
    n = list(map(int,n))
    n.sort()
    print(" ".join(list(map(str,n))))
    s = sys.stdin.readline()