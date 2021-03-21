import sys

s = sys.stdin.readline()
while(s != ""):
    s = int(s)
    t = ((1 + s) * s) / 2
    print(int(t))
    s = sys.stdin.readline()