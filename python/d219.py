import sys

b = sys.stdin.readline()
while(b != ""):
    b = int(b)
    p = sys.stdin.readline()
    w = sys.stdin.readline()
    p = int(p)
    w = int(w)
    print(pow(b,p,w))
    b = sys.stdin.readline()