import sys

for s in sys.stdin:
    s = s.split()
    a = 0
    for year in range(int(s[0]),int(s[1])+1):
        if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
            a += 1
    print(a)