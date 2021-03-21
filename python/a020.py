import sys

i = sys.stdin.readline()
while(i != ""):
    i = i.replace("\r", "").replace("\n", "")
    a = 0
    if(i[0] == "A"):
        a = 10
    if(i[0] == "B"):
        a = 11
    if(i[0] == "C"):    
        a = 12
    if(i[0] == "D"):
        a = 13
    if(i[0] == "E"):
        a = 14
    if(i[0] == "F"):
        a = 15
    if(i[0] == "G"):
        a = 16
    if(i[0] == "H"):
        a = 17
    if(i[0] == "I"):
        a = 34
    if(i[0] == "J"):
        a = 18
    if(i[0] == "K"):
        a = 19
    if(i[0] == "L"):
        a = 20
    if(i[0] == "M"):
        a = 21
    if(i[0] == "N"):
        a = 22
    if(i[0] == "O"):
        a = 35
    if(i[0] == "P"):
        a = 23
    if(i[0] == "Q"):
        a = 24
    if(i[0] == "R"):
        a = 25
    if(i[0] == "S"):
        a = 26
    if(i[0] == "T"):
        a = 27
    if(i[0] == "U"):
        a = 28
    if(i[0] == "V"):
        a = 29
    if(i[0] == "W"):
        a = 32
    if(i[0] == "X"):
        a = 30
    if(i[0] == "Y"):
        a = 31
    if(i[0] == "Z"):
        a = 33

    num = ((a - a % 10) / 10) + (a % 10) * 9
    isum = num + int(i[1])*8 + int(i[2])*7 + int(i[3])*6 + int(i[4])*5 + int(i[5])*4 + int(i[6])*3 + int(i[7])*2 + int(i[8]) + int(i[9])

    if (isum % 10 == 0):
        print("real")
    else:
        print("fake")
    i = sys.stdin.readline()