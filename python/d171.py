import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.split()
    t = int(s[0]) ** int(s[1])
    print(len(str(t)))
    s = sys.stdin.readline()