import sys

s = sys.stdin.readline()
while(s != ""):
    n = int(s)
    if (n % 3 == 0):
        print("yes")
    else:
        print("no")
    s = sys.stdin.readline()