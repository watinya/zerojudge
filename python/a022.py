import sys

s = sys.stdin.readline()
while (s != ""):
    s = s.replace("\r", "").replace("\n", "")
    ss = s[::-1]
    if (s == ss):
        print("yes")
    else:
        print("no")
    s = sys.stdin.readline()