import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.split()
    t = 0
    for i in range(1,len(s)):
        t += int(s[i])
    if (t > 59 * int(s[0])):
        print("no")
    else:
        print("yes")
    s = sys.stdin.readline()