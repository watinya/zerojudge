import sys

n = sys.stdin.readline()
while(n != ""):
    a = 1
    while(a < int(n)):
        if (n == 0):
            break
        elif (a % 7 != 0):
            print(a,end = " ")
        a += 1
    print()
    n = sys.stdin.readline()