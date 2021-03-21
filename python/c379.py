import sys

s = sys.stdin.readline()
while(s != ""):
    s = int(s)
    s = int(s * (3 / 10))
    print(s)
    s = sys.stdin.readline()