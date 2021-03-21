'''
print(pow(*map(int, input().split()), 10007))
'''
import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.split()
    s = pow(int(s[0]),int(s[1]),10007)
    print(s)
    s = sys.stdin.readline()