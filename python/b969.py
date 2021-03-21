import sys

s = sys.stdin.readline()
while(s != ""):
    g = input()
    s = s.split()
    for ss in s:
        print(g + ", " + ss)
    s = sys.stdin.readline()