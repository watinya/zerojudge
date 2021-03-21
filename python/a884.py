import sys

n = eval(input())
m = 1
while(m <= n):
    s = sys.stdin.readline()
    s = s.split()
    print(int(s[0]) - int(s[1]))
    m += 1