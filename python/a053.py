import sys

for s in sys.stdin:
    s = int(s)
    if(s >= 0 and s <= 10):
        a = s * 6
        print(a)
    elif(s >= 11 and s <= 20):
        a = 60 + (s - 10) * 2
        print(a)
    elif(s >= 21 and s <= 40):
        a = 80 + (s - 20) * 1
        print(a)
    elif(s > 40):
        print("100")