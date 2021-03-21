import sys

m = sys.stdin.readline()
n = sys.stdin.readline()
m = m.replace(":"," ")
n = n.replace(":"," ")
m = m.split()
n = n.split()
t = 0
for p in range(0,len(m),2):
    for q in range(0,len(n),2):
        if(int(m[p]) == int(n[q])):
            t = t + int(m[p + 1]) * int(n[q + 1])
print(t)