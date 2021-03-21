import sys

for n in sys.stdin:
    s = sys.stdin.readline()
    while(s != ""):
        s = s.replace("\r", "").replace("\n", "")
        s = s.split()
        print (max(list(map(int , s))))
        s = sys.stdin.readline()