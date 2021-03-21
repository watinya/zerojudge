import sys

s = sys.stdin.readline()
while (s != ""):
    s = s.replace("\r", "").replace("\n", "")
    s = int(s)
    s = (s**2 - s + 2)
    print(s)
    s = sys.stdin .readline()