import sys

s = sys.stdin.readline()
while(s != ""):
    for i in s:
        i = chr( ord(i) - 7 )
        print(i,end = "")
    print()
    s = sys.stdin.readline()