import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.split()
    print(s[0] + " and " + s[1] + " sitting in the tree")
    s = sys.stdin.readline()