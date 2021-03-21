import sys

T = eval(input())
a = 1
while(a <= T):
    num = sys.stdin.readline()
    num = num.replace("\r", "").replace("\n", "")
    t = 1
    for s in range(0,len(num)):
        t = t * int(num[s])
    print(t)
    a += 1