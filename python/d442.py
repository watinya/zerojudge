def judge(num):
    a = 0
    for i in range(len(num)):
        a += int(num[i])**2
    return str(a)

import sys

N = sys.stdin.readline()
for N in range(eval(N)):
    num = sys.stdin.readline()
    num = num.replace("\n", "")
    result = num
    
    while(result != "1" and result != "4"):
        result = judge(result)

    if(result == "1"):
        print("Case #%s: %s is a Happy number."%(int(N)+1,num))
    elif(result == "4"):
        print("Case #%s: %s is an Unhappy number."%(int(N)+1,num))