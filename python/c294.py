import sys

num = sys.stdin.readline()
while(num != ""):
    num = list(map(int,num.split()))
    num.sort()
    a,b,c = map(int,num)
    if(a + b <= c):
        print("%d %d %d\nNo"%(a,b,c))
    elif(a*a + b*b < c*c):
        print("%d %d %d\nObtuse"%(a,b,c))
    elif(a*a + b*b == c*c):
        print("%d %d %d\nRight"%(a,b,c))
    elif(a*a + b*b > c*c):
        print("%d %d %d\nAcute"%(a,b,c))
    num = sys.stdin.readline()