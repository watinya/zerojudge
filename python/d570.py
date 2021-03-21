import sys

n = sys.stdin.readline()
n = n.replace("\n","")
for i in range(int(len(n))-1,-1,-1):
    print(n[0:i+1],end = "")
    print()