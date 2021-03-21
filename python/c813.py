import sys

s = sys.stdin.readline()
while(int(s) != 0):
    s = int(s)
    if(s % 9 != 0):
        print(s % 9)
    else:
        print("9")
    s = sys.stdin.readline()