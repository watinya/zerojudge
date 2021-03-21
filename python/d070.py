import sys

y = sys.stdin.readline()
while(y != ""):
    y.replace("\r", "").replace("\n","")
    y = int(y)
    if (y == 0):
        break
    else:
        if(y % 4 == 0 and y % 100 != 0 or y % 400 == 0):
            print("a leap year")
        else:
            print("a normal year")
    y = sys.stdin.readline()