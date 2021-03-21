import sys

s = sys.stdin.readline()
while(s != ""):
    s = eval(s)
    print("%.0f"%s)
    s = sys.stdin.readline()