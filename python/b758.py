def time():
    global h,m
    if (m < 10):
        m = "0%s"%m
    if (h < 10):
        h = "0%s"%h
    return

import sys

s = sys.stdin.readline()
while(s != ""):
    if (s == "\n"):
        s = sys.stdin.readline()
        continue
    s = s.replace("\r","").replace("\n","")
    s = s.split()
    mm = int(s[0]) * 60 + int(s[1]) + 150
    h = mm // 60
    m = mm % 60
    if (h >= 24):
        h -= 24
        time()
        print("%s:%s"%(h,m))
    else:
        time()
        print("%s:%s"%(h,m))
    s = sys.stdin.readline()