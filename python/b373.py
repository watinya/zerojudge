import sys

n = sys.stdin.readline()
while(n != ""):
    s = sys.stdin.readline()
    s = s.replace("\n", "").replace("\r", "")
    s = list(map(int,s.split()))
    t = 0
    for i in range(len(s) - 1):
        for j in range(len(s)-1-i):
            if(s[j] > s[j + 1]):
                s[j], s[j+1] = s[j+1], s[j]
                t += 1
    print(t)
    n = sys.stdin.readline()