import sys

s = eval( sys.stdin.readline() )
while(s != ""):
    if (s >= 0 and s <= 5):
        print("0")
    elif (s >= 6 and s <= 11):
        print("590")
    elif (s >= 12 and s <= 17):
        print("790")
    elif (s >= 18 and s <= 59):
        print("890")
    elif (s >= 60):
        print("399")
    s = eval( sys.stdin.readline())