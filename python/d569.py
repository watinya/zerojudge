def fib(n):
    if (n == 0 or n == 1):
        return int(n)
    else:
        return fib(n-1) + fib(n-2)

import sys

n = sys.stdin.readline()
while(int(n) != 0):
    print(fib(int(n)+1))
    n = sys.stdin.readline()