import sys

s = sys.stdin.readline()
for i in range(int(s)):
    n = sys.stdin.readline()
    n = n.split()
    n = list(map(int,n))
    if(n[1] / n[0] == n[2] / n[1]):
        d = n[2] / n[1]
        n.append(int(int(n[3]) * d))
        print(" ".join(list(map(str,n))))
    else:
        d = n[2] - n[1]
        n.append(int(n[3]) + d)
        print(" ".join(list(map(str,n))))

'''
import sys

t = int(input())
while t > 0:
    for a in sys.stdin:
        a = a.replace("\r", "").replace("\n", "")
        a,b,c,d = map (int,a.split())
        if ( a-b == b-c ):
            print(a , b , c , d , (2*d - c ))
        else:
            print(a , b , c , d , "%.0f"%( d * (d/c)) )
        t = t - 1
'''

'''        
import sys

t = int(input())
while(t > 0):
    s = sys.stdin.readline()
    while(s != ""):
        s = s.replace("\r", "").replace("\n", "")
        s = s.split()
        if ( int(s[1]) / int(s[0]) == int(s[2]) / int(s[1]) ):
            print( int(s[0]) , int(s[1]) , int(s[2]) , int(s[3]) , int(int(s[3]) * ( int(s[3]) / int(s[2]) )))
        else:
            print( int(s[0]) , int(s[1]) , int(s[2]) , int(s[3]) , int(int(s[3]) + ( int(s[3]) - int(s[2]) )))
        s = sys.stdin.readline()
    t = t - 1
'''