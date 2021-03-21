import sys

n = eval(input())
s = sys.stdin.readline()
s = s.split()
while(n == int(len(s))):
    s.sort()
    n = " ".join(s)
    print(n)