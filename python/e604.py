import sys

s = sys.stdin.readline()
while(s != ""):
    t = 2 * (3 ** (int(s))) - 1
    print(t)
    s = sys.stdin.readline()