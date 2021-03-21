import sys

i = sys.stdin.readline()
while(i != ""):
    p = []
    i = i.replace("\r", "").replace("\n", "")
    for n in range(int(len(i))-1):
        s = abs(ord(i[n]) - ord(i[n+1]))
        p.append(str(s))
    ans = "".join(p)
    print(ans)
    i = sys.stdin.readline()
    
'''
import sys

i = sys.stdin.readline()
while(i != ""):
    i = i.replace("\r", "").replace("\n", "")
    a = 0
    p = []
    pp = []
    for n in range(len(i)):
        if(i[n] == "A"):
            a = 1
        if(i[n] == "B"):
            a = 2
        if(i[n] == "C"):    
            a = 3
        if(i[n] == "D"):
            a = 4
        if(i[n] == "E"):
            a = 5
        if(i[n] == "F"):
            a = 6
        if(i[n] == "G"):
            a = 7
        if(i[n] == "H"):
            a = 8
        if(i[n] == "I"):
            a = 9
        if(i[n] == "J"):
            a = 10
        if(i[n] == "K"):
            a = 11
        if(i[n] == "L"):
            a = 12
        if(i[n] == "M"):
            a = 13
        if(i[n] == "N"):
            a = 14
        if(i[n] == "O"):
            a = 15
        if(i[n] == "P"):
            a = 16
        if(i[n] == "Q"):
            a = 17
        if(i[n] == "R"):
            a = 18
        if(i[n] == "S"):
            a = 19
        if(i[n] == "T"):
            a = 20
        if(i[n] == "U"):
            a = 21
        if(i[n] == "V"):
            a = 22
        if(i[n] == "W"):
            a = 23
        if(i[n] == "X"):
            a = 24
        if(i[n] == "Y"):
            a = 25
        if(i[n] == "Z"):
            a = 26
        p.append(a)
    for n in range(0,len(p)-1):
        s = p[n+1] - p[n]
        if (s >= 0):
            pp.append(s)
        else:
            s = s * (-1)
            pp.append(s)
    for n in range(len(pp)):
        print(pp[n],end = "")
    print()
    i = sys.stdin.readline()
'''