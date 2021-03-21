import sys

s = sys.stdin.readline()
while(s != ""):
    n = sys.stdin.readline()
    for i in range(1,int(s)+1):
        print(i,end = " ")
    print()
    s = sys.stdin.readline()