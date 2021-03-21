# coding:UTF-8
import sys

s = sys.stdin.readline()
while (s != ""):
    s = s.replace("\r", "").replace("\n", "")
    s = s.split()
    s = ( ( int(s[0]) * 2 + int(s[1]) ) % 3)
    if (s == 0):
        print("普通")
    if (s ==1):
        print("吉")
    if(s == 2):
        print("大吉")
    s = sys.stdin.readline()