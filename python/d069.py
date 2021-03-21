import sys

t = eval(input())
a = 1
while(a <= t):
    year = sys.stdin.readline()
    if (int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0):
        print("a leap year")
    else:
        print("a normal year")
    a += 1