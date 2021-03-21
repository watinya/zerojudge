import sys

for s in sys.stdin:
    s = s.split()
    a = int(s[0])
    b = int(s[1])
    if (a % 2 == 0 and b % 2 == 0):
        ans = int ((b - a) / 2 + 1)
        print(ans)
    elif(a % 2 == 0 and b % 2 != 0 or a % 2 != 0 and b % 2 == 0):
        ans = int((b - a) // 2 + 1)
        print(ans)
    elif (a % 2 != 0 and b % 2 != 0):
        ans = int((b - a) / 2)
        print(ans)