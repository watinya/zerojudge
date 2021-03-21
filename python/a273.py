import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.split()
    a,b = int(s[0]),int(s[1])
    if(a == 0):
        print("Ok!")
    elif (a != 0 and b == 0):
        print("Impossib1e!")
    elif(a % b == 0):
        print("Ok!")
    else:
        print("Impossib1e!")
    s = sys.stdin.readline()