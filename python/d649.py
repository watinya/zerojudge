import sys

s = sys.stdin.readline()
while(s != ""):
    s = eval(s)
    for i in range(1,s+1):
        i = int(i)
        print("_" * (s-i) + "+" * i)
    s = sys.stdin.readline()
