import sys
Num = sys.stdin.readline()
while( Num != ""):
    Num = Num.replace("\r", "").replace("\n", "")
    if (int(Num) >= 0):
        print(Num)
    else:
        print(int(Num)*(-1))
    Num = sys.stdin.readline()

'''
import sys

s = sys.stdin.readline()
while(s != ""):
    print(abs(int(s)))
    s = sys.stdin.readline()
'''