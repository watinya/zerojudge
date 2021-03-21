import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.split()
    a = int(s[0])
    b = int(s[1])
    if(a % 2 != 0):
        a += 1
    if(b % 2 != 0):
        b -= 1
    n = ((b - a) / 2) + 1
    print(int(((a + b) * n) / 2))
    s = sys.stdin.readline()