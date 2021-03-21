import sys

f = sys.stdin.readline()
while(f != ""):
    c = 5 / 9 * (int(f) - 32)
    print("%.3f"%c)
    f = sys.stdin.readline()