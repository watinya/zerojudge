import sys

n = eval(input())
a = 1
while(a <= n):
    y = sys.stdin.readline()
    if (int(y) % 4 == 0 and int(y) % 100 != 0 or int(y) % 400 == 0):
        print("Case %d: a leap year"%a)
    else:
        print("Case %d: a normal year"%a)
    a += 1