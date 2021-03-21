import sys

s = sys.stdin.readline()
while(s != ""):
    s = int(s)
    f = (s * (s + 1)) / 2
    g = (s * (s + 1) * (s + 2)) / 6
    print("%.0f %.0f"%(f,g))
    s = sys.stdin.readline()