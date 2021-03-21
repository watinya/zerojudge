'''
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
'''   
def gcd(a,b):
    c = a // b
    d = a % b
    if d != 0:
        return gcd(b,d)
    else:
        return b

import sys

for s in sys.stdin:
    s = s.split()
    if (len(s) == 2):
        a = int(s[0])
        b = int(s[1])
        if (a > b):
            print(gcd(a,b))
        elif (a < b):
            print(gcd(b,a))
        else:
            print(a)