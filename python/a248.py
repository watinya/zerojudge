import sys

s = sys.stdin.readline()
while(s != ""):
    a,b,c = map(int,s.split())
    print(a//b, end = ".")
    
    cnt = 2
    n = "%f" %(a/b - a//b)
    while(n[cnt] == "0" and cnt <= c):
        print("0", end = "")
        cnt += 1
    
    print("%d" %((a * (10**c)) // b - a // b * (10**c)))
    s = sys.stdin.readline()