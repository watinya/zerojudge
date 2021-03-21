import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.replace("\r", "").replace("\n", "")
    m = int(s) // 12
    n = int(s) - 12 * m
    t = m * 50 + n * 5
    print(t)
    s = sys.stdin.readline()