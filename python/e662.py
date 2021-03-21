import sys

num = sys.stdin.readline().split()
while(num[0] != "0" and num[1] != "0"):
    Num = num[1].replace("%s"%num[0],"").lstrip("0")
    if(Num != ""):
        print(eval(Num))
    else:
        print("0")
    num = sys.stdin.readline().split()