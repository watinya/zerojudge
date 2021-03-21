
import sys

for s in sys.stdin:
    s = bin(int(s))
    s = s.replace("0b","")
    print(s)
 
'''
import sys

num = sys.stdin.readline()
while(num != ""):
    print(bin(int(num)).replace("0b", ""))
    num = sys.stdin.readline()
'''