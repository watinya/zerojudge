import sys

x = sys.stdin.readline()
while(x != ""):
    x = x.replace("\r", "").replace("\n", "")
    a = 0
    b = 0
    for i in range(1,len(x),2):
        a += int(x[i])
    for i in range(0,len(x),2):
        b += int(x[i])
    print(abs(a - b))
    x = sys.stdin.readline()