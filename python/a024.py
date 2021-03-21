def gcd(a,b):
    while b:
        r = a % b
        a = b
        b = r
    return a 

import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.split()
    print(gcd(int(s[0]) , int(s[1])))
    s = sys.stdin.readline()