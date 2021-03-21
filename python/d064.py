import sys

s = sys.stdin.readline()
while (s != ""):
    if (int(s) % 2 == 1):
        print("Odd")
    else:
        print("Even")
    s = sys.stdin.readline()