import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.replace("\n", "")
    for i in range(0,len(s)):
        print(" %s"%s[i],end = " ")
    print()
    for i in range(0,len(s)):
        if (int(s[i]) == 0):
            print(".:",end = " ")
        elif (int(s[i]) == 1 or int(s[i]) == 4 or int(s[i]) == 6):
            print(":.",end = " ")
        elif (int(s[i]) == 2 or int(s[i]) == 3 or int(s[i]) == 5):
            print("::",end = " ")
    print()
    for i in range(0,len(s)):
        if (int(s[i]) == 0 or int(s[i]) == 1):
            print("::",end = " ")
        elif (int(s[i]) == 2):
            print(":.",end = " ")
        elif (int(s[i]) == 3 or int(s[i]) == 4):
            print(".:",end = " ")
        elif (int(s[i]) == 5 or int(s[i]) == 6):
            print("..",end = " ")
    s = sys.stdin.readline()