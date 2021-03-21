import sys

s = sys.stdin.readline()
while (s != ""):
    s = s.replace("\r", "").replace("\n", "")
    s = int(s)
    s = (1+ (s * (s**2+5)) / 6 )
    print("%.0f"%s)
    s = sys.stdin .readline()