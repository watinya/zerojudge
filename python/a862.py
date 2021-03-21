import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.split()
    V = eval(s[0])
    R = eval(s[1])
    I = (V / R) * 1000
    print("%.4f"%I)
    s = sys.stdin.readline()