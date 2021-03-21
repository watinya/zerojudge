import sys

s = sys.stdin.readline()
while(s != ""):
    t = 1
    s = int(s)
    while(t <= s):
        print("%s. I don't say swear words!"%t)
        t = int(t) + 1
    s = sys.stdin.readline()