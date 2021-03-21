# coding:UTF-8
import sys

year = sys.stdin.readline()
while (year != ""):
    year = year.replace("\r", "").replace("\n", "")
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        print("閏年")
    else:
        print("平年")
    year = sys.stdin.readline()