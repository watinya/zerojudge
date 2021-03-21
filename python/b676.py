import sys

for s in sys.stdin:
    s = int(s)
    if(s % 5 == 0):
        print("U")
    elif(s % 5 == 1):
        print("G")
    elif(s % 5 == 2):
        print("Y")
    elif(s % 5 == 3):
        print("T")
    elif(s % 5 == 4):
        print("I")