import sys
s = sys.stdin.readline()
while(s != ""):
    s = s.replace("\r", "").replace("\n", "")
    s = s.split()
    print(int(s[0]) + int(s[1]))
    s = sys.stdin.readline()