import sys
s = sys.stdin.readline()
while(s != ""):
    s = s.split()
    t = 0
    for i in range(len(s)):
        t += int(s[i])
    print(t)
    s = sys.stdin.readline()