# coding:UTF-8
import sys
a = ["癸", "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬"]
b = ["亥", "子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌"]

y = sys.stdin.readline()
while(y != ""):
    y = int(y) - 3
    m = y % 10
    n = y % 12
    print(a[m] + b[n])
    y = sys.stdin.readline()