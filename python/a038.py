import sys

Num = sys.stdin.readline()
while (Num != ""):
    Num = Num.replace("\r", "").replace("\n", "")
    Num = Num.rstrip("0")[::-1]
    if (Num == ""):
        print("0")
    else:
        print(Num)
    Num = sys.stdin.readline()