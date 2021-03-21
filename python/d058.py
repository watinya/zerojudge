import sys

s = sys.stdin.readline()
while(s != ""):
    s = int(s)
    if (s > 0):
        print(1)
    elif(s == 0):
        print(0)
    elif(s < 0):
        print(-1)
    s = sys.stdin.readline()