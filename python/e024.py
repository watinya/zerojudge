import sys

s = sys.stdin.readline()
a,b = map(int,s.split())
while(a != 0 and b != 0):
    print(a ** b)
    s = sys.stdin.readline()
    a,b = map(int,s.split())