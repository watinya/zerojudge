import sys

T = sys.stdin.readline()
for i in range(int(T)):
    N = sys.stdin.readline()
    w = sys.stdin.readline()
    w = w.split()
    m,n = 0,0
    for p in range(int(N) - 1):
        if(w[p] < w[p+1]):
            m += 1
        elif(w[p] > w[p+1]):
            n += 1
    print("Case %s: %s %s"%(int(i)+1,m,n))