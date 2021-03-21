import sys

m = sys.stdin.readline()
while(m != ""):
    n = sys.stdin.readline()
    t = ord(n[0]) - ord(m[0])
    if(t >= 0):
        print(t)
    else:
        print(t+26)
    m = sys.stdin.readline()