def F(x):
    x = int(x)
    if(x == 1):
        return 1
    elif(x % 2 == 0):
        return F(x / 2)
    else:
        return F(x - 1) + F(x + 1)

import sys

s = sys.stdin.readline()
while(s != ""):
    print(F(s))
    s = sys.stdin.readline()