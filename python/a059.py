import sys

s = eval(input())
for t in range(s):
    a = eval(sys.stdin.readline())
    b = eval(sys.stdin.readline())
    p = 0
    for i in range(40):
        if ((i ** 2) >= a and (i ** 2) <= b ):
            p += (i ** 2)
    print("Case %s: %d"%(t+1,p))