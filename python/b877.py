import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.replace("\r", "").replace("\n", "")
    s = s.split()
    if (s[1] >= s[0]):
        ss = int(s[1]) - int(s[0])
        print(ss)
    else:
        ss = 100 - int(s[0]) + int(s[1])
        print(ss)
    s = sys.stdin.readline()