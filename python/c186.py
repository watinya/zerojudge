import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.split()
    for i in range(int(len(s))):
        print(s[i])
    s = sys.stdin.readline()