import sys

s1 = sys.stdin.readline()
s2 = sys.stdin.readline()
while(s1 != ""):
    s1 = s1.replace("\r", "").replace("\n", "")
    s2 = s2.replace("\r", "").replace("\n", "")
    print("%s and %s sitting in the tree"%(s1,s2))
    s1 = sys.stdin.readline()
    s2 = sys.stdin.readline()