import sys

for s in sys.stdin:
    if (int(s) >= 15):
        print(int(s) - 15)
    else:
        print(int(s) + 9)