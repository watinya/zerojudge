import sys

t = 0
for i in range(5):
    s = sys.stdin.readline()
    s = s.split()
    s[0] = int(s[0])
    s[1] = int(s[1])
    s[2] = int(s[2])
    s.sort()
    if (s[2] - s[0] < s[1] and s[0] + s[1] > s[2]):
        t += 1
print(t)