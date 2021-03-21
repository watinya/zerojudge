import sys

w = sys.stdin.readline()
while(w != ""):
    h = sys.stdin.readline()
    bmi = '%4.1f'%(int(w)/(int(h)/100)**2)
    print(bmi)
    w = sys.stdin.readline()