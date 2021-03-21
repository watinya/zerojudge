import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.replace(":"," ")
    s = s.split()
    m = 0
    n = 0
    for i in range(0,len(s),2):
        if(int(s[i]) % 2 == 1):
            m += eval(s[i + 1])
        else:
            n += eval(s[i + 1])
    print(round(m - n,3))
    s = sys.stdin.readline()