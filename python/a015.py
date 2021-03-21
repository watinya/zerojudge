import sys

rc = sys.stdin.readline()
while(rc != ""):
    array = []
    rc = rc.split()

    for r in range(int(rc[0])):
        s = sys.stdin.readline()
        s = s.strip("\n")
        s = s.split()
        array.append(s)

    for r in range(int(rc[1])):
        for c in range(int(rc[0])):
            print(array[c][r],end = " ")
        print()
    rc = sys.stdin.readline()