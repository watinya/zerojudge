import sys

s = sys.stdin.readline()
while (s != ""):
    s = s.replace("\r", "").replace("\n", "")
    s = int(s[:-3]+s[-2:])
    s = int(s)
    if (s >= 730 and s < 1700):
        print("At School")
    else:
        print("Off School")
    s = sys.stdin.readline()