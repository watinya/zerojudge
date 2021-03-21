import sys

m = sys.stdin.readline()
while(m != ""):
    m = m.split()
    m = list(map(int,m))
    m.sort()
    a,b,c = m[0],m[1],m[2]
    if (a*a + b*b < c*c):
        print('obtuse triangle')
    elif (a*a + b*b == c*c):
        print("right triangle")
    elif (a*a + b*b > c*c) :
        print("acute triangle")
    m = sys.stdin.readline()