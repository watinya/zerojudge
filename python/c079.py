def num(m,n):
    global a
    if(m < n):
        return a
    else:
        a += m // n
        m = m // n + m % n
        return num(m,n)

import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.split()
    a = int(s[0])
    num(int(s[0]),int(s[1]))
    print(a)
    s = sys.stdin.readline()