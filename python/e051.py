import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.replace("\r", "").replace("\n", "")
    l = "_" * (int(len(s))-2)
    print("%s%s%s"%(s[0],l,s[(-1)]))
    s = sys.stdin.readline()