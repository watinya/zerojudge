import sys

s = sys.stdin.readline()
while (s != ""):
    s = s.replace("\r", "").replace("\n", "")
    print("Go, %s, go go"%s)
    s = sys.stdin.readline()