# coding:UTF-8
import sys

s = sys.stdin.readline()
for i in range(0,len(s)):
    print(s[i],end="")
    if (s[i] == "@"):
        print("【跳1行】\n1",end="")
    if (s[i] == "$"):
        print("【跳2行】\n1\n2",end="")
    if (s[i] == "#"):
        print("【跳3行】\n1\n2\n3",end="")
    if (s[i] == "!"):
        print("【跳4行】\n1\n2\n3\n4",end="")
    if (s[i] == "%"):
        print("【跳5行】\n1\n2\n3\n4\n5",end="")