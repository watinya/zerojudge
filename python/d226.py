import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.split()
    print(2 * int(s[0]) * int(s[1]))
    s = sys.stdin.readline()