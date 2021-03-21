import sys

w = sys.stdin.readline()
while(w != ""):
    if(int(w) > 50):
        print(int(w) - 1)
    else:
        print(int(w))
    w=sys.stdin.readline()