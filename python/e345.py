import sys

s = sys.stdin.readline()
while(s != ""):
    if(int(s) != 0):
        print((int(s) - 1) % 9 + 1)
    else:
        print(0)
    s = sys.stdin.readline()