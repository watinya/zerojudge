import sys

Num = sys.stdin.readline()
while(Num != ""):
    if (int(Num) % 3 == 0):
        Ans = int(Num)//3
        print(Ans)
    else:
        Ans = int(Num) // 3 + 1
        print(Ans)
    Num = sys.stdin.readline()