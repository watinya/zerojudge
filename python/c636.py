# coding:UTF-8

import sys

p = ["豬","鼠","牛","虎","兔","龍","蛇","馬","羊","猴","雞","狗"]
s = sys.stdin.readline()
while(s != ""):
    s = s.replace("\r", "").replace("\n", "")
    if(int(s) > 0):
        i = int(s) % 12
        print(p[i])
    else:
        i = (int(s) + 13) % 12
        print(p[i])
    s = sys.stdin.readline()