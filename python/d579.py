import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.replace("\r", "").replace("\n", "")
    s = eval(s)
    print("|%.4f|=%.4f"%(s,abs(s)))
    s = sys.stdin.readline()