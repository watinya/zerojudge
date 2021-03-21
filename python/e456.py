import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.split()
    for i in range(len(s) - 1):
        print("%s little, "%s[i],end = "")
    print("%s little Indians"%s[-1])
    s = sys.stdin.readline()