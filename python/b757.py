import sys

r = sys.stdin.readline()
while(r != ""):
    r = float(r)
    R = (r * 9) / 5 + 32
    if (float(R) == int(R)):
        print(int(R))
    else:
        print("%g"%R)
    r = sys.stdin.readline()