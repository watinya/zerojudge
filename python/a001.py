# coding:UTF-8  

import sys
s = sys.stdin.readline()
while(s != ""):
    s = s.replace("\r", "").replace("\n", "")
    print("hello, "+s)
    s = sys.stdin.readline()
