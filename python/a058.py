import sys

s = eval(sys.stdin.readline())
a = 0
b = 0
c = 0
for t in range(s):
    num = sys.stdin.readline()
    num = int(num)
    if (num % 3 == 0):
        a += 1
    elif(num % 3 == 1):
        b += 1
    elif(num % 3 == 2):
        c += 1
print("%d %d %d"%(a,b,c))