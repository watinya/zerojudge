import sys

for n in sys.stdin:
    p = input()
    p = p.split()
    print (max(list(map(int , p))))