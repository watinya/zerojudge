import sys

s = sys.stdin.readline()
while(s != ""):
    m,n = map(int,s.split())
    ans = m * (m+1) * n * (n+1) / 4
    print(int(ans))
    s = sys.stdin.readline()