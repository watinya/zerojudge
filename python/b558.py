import sys

s = sys.stdin.readline()
while(s != ""):
    s = int(s)
    num = 1 + ((s * (s - 1)) / 2)
    print("%.0f"%num)
    s = sys.stdin.readline()