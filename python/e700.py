# coding:UTF-8
import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.replace("\n","").replace("/"," ")
    s = s.split()
    s = int(s[0]) * 100 + int(s[1])
    if (s >= 121 and s <= 219):
        print("水瓶座")
    elif(s >= 220 and s <= 320):
        print("雙魚座 ")
    elif(s >= 321 and s <= 420):
        print("牡羊座")
    elif(s >= 421 and s <= 521):
        print("金牛座")
    elif(s >= 522 and s <= 621):
        print("雙子座")
    elif(s >= 622 and s <= 722):
        print("巨蟹座")
    elif(s >= 723 and s <= 821):
        print("獅子座")
    elif(s >= 822 and s <= 923):
        print("處女座")
    elif(s >= 924 and s <= 1023):
        print("天秤座")
    elif(s >= 1024 and s <= 1122):
        print("天蠍座")
    elif(s >= 1123 and s <= 1222):
        print("射手座")
    elif(s >= 1223 or s <=120):
        print("摩羯座")
    s = sys.stdin.readline()