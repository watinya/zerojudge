import sys

N = sys.stdin.readline()
for i in range(int(N)):
    s = sys.stdin.readline()
    s = s.split()
    if (int(s[2]) - int(s[0]) < int(s[1]) and int(s[0]) + int(s[1]) > int(s[2])):
        print("OK")
    else:
        print("Wrong!!")