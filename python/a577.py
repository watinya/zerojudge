import sys

a = sys.stdin.readline()
while(a != ""):
    a = a.replace("\r", "").replace("\n", "")
    b = sys.stdin.readline()
    print(int(a) * int(b))
    a = sys.stdin.readline()