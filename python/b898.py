import sys

s = sys.stdin.readline()
for i in range(int(s)):
    n = sys.stdin.readline()
    n = n.split()
    print(max(list(map(int,n))))