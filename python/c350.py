def num(n,k,w):
    global a
    if(n < k):
        return a
    else:
        a += (n // k) * w
        n = n % k + (n // k) * w
        return num(n,k,w)

import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.split()
    a = int(s[0])
    num(int(s[0]),int(s[1]),int(s[2]))
    print(a)
    s = sys.stdin.readline()