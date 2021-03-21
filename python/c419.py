import sys

s = eval(sys.stdin.readline())
for ss in range(1,s+1):
    print("_" * int(s-ss) + "*" * ss)