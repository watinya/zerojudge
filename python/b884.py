import sys

n = sys.stdin.readline()
for i in range(int(n)):
    xy = sys.stdin.readline()
    xy = xy.replace("\r","").replace("\n","")
    xy = xy.split()
    x = int(xy[0])
    y = int(xy[1])
    yee = 100 - (x + y)
    if(yee > 0 and yee <= 30):
        print("sad!")
    elif(yee > 30 and yee <= 60):
        print("hmm~~")
    elif(yee > 60 and yee < 100):
        print("Happyyummy")
    else:
        print("evil!!")