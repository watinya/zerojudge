import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.split()
    p = []
    m = int(s[0])
    n = int(s[1])
    while(m <= n):
        t = 0
        for i in str(m):
            t += int(i) ** int(len(str(m)))
        if (t == m):
            p.append(str(m))
        m += 1
    a = " ".join(p)
    if(a != ""):
        print(a)
    else:
        print("none")
    s = sys.stdin.readline()