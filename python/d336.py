import sys

t = sys.stdin.readline()
for i in range(int(t)):
    s = sys.stdin.readline()
    s = s.replace("\n", "")
    t = 0
    for i in range(len(s)):
        t += int(s[i]) * (2 ** (len(s) - i - 1))
    if(t % 3 == 0):
        print("Yes")
    else:
        print("No")