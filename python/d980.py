import sys

T = sys.stdin.readline()
for i in range(1,int(T)+1):
    s = sys.stdin.readline()
    s = list(map(int,s.split()))
    s.sort()
    a,b,c = s[0],s[1],s[2]
    if((a > 0 and b > 0 and c > 0) and a+b>c and c-b<a):
        if(a == b == c):
            print("Case %d: Equilateral"%i)
        elif(a == b or b == c or c == a):
            print("Case %d: Isosceles"%i)
        else:
            print("Case %d: Scalene"%i)
    else:
        print("Case %d: Invalid"%i)