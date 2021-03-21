import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.split()
    ss = " " + s[0] + " "
    print(ss.join(s[1:]))
    s = sys.stdin.readline()