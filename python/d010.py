# coding:UTF-8
import sys

s = sys.stdin.readline()
while(s != ""):
    t = 0
    for i in range(1,int(s)):
        if(int(s) % i == 0):
            t += i
    if (t > int(s)):
        print("盈數")
    elif (t == int(s)):
        print("完全數")
    elif (t < int(s)):
        print("虧數")
    s = sys.stdin.readline()