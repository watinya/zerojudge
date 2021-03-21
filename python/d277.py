import sys

N = sys.stdin.readline()
while(N != ""):
    N = int(N)
    if(N % 2 == 0):
        print(N)
    else:
        print(N - 1)
    N = sys.stdin.readline()