import sys

n = sys.stdin.readline()
A = sys.stdin.readline()
A = A.split()
q = eval(input())
for i in range(q):
    m = sys.stdin.readline()
    m = m.split()
    t = 0
    for i in range(int(m[0]) - 1,int(m[1])):
        t += int(A[i])
    print(t)