import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.replace("\r", "").replace("\n", "")
    s = s.split()
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    D = b ** 2 - 4 * a * c
    a1 = ( (-b + ((b ** 2 - 4 * a * c) ** (1 / 2)) ) / (2 * a))
    a2 = ( (-b - ((b ** 2 - 4 * a * c) ** (1 / 2)) ) / (2 * a))
    if (D > 0):
        print("Two different roots x1=%d , x2=%d"%(a1,a2) )
    elif (D == 0):
        print("Two same roots x=%d"%a1)
    elif (D < 0):
        print("No real root")
    s = sys.stdin.readline()