import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.replace("\r", "").replace("\n", "")
    s = s.split()
    if (int(s[1]) > 0):
        a = int(s[1]) + 1
    else:
        a = int(s[1]) - 1
    for i in range(int(s[0]) , a , int(s[2])):
        print(i , end = " ")
    s = sys.stdin.readline()