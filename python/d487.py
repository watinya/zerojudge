def order(x):
    global a
    if (x == 0):
        return a
    else:
        a *= x
        return order(x - 1)
    
import sys

n = sys.stdin.readline()
while(n != ""):
    p = []
    a = 1
    n = int(n)
    if (n == 0 or n == 1):
        print("%s! = 1 = 1"%n)
    else:
        order(n)
        for i in range(n,0,-1):
            p.append(str(i))
        print("%s! = "%n + " * ".join(p) + " = %s"%a)
    n = sys.stdin.readline()