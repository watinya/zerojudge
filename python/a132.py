import sys

n = sys.stdin.readline()
while(int(n) != 0):
    m = bin(int(n)).replace("0b","")
    c = str(m).count("1")
    print("The parity of %s is %s (mod 2)."%(m,c))
    n = sys.stdin.readline()