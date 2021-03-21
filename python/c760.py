import sys

for x in sys.stdin.read().split():
    print(x[0].upper() + x[1:])