import sys

N = sys.stdin.readline().replace("\n", "")
while(N != "0"):
    a,b = 0,0
    for m in range(0,len(N),2):
        a += int(N[m])
    for n in range(1,len(N),2):
        b += int(N[n])
    if ((a-b) % 11 == 0):
        print("%s is a multiple of 11."%N)
    else:
        print("%s is not a multiple of 11."%N)
    N = sys.stdin.readline().replace("\n", "")