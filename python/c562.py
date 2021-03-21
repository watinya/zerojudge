import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.replace("\n","")
    t = 0
    for i in range(len(s)):
        if (int(s[i]) == 0 or int(s[i]) == 6 or int(s[i]) == 9):
            t += 1
        elif(int(s[i]) == 8):
            t += 2
    print(t)
    s = sys.stdin.readline()