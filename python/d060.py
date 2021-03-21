import sys

Min = sys.stdin.readline()
while (Min != ""):
    Min = int(Min)
    if (Min > 25):
        print(85 - Min)
    else:
        print(25 - Min)
    Min = sys.stdin.readline()