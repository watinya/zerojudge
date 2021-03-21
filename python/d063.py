import sys

s = sys.stdin.readline()
while (s != ""):
    if (int(s) == 1):
        print(0)
    else:
        print(1)
    s = sys.stdin.readline()