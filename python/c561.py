import sys

for i in sys.stdin:
    s = sys.stdin.readline()
    while(s != ""):
        s = s.split()
        p = []
        for n in range(len(s)):
            m = s[n][::-1]
            p.append(m)
        print(max(list(map(int , p))))
        s = sys.stdin.readline()