import sys

s = sys.stdin.readline()
while(s != ""):
    s = s.replace("\n", "").replace("\r", "")
    t = 0
    i = 1
    while(i < len(s)):
        if("A" <= s[i] <= "Z" or "a" <= s[i] <= "z"):
            if("A" > s[i-1] or "a" > s[i-1] > "Z" or s[i-1] > "z"):
                t += 1
        i += 1
    print(t + 1)
    s = sys.stdin.readline()