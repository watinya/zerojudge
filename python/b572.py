import sys

N = int(input())
a = 1
while(a <= N):
    time = sys.stdin.readline()
    time = time.replace("\r", "").replace("\n", "")
    time = time.split()
    s = ( int(time[2]) - int(time[0]) ) * 60 + int(time[3]) - int(time[1])
    if (s >= int(time[4])):
        print("Yes")
    else:
        print("No")
    a += 1