import sys

N = sys.stdin.readline()
while(N != ""):
    s = sys.stdin.readline()
    for i in range(0,len(s),int(N)+1):
        print(s[i],end = "")
    print()
    N = sys.stdin.readline() 