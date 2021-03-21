import sys

T = int(input())
a = 1
while(a <= T):
    s = sys.stdin.readline()
    ss = (int(s) * (int(s) + 1)) / 2
    if(int(ss) % 3 == 0):
        print("YES")
    else:
        print("NO")
    a += 1