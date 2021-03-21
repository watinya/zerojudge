import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.split()
    if(int(s[0]) != int(s[1])):
        print(int(s[1])+1)
    else:
        print(int(s[1]))
    s = sys.stdin.readline()