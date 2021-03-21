import sys

for s in sys.stdin:
    s.replace("/", "//")
    print(eval(s))
    