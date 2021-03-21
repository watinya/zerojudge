import sys

s = sys.stdin.readline()
for i in range(int(s)):
    n = sys.stdin.readline()
    n = list(map(int,n.split()))
    if(n[0] > n[1]):
        print(">")
    elif(n[0] < n[1]):
        print("<")
    else:
        print("=")