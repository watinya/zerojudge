import sys

s = sys.stdin.readline()
while(s != ""):
    for s in range(int(s)):
        n = input()
        n = n.split()
        a = int(n[0])
        b = int(n[1])
        c = int(n[2])
        if (a == 1):
            print(b + c)
        elif(a == 2):
            print(b - c)
        elif(a == 3):
            print(b * c)
        elif(a == 4):
            print(b // c)
    s = sys.stdin.readline()