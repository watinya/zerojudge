import sys

s = sys.stdin.readline().replace("\n","")
while(s != "0"):
    s = s.replace(" ","")
    if(s.isalpha() == True):
        s = s.lower()
        t = 0
        for i in range(len(s)):
            t += ord(s[i])-96
        print(t)
    else:
        print("Fail")
    s = sys.stdin.readline().replace("\n","")