import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.split()
    ss = list(set(s))
    for i in range(len(ss)):
        if(s.count(ss[i]) == 2):
            print(ss[i])
            break
    s = sys.stdin.readline()